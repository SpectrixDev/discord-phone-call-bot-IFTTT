import logging
import discord
from discord.ext import commands
from bot.config import load_config, ConfigError

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

def create_bot():
    try:
        config = load_config()
    except ConfigError as e:
        logging.error(f"Configuration error: {e}")
        raise SystemExit(1)

    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or(config["prefix"]),
        case_insensitive=True,
        intents=intents
    )
    bot.config = config

    @bot.event
    async def on_ready():
        logging.info("=========")
        logging.info("Ready for use!")
        logging.info("Bot created by https://github.com/SpectrixDev")
        logging.info("=========")

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"**:no_entry: {error}**")
        else:
            logging.error(f"Unhandled command error: {error}")

    # Load all cogs from bot/cogs/
    import os
    import glob

    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for cog_file in glob.glob(os.path.join(cogs_dir, "*.py")):
        if not cog_file.endswith("__init__.py"):
            cog_name = f"bot.cogs.{os.path.splitext(os.path.basename(cog_file))[0]}"
            try:
                bot.load_extension(cog_name)
                logging.info(f"Loaded cog: {cog_name}")
            except Exception as e:
                logging.error(f"Failed to load cog {cog_name}: {e}")

    return bot

def run():
    setup_logging()
    bot = create_bot()
    bot.run(bot.config["discordToken"])
