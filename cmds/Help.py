from discord.ext import commands
import logging
from typing import Literal

from core.translator import locale_str, get_translate, load_translated
from core.emojis import get_emoji, update_custom_emojis, update_default_emojis
from core.config import OWNER_ID
from core.utils import create_basic_embed

logger = logging.getLogger(__name__)

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        logger.info(f'Loaded "{__name__}"')

    @commands.hybrid_command(name=locale_str('help'), description=locale_str('help'))
    async def help(self, ctx: commands.Context):
        '''i18n'''
        eb_str = await get_translate('embed_help', ctx)
        eb_dict: dict[str, str] = load_translated(eb_str)[0]
        author: str = eb_dict.get('author', '')
        description: str = eb_dict.get('description', '')
        ''''''

        eb = create_basic_embed(description=description, 功能=author)
        await ctx.send(embed=eb)

    @commands.hybrid_command(name=locale_str('emoji'), description=locale_str('emoji'))
    async def emoji(self, ctx: commands.Context, name: str):
        emoji = get_emoji(name)
        if not emoji:
            return await ctx.send('Emoji not found!')
        await ctx.send(f'{emoji}\nID: {emoji.id}\nName: {emoji.name}')

    @commands.hybrid_command(name=locale_str('reload_emojis'), description=locale_str('reload_emojis'))
    async def reload_emojis(self, ctx: commands.Context, type: Literal['all', 'default', 'custom'] = 'all'):
        if ctx.author.id != OWNER_ID: return
        
        async with ctx.typing():
            if type == 'all':
                await update_default_emojis(self.bot)
                await update_custom_emojis(self.bot)
            elif type == 'default':
                await update_default_emojis(self.bot)
            elif type == 'custom':
                await update_custom_emojis(self.bot)

            await ctx.send('Emojis reloaded!')

async def setup(bot):
    await bot.add_cog(Help(bot))