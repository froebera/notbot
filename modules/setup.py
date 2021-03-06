"""Setup module."""

import asyncio
from typing import Optional
import discord
from discord.ext import commands as cmd
from .utils import checks


def lget(l, idx, default):
    """Safely get a list object"""
    try:
        return l[idx]
    except IndexError:
        return default


class SetupModule(cmd.Cog):
    """Easy-to-use setup commands for getting the bot up and running."""

    def __init__(self, bot: cmd.Bot):
        self.bot = bot

    @checks.is_mod()
    @cmd.group(name="setup", invoke_without_command=True)
    async def setup(self, ctx):
        return

    async def setup_tt2_key(self, ctx, group, kind, phase=None):
        await ctx.send(
            "Let's set up a clan {}. Please type it in now.{}".format(
                kind,
                ""
                if kind != "raid queue size"
                else "\nNOTE: if you do not plan on using queues, **enter 6 for this step**. You can change this later.",
            )
        )

        def check(msg):
            if msg.author != ctx.author and ctx.guild != msg.guild:
                return 0
            if msg.content.lower().strip() in ["exit", "cancel"]:
                raise cmd.BadArgument("Exiting setup.")
            if kind == "name":
                return len(msg.content) > 4 and len(msg.content) < 30
            if kind == "code":
                return len(msg.content) <= 7 and len(msg.content) >= 4
            if kind == "announce channel":
                if len(msg.content) > 30:
                    return 0
                if msg.clean_content.isdigit() and discord.utils.get(
                    ctx.guild.channels, id=int(msg.clean_content)
                ):
                    return 1
                if msg.clean_content[0] == "#" and discord.utils.get(
                    ctx.guild.channels, name=msg.clean_content[1:]
                ):
                    return 1
                if discord.utils.get(ctx.guild.channels, name=msg.clean_content):
                    return 1
                asyncio.ensure_future(ctx.send(f"Unrecognised channel: {msg.content}"))
                return 0
            if kind.endswith(" role"):
                if len(msg.content) > 30:
                    return 0
                if msg.clean_content.isdigit() and discord.utils.get(
                    ctx.guild.roles, id=int(msg.clean_content)
                ):
                    return 1
                if msg.clean_content[0] == "@" and discord.utils.get(
                    ctx.guild.roles, name=msg.clean_content[1:]
                ):
                    return 1
                if discord.utils.get(ctx.guild.roles, name=msg.clean_content):
                    return 1
                asyncio.ensure_future(ctx.send(f"Unrecognised role: {msg.content}"))
                return 0
            if kind == "raid queue size":
                if msg.content not in "1 2 3 4 5 6".split():
                    asyncio.ensure_future(
                        ctx.send(f"{kind.title()} must be between 1 and 5")
                    )
                    return 0
                return 1
            if kind.startswith("raid "):
                if msg.content not in "1 2 3 4 5 6 7 8 9 10".split():
                    asyncio.ensure_future(
                        ctx.send(f"{kind.title()} must be between 1 and 10")
                    )
                    return 0
                return 1

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
        except asyncio.TimeoutError:
            raise cmd.BadArgument(
                "Query timed out. Exiting setup. Type **;setup tt2** to return."
            )

        val = msg.clean_content
        if kind == "name":
            key = kind
        elif kind == "code":
            _, db_res = await self.bot.db.hscan("cc", match=msg.clean_content.lower())
            if db_res:
                raise cmd.BadArgument(
                    "Clan already using that code. Contact bot owner. Exiting..."
                )
            c_code = await self.bot.db.hget(group, kind)
            if c_code == msg.clean_content.lower():
                raise cmd.BadArgument("You are using this code already. Exiting...")
            in_use = lget(db_res, 1, 0)
            if in_use and in_use != str(ctx.guild.id):
                raise cmd.BadArgument(
                    "Clan already using that code. Contact bot owner. Exiting..."
                )
            val = msg.clean_content.lower()
            key = kind
        elif kind == "announce channel":
            key = kind.replace(" channel", "")
            val = await cmd.TextChannelConverter().convert(ctx, msg.content)
            val = val.id
        elif kind.endswith(" role"):
            key = kind.replace(" role", "")
            try:
                val = await cmd.RoleConverter().convert(ctx, msg.content)
            except cmd.BadArgument:
                raise cmd.BadArgument(f"**{msg.content}** not a valid channel.")
            val = val.id
        elif kind == "raid queue size":
            key = "mode"
            val = int(val)
        elif kind.startswith("raid "):
            key = kind.replace("raid ", "")
            val = int(val)

        await self.bot.db.hset(group, key, val)
        await self.bot.db.hset(group, "ph", phase)
        await ctx.send(
            f":white_check_mark: Set the clan **{kind}** to **{msg.content}**."
        )
        return phase

    @checks.is_mod()
    @setup.command(name="greet")
    async def setup_greet(self, ctx):
        done = await self.bot.db.hget(f"{ctx.guild.id}:setup", "greet")
        if done is not None and done == "1":
            raise cmd.BadArgument(
                f"Already set up greet! **{ctx.prefix}help settings greet**"
            )
        await ctx.send("Greet setup initiated.")

        if done is None:
            chans = list(enumerate(ctx.guild.text_channels))[0:30]
            embed = await self.bot.embed()
            embed.description = "\n".join([f"{x+1}. {y.mention}" for x, y in chans])
            ms1 = await ctx.send(
                "Set the **greet channel** by choosing a number below:", embed=embed
            )

            def check(msg):
                return (
                    msg.author == ctx.author
                    and msg.guild == ctx.guild
                    and msg.content in map(str, [x + 1 for x, y in chans])
                )

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            except asyncio.TimeoutError:
                raise cmd.BadArgument(
                    f"Query timed out. Type **{ctx.prefix}setup greet** to return."
                )

            await ms1.delete()
            chosen = chans[int(msg.content) - 1][1]
            if not chosen.permissions_for(ctx.guild.me).send_messages:
                raise cmd.BadArgument(
                    f"No send permissions. Type **{ctx.prefix}setup greet** to return."
                )
            await self.bot.db.hset(f"{ctx.guild.id}:set", "grtc", chosen.id)
            await ctx.send(f"Set the greet channel to {chosen.mention}!")
            await self.bot.db.hset(f"{ctx.guild.id}:setup", "greet", "0")

        ms2 = await ctx.send(
            "Choose a **greet message** (limit 140 chars):\nFormat tags: {user} {server} {user.mention}"
        )

        def check2(msg):
            return (
                msg.author == ctx.author
                and msg.guild == ctx.guild
                and msg.content[0:140]
            )

        try:
            msg = await self.bot.wait_for("message", check=check2, timeout=60.0)
        except asyncio.TimeoutError:
            raise cmd.BadArgument(
                f"Query timed out. Type **{ctx.prefix}setup greet** to return."
            )

        await ms2.delete()

        await self.bot.db.hset(f"{ctx.guild.id}:set", "grt", msg.content[0:140])
        await self.bot.db.hset(f"{ctx.guild.id}:setup", "greet", "1")
        await self.bot.db.hset(f"{ctx.guild.id}:toggle", "greet", "1")
        embed = await self.bot.embed()
        embed.description = msg.content[0:140].format(user=ctx.author, server=ctx.guild)
        await ctx.send("Set the greet message:", embed=embed)

    @checks.is_mod()
    @setup.command(name="goodbye")
    async def setup_goodbye(self, ctx):
        done = await self.bot.db.hget(f"{ctx.guild.id}:setup", "goodbye")
        if done is not None and done == "1":
            raise cmd.BadArgument(
                f"Already set up greet! **{ctx.prefix}help settings goodbye**"
            )
        await ctx.send("Goodbye setup initiated.")

        if done is None:
            chans = list(enumerate(ctx.guild.text_channels))[0:30]
            embed = await self.bot.embed()
            embed.description = "\n".join([f"{x+1}. {y.mention}" for x, y in chans])
            ms1 = await ctx.send(
                "Set the **goodbye channel** by choosing a number below:", embed=embed
            )

            def check(msg):
                return (
                    msg.author == ctx.author
                    and msg.guild == ctx.guild
                    and msg.content in map(str, [x + 1 for x, y in chans])
                )

            try:
                msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            except asyncio.TimeoutError:
                raise cmd.BadArgument(
                    f"Query timed out. Type **{ctx.prefix}setup goodbye** to return."
                )

            await ms1.delete()
            chosen = chans[int(msg.content) - 1][1]
            if not chosen.permissions_for(ctx.guild.me).send_messages:
                raise cmd.BadArgument(
                    f"No send permissions. Type **{ctx.prefix}setup goodbye** to return."
                )
            await self.bot.db.hset(f"{ctx.guild.id}:set", "dptc", chosen.id)
            await ctx.send(f"Set the greet channel to {chosen.mention}!")
            await self.bot.db.hset(f"{ctx.guild.id}:setup", "goodbye", "0")

        ms2 = await ctx.send(
            "Choose a **goodbye message** (limit 140 chars):\nFormat tags: {user} {server} {user.mention}"
        )

        def check2(msg):
            return (
                msg.author == ctx.author
                and msg.guild == ctx.guild
                and msg.content[0:140]
            )

        try:
            msg = await self.bot.wait_for("message", check=check2, timeout=60.0)
        except asyncio.TimeoutError:
            raise cmd.BadArgument(
                f"Query timed out. Type **{ctx.prefix}setup goodbye** to return."
            )

        await ms2.delete()

        await self.bot.db.hset(f"{ctx.guild.id}:set", "dpt", msg.content[0:140])
        await self.bot.db.hset(f"{ctx.guild.id}:setup", "goodbye", "1")
        await self.bot.db.hset(f"{ctx.guild.id}:toggle", "goodbye", "1")
        embed = await self.bot.embed()
        embed.description = msg.content[0:140].format(user=ctx.author, server=ctx.guild)
        await ctx.send("Set the goodbye message:", embed=embed)

    @checks.is_mod()
    @setup.command(name="tt2", aliases=["tt"])
    async def setup_tt2(self, ctx, group: Optional[int] = 1):
        """Setup the TT2 module for raiding."""
        await ctx.send("You have initiated TT2 setup.")
        group = f"{ctx.guild.id}:tt:{group}"
        phase = await self.bot.db.hget(group, "ph")
        if not phase or phase is None:
            phase = await self.setup_tt2_key(ctx, group, "name", phase=1)
        else:
            phase = int(phase)
        if phase == 1:
            phase = await self.setup_tt2_key(ctx, group, "code", phase=2)
        if phase == 2:
            phase = await self.setup_tt2_key(ctx, group, "announce channel", phase=3)
        if phase == 3:
            phase = await self.setup_tt2_key(ctx, group, "gm role", phase=4)
        if phase == 4:
            phase = await self.setup_tt2_key(ctx, group, "master role", phase=5)
        if phase == 5:
            phase = await self.setup_tt2_key(ctx, group, "captain role", phase=6)
        if phase == 6:
            phase = await self.setup_tt2_key(ctx, group, "knight role", phase=7)
        if phase == 7:
            phase = await self.setup_tt2_key(ctx, group, "recruit role", phase=8)
        if phase == 8:
            phase = await self.setup_tt2_key(ctx, group, "raid tier", phase=9)
        if phase == 9:
            phase = await self.setup_tt2_key(ctx, group, "raid zone", phase=10)
        if phase == 10:
            phase = await self.setup_tt2_key(ctx, group, "raid queue size", phase=11)
        if phase == 11 and phase != 0:
            name = await self.bot.db.hget(group, "name")
            await ctx.send(f"Looks like **{name}** clan is fully setup!")


def setup(bot):
    """Bind the module to the bot."""
    bot.add_cog(SetupModule(bot))
