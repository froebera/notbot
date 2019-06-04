from discord.ext import commands as cmd
from discord.ext import tasks as tsk
from astutus.utils import Duration, checks, Truthy, get_hms
from typing import Optional
import arrow
from datetime import datetime


class TTKey(cmd.Converter):
    async def convert(self, ctx: cmd.Context, arg):
        if arg.lower() not in [
            "grandmaster",
            "gm",
            "master",
            "captain",
            "knight",
            "recruit",
            "guest",
            "applicant",
            "timer",
            "tier",
            "zone",
            "average",
            "avg",
            "announce",
            "farm",
        ]:
            await ctx.send(f"**{arg}** is not a valid settings key for TT2 module.")
            raise cmd.BadArgument("Bad key for TT2 settings")
        if arg == "average":
            arg == "avg"
        elif arg == "grandmaster":
            arg == "gm"
        if (
            arg in "gmmastercaptainknightrecruitapplicantguest"
            and not checks.can_manage_roles()
        ):
            raise cmd.BadArgument()
        elif arg == "announce" and not checks.can_manage_channels():
            raise cmd.BadArgument()
        return arg.lower()


class TTRaidGroup(cmd.Converter):
    async def convert(self, ctx, arg):
        if arg[0] != "g" or arg[1] not in ("1", "2", "3"):
            raise cmd.BadArgument()
        elif arg == "gm":
            raise cmd.BadArgument()
        else:
            return f"{ctx.guild.id}:tt:{arg[1]}"


class TapTitansModule(cmd.Cog):
    def __init__(self, bot: cmd.Bot):
        self.bot = bot
        self.raid_timer.start()

    async def get_roles(self, ctx, group, *roles):
        result = []
        for role in roles:
            r = await self.bot.db.hget(group, role)
            if r:
                result.append(int(r))
        return result

    @tsk.loop(minutes=1.0)
    async def raid_timer(self):
        return

    @cmd.group(case_insensitive=True)
    async def tt(self, ctx):
        pass

    @tt.group(name="set")
    @cmd.guild_only()
    async def tt_set(self, ctx, group: Optional[TTRaidGroup], key: TTKey, val):
        if group == None:
            group = f"{ctx.guild.id}:tt:1"
        if key in "gmmastercaptainknightrecruitapplicantguest":
            val = await cmd.RoleConverter().convert(ctx, val)
            await self.bot.db.hset(group, key, val.id)
        elif key == "announce":
            val = await cmd.TextChannelConverter().convert(ctx, val)
            await self.bot.db.hset(group, key, val.id)
        elif key in "zonetier":
            try:
                val = int(val)
            except:
                raise cmd.BadArgument(f"Bad value for raid {key}")
            else:
                if not 1 <= val <= 10:
                    raise cmd.BadArgument()
                await self.bot.db.hset(group, key, val)
        elif key == "farm":
            val = await Truthy().convert(ctx, val)
            await self.bot.db.hset(group, key, val)
        else:
            await self.bot.db.hset(group, key, val)
        await ctx.send(f"Set the TT2 **{key}** key to **{val}**")

    @tt.group(
        name="raid",
        aliases=["boss", "rd"],
        case_insensitive=True,
        invoke_without_command=True,
    )
    async def tt_raid(
        self,
        ctx,
        group: Optional[TTRaidGroup],
        level: cmd.Greedy[int],
        time: Optional[Duration],
    ):
        if group == None:
            group = f"{ctx.guild.id}:tt:1"
        roles = await self.get_roles(ctx, group, "gm", "master", "timer")
        if not await checks.user_has_role((r.id for r in ctx.author.roles), *roles):
            raise cmd.BadArgument
        is_live = await self.bot.db.hget(group, "spawn")
        reset = await self.bot.db.hget(group, "reset")
        if not reset:
            reset = "starts"
        else:
            reset = f"reset #**{reset}** is"
        if is_live:
            dt = arrow.get(is_live) - arrow.utcnow()
            _h, _m, _s = await get_hms(dt)
            await ctx.send(f"Raid {reset} in **{_h}**h **{_m}**m **{_s}**s.")
            return
        if not level or len(level) == 0 or level == None:
            tier = await self.bot.db.hget(group, "tier") or 1
            zone = await self.bot.db.hget(group, "zone") or 1
        elif not all(1 <= x <= 10 for x in level):
            await ctx.send("Tier/zone must be between **1** and **10**.")
            raise cmd.BadArgument()
        elif len(level) == 2:
            tier, zone = level
        elif len(level) == 1:
            tier, zone = level, 1
        if not time or time == None:
            time = await Duration().convert(ctx, "24h")
        await self.bot.db.hset(group, "spawn", time.timestamp)
        time = time.humanize()
        if time == "just now":
            time = "now"
        await ctx.send(f"Tier **{tier}**, zone **{zone}** raid starts **{time}**.")

    @tt_raid.command(name="clear", aliases=["end", "ended", "cleared"])
    async def tt_raid_clear(self):
        return

    @tt_raid.command(name="cancel", aliases=["abort", "stop"])
    async def tt_raid_cancel(self, ctx, group: Optional[TTRaidGroup]):
        if group == None:
            group = f"{ctx.guild.id}:tt:1"
        result = await self.bot.db.hdel(group, "spawn")
        if not result:
            await ctx.send("No raid to cancel.")
            return
        await self.bot.db.delete(f"{group}:q")
        await ctx.send("Cancelled the current raid.")

    @tt_raid.command(name="info", aliases=["information"])
    async def tt_raid_info(self):
        return

    @tt.command(name="queue", aliases=["q"], case_insensitive=True)
    async def tt_queue(self, ctx, group: Optional[TTRaidGroup], list=None):
        if group == None:
            group = f"{ctx.guild.id}:tt:1"
        roles = await self.get_roles(
            ctx, group, "gm", "master", "captain", "knight", "recruit"
        )
        if not await checks.user_has_role((r.id for r in ctx.author.roles), *roles):
            raise cmd.BadArgument

        result = await self.bot.db.hget(group, "spawn")
        if not result:
            await ctx.send("No raid/reset to queue for.")
            return
        resets = await self.bot.db.hget(group, "resets")
        if not resets:
            resets = "first spawn"
        else:
            resets = f"reset #{resets}"
        q = f"{group}:q"
        users = await self.bot.db.lrange(q)

        if not list:
            if not str(ctx.author.id) in users:
                await self.bot.db.rpush(q, ctx.author.id)
                users.append(ctx.author.id)
            else:
                await ctx.send(
                    f"You're already #**{users.index(str(ctx.author.id))+1}** in the queue, **{ctx.author}**."
                )
                return
        u = []
        for user in users:
            user_obj = await self.bot.fetch_user(int(user))
            u.append(f"{len(u)+1}. {user_obj}")
        await ctx.send(
            "**Queue** for **{}**:\n```{}```\nUse **;tt unqueue** to cancel.".format(
                resets, "\n".join(u)
            )
        )

    @tt.command(name="unqueue", aliases=["unq"], case_insensitive=True)
    async def tt_unqueue(self, ctx, group: Optional[TTRaidGroup]):
        if group == None:
            group = f"{ctx.guild.id}:tt:1"
        roles = await self.get_roles(
            ctx, group, "gm", "master", "captain", "knight", "recruit"
        )
        if not await checks.user_has_role((r.id for r in ctx.author.roles), *roles):
            raise cmd.BadArgument

        result = await self.bot.db.hget(group, "spawn")
        if not result:
            await ctx.send("No raid/reset to queue for.")
            return
        resets = await self.bot.db.hget(group, "resets")
        if not resets:
            resets = "first spawn"
        else:
            resets = f"reset #{resets}"
        q = f"{group}:q"
        users = await self.bot.db.lrange(q)

        if not str(ctx.author.id) in users:
            await ctx.send(f"You're not in the queue, **{ctx.author}**.")
            return
        res = await self.bot.db.lrem(q, str(ctx.author.id))
        if res:
            await ctx.send(f"Ok **{ctx.author}**, I removed you from the queue.")

    @tt.group(name="card", case_insensitive=True)
    async def tt_card(self):
        return

    @tt.group(name="deck", case_insensitive=True)
    async def tt_deck(self):
        return

    @tt.group(name="hero", case_insensitive=True)
    async def tt_hero(self):
        return

    @tt.group(name="equip", case_insensitive=True)
    async def tt_equip(self):
        return

    @tt.group(name="artifact", case_insensitive=True)
    async def tt_artifact(self):
        return

    @tt.group(name="enhancement", case_insensitive=True)
    async def tt_enhance(self):
        return

    @tt.group(name="enchant", case_insensitive=True)
    async def tt_enchant(self):
        return

    @tt.group(name="titan", case_insensitive=True)
    async def tt_titan(self):
        return

    @tt.group(name="titanlord", case_insensitive=True)
    async def tt_titanlord(self):
        return

    @tt.group(name="skill", case_insensitive=True)
    async def tt_skill(self):
        return


def setup(bot):
    bot.add_cog(TapTitansModule(bot))
