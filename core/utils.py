from discord.ext import commands
from discord import Member, Color, Embed, Interaction
from typing import Optional
from datetime import datetime, timedelta, timezone
from fakeredis.aioredis import FakeRedis

bot: Optional[commands.Bot] = None

redis_client = FakeRedis(decode_responses=True)

def set_bot(b: commands.Bot):
    global bot
    bot = b

def get_bot() -> commands.Bot:
    if not bot:
        raise ValueError('bot is not set.')
    return bot

async def get_member(ctx: commands.Context | Interaction) -> Optional[Member]:
    _id = ctx.author.id if isinstance(ctx, commands.Context) else ctx.user.id
    member = ctx.guild.get_member(_id) or await ctx.guild.fetch_member(_id) if ctx.guild else None
    return member

def create_basic_embed(
        title: Optional[str] = None, 
        description: Optional[str] = None, 
        color = Color.blue(), 
        功能: Optional[str] = None, 
        time: bool = True
    ) -> Embed:
    '''
    會設定discord.Embed(title, description, color, timestamp)
        embed.set_author(功能, embed_default_link)
    功能會跑去author
    '''

    embed = Embed(title=title if title is not None else None, description=description, color=color, timestamp=datetime.now() if time else None)
    if 功能 is not None: embed.set_author(name=功能)
    return embed

def secondToReadable(seconds):
    '''將傳入的秒數轉換為01:01:01的形式'''
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    if hours > 0:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    elif minutes > 0:
        return f"00:{minutes:02d}:{seconds:02d}"
    else:
        return f"00:{seconds:02d}"
    
def math_round(x: float, ndigits: int = 0) -> float:
    factor = 10 ** ndigits
    if x >= 0: return int(x * factor + 0.5) / factor
    else: return int(x * factor - 0.5) / factor

def current_time(UTC: int = 8) -> str:
    '''回傳現在時間(str)，arg: UTC: 使用者所提供的時區'''
    time = datetime.now(timezone(timedelta(hours=UTC)))
    return time.strftime('%Y/%m/%d %H:%M:%S %A')