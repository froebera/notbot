import logging
import traceback
import discord
from discord.ext import commands
from .services import get_config_service
from .context import Context

extension_prefix = "notbot."
extensions = [
    "cogs.raid",
    "cogs.info",
    "cogs.admin",
    "cogs.efficiency"
    # "cogs.stats",
]

logger = logging.getLogger(__name__)


async def prefix_callable(bot, message) -> list:
    user_id = bot.user.id
    prefix_base = [f"<@!{user_id}> ", f"<@{user_id}> "]
    if message.guild is not None:
        prefix_base.append(bot.default_prefix)
    #     custom = await bot.db.hget(f"{message.guild.id}:set", "pfx")
    #     if custom or custom is not None:
    #         prefix_base.append(custom)
    #     pprefix_enabled = await bot.db.hget(f"{message.guild.id}:toggle", "pprefix")
    #     if pprefix_enabled is not None and pprefix_enabled != "0":
    #         pprefix = await bot.db.hget("pprefix", message.author.id)
    #         if pprefix is not None:
    #             prefix_base.append(pprefix)
    return prefix_base
    # return "?"


class NOTBOT(commands.AutoShardedBot):
    def __init__(self, ctx: Context):
        super().__init__(
            command_prefix=prefix_callable,
            description="",
            pm_help=None,
            fetch_offline_members=True,
        )
        self.context: Context = ctx
        self.context.set_bot(self)
        self.context.start()
        config_service = get_config_service(ctx)
        self.default_prefix = config_service.get_config("DEFAULT")["prefix"]
        # self.remove_command("help")
        for extension in extensions:
            e = extension_prefix + extension
            try:
                logger.info("Loading cog %s", e)
                self.load_extension(e)
            except (discord.ClientException, ModuleNotFoundError):
                logger.error("Failed to load cog %s", e)

    async def on_ready(self):
        logger.info("Ready: %s (ID: %s)", self.user, self.user.id)

    def run(self):
        config_service = get_config_service(self.context)
        token = config_service.get_config("DEFAULT")["token"]
        super().run(token, reconnect=True)

    async def on_command_error(self, ctx, error):
        """Hooks for discord.py command errors."""
        if isinstance(error, commands.CommandOnCooldown):
            cooldown = round(error.retry_after)
            await ctx.send(
                "Woah **{}**, please cool down. Try **{}{}** again in **{}**s.".format(
                    ctx.author, ctx.prefix, ctx.invoked_with, cooldown
                )
            )
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f":negative_squared_cross_mark: {error}")

        elif isinstance(error, commands.BadUnionArgument):
            await ctx.send(
                f":negative_squred_cross_mark: You didn't supply any valid items! {ctx.prefix}help {ctx.command.qualified_name}"
            )
        elif isinstance(error, commands.MissingPermissions):
            perms = ", ".join(error.missing_perms)
            await ctx.send(f":no_entry: {perms}.")

        elif isinstance(error, commands.BotMissingPermissions):
            perms = ", ".join([f"**{perm}**" for perm in error.missing_perms])
            await ctx.send(f":warning: I need permission to {perms} for this to work.")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f":negative_squared_cross_mark: {error}")

        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f":negative_squared_cross_mark: {error}")

        else:
            if ctx.command:
                logger.error(
                    "An unexpected exception occured while invoking %s", ctx.command
                )
            else:
                logger.error("An unexpected exception occured")

            logger.error(
                "".join(
                    traceback.format_exception(type(error), error, error.__traceback__)
                )
            )

            await ctx.send(
                f":negative_squared_cross_mark: Something went wrong ;( Please contact the bot author:\n {str(error)}"
            )

    @commands.check
    async def globally_block_bots(self, ctx):
        return not ctx.author.bot
