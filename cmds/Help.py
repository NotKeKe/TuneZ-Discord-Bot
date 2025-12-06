from discord.ext import commands
import logging

from core.translator import locale_str

logger = logging.getLogger(__name__)

class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_load(self):
        logger.info(f'Loaded "{__name__}"')

    @commands.hybrid_command(name=locale_str('help'), description=locale_str('help'))
    async def help(self, ctx: commands.Context):
        await ctx.send('Under development...')

async def setup(bot):
    await bot.add_cog(Help(bot))