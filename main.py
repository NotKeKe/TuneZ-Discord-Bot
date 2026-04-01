import discord
from discord.ext import commands
import asyncio
import os
import logging
from pathlib import Path

from core.config import ENV_PATH, resource_path
from core.utils import set_bot
from core.translator import i18n
from core.emojis import create_emojis

logger = logging.getLogger(__name__)

async def setup_bot():
    global bot
    logger.info('Starting bot...')

    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True
    intents.members = True
    intents.presences = True
    intents.voice_states = True

    bot = commands.Bot('$', intents=intents)
    set_bot(bot) # 用於之後 import bot

    bot.help_command = None

    # 設定 events
    @bot.event
    async def setup_hook():
        try:
            translator = i18n()
            await bot.tree.set_translator(translator)
            synced_bot = await bot.tree.sync()
            logger.info(f'Synced {len(synced_bot)} commands.')
        except:
            logger.error('Error while syncing commands.', exc_info=True)

    @bot.event
    async def on_ready():
        if not bot.user:
            logger.warning('Bot is not logged in.')
            return
        logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
        await create_emojis(bot)

    @bot.event
    async def on_connect(): ...

    @bot.event
    async def on_disconnect(): ...


# load commands
async def load():
    for filename in Path(resource_path('cmds')).iterdir():
        try:
            if filename.suffix == '.py':
                logger.info('Loading command: ' + filename.stem)
                await bot.load_extension(f'cmds.{filename.stem}')
        except commands.errors.NoEntryPointError:
            logger.warning(f'Failed to load command: {filename.stem}, no entry point found.')
        except:
            logger.error('Error while loading command: ' + filename.stem, exc_info=True)

async def main():
    try:
        await setup_bot()
        async with bot:
            await load()
            bot_token = os.getenv('DISCORD_TOKEN')

            bot_set = False
            try:
                await bot.start(bot_token) # type: ignore
                bot_set = True
            except discord.errors.LoginFailure:
                pass

            if not bot_set:
                logger.error(f'DISCORD_TOKEN is not set or is invalid. Please set it in `{str(ENV_PATH)}`.')
                exit()
            
    except (KeyboardInterrupt, asyncio.CancelledError): pass
    finally:
        logger.info('Bot is shutting down.')
        from core.utils import close_event
        await close_event()

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass