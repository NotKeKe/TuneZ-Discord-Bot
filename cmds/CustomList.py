import discord
from discord import app_commands
from discord.ext import commands
import logging

from cmds.music_bot.autocomplete import *
from cmds.music_bot.play_list import CustomListPlayer, add_to_custom_list, get_custom_list, del_custom_list, remove_one_from_custom_list
from cmds.music_bot.utils import send_info_embed, players, custom_list_players

from core.translator import locale_str, get_translate, load_translated
from core.utils import create_basic_embed

logger = logging.getLogger(__name__)

class CustomList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name=locale_str('play_custom_list'), description=locale_str('play_custom_list'))
    @app_commands.autocomplete(list_name=custom_play_list_autocomplete)
    async def play_custom_list(self, ctx: commands.Context, list_name: str):
        if not ctx.guild: return
        async with ctx.typing():
            member = ctx.guild.get_member(ctx.author.id) or await ctx.guild.fetch_member(ctx.author.id) if ctx.guild else None
            if not member:
                return await ctx.send(await get_translate('send_play_not_in_guild', ctx))

            if not member.voice: return await ctx.send(await get_translate('send_play_not_in_voice', ctx))
            if players.get(ctx.guild.id): # 不讓使用者同時播放兩個 list，或是自訂歌曲 + 自訂歌單
                return await ctx.send(await get_translate('send_play_custom_list_already_playing_left_first', ctx))
            if not ctx.voice_client and member.voice.channel:
                await member.voice.channel.connect()

            if ctx.voice_client.is_paused(): return await ctx.invoke(self.bot.get_command('resume')) # type: ignore
            if players.get(ctx.guild.id): return # 如果 player 已經存在，則不再建立
            
            # 取得 player
            custom_list_player = CustomListPlayer(ctx, list_name)
            player = await custom_list_player.run()
            players[ctx.guild.id] = player
            custom_list_players[ctx.guild.id] = custom_list_player

            # 播放
            await player.play()
            await send_info_embed(player, ctx)
            
    @commands.hybrid_command(name=locale_str('add_custom_list'), description=locale_str('add_custom_list'))
    @app_commands.autocomplete(list_name=custom_play_list_autocomplete)
    @app_commands.describe(list_name=locale_str('add_custom_list_list_name'))
    async def add_custom_list(self, ctx: commands.Context, url: str, list_name: str):
        async with ctx.typing():
            result = await add_to_custom_list(url, list_name, ctx.author.id)
            await ctx.send(result if result is not True else (await get_translate('send_add_to_custom_list_success', ctx)).format(list_name=list_name)) # type: ignore

    @commands.hybrid_command(name=locale_str('show_custom_list'), description=locale_str('show_custom_list'))
    @app_commands.autocomplete(list_name=custom_play_list_autocomplete)
    async def show_custom_list(self, ctx: commands.Context, list_name: str):
        async with ctx.typing():
            result = await get_custom_list(list_name, ctx.author.id)
            description = '\n'.join(f'{i+1}. [{song[0]}]({song[1]})' for i, song in enumerate(result))
            eb = create_basic_embed(description=description)
            await ctx.send(embed=eb)

    @commands.hybrid_command(name=locale_str('delete_custom_list'), description=locale_str('delete_custom_list'), aliases=['del_custom_list'])
    @app_commands.autocomplete(list_name=custom_play_list_autocomplete)
    async def delete_custom_list(self, ctx: commands.Context, list_name: str):
        async with ctx.typing():
            view = discord.ui.View(timeout=60)
            button_check = discord.ui.Button(emoji='✅', label='Yes', style=discord.ButtonStyle.green)
            async def button_check_callback(interaction: discord.Interaction):
                button_reject.disabled = True
                button_check.disabled = True

                await del_custom_list(list_name, interaction.user.id)

                await interaction.response.edit_message(content=await interaction.translate('send_delete_custom_list_success'), embed=None, view=None)
            button_check.callback = button_check_callback

            button_reject = discord.ui.Button(emoji='❌', label='No', style=discord.ButtonStyle.red)
            async def button_reject_callback(interaction: discord.Interaction):
                button_reject.disabled = True
                button_check.disabled = True
                await interaction.response.edit_message(content=await interaction.translate('send_delete_custom_list_cancelled'), embed=None, view=None)
            button_reject.callback = button_reject_callback

            view.add_item(button_check)
            view.add_item(button_reject)

            '''i18n'''
            eb = load_translated((await get_translate('embed_clear_confirm', ctx)))[0]
            title = eb.get('title')
            ''''''

            eb = create_basic_embed(title, color=ctx.author.color)
            eb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=eb, view=view)

    @commands.hybrid_command(name=locale_str('remove_one_from_custom_list'), description=locale_str('remove_one_from_custom_list'), aliases=['rm_one_custom_list'])
    @app_commands.autocomplete(list_name=custom_play_list_autocomplete)
    @app_commands.describe(index=locale_str('remove_one_from_custom_list_index'))
    async def remove_one_from_custom_list(self, ctx: commands.Context, list_name: str, index: int):
        """Remove one song from custom list forever"""
        async with ctx.typing():
            # 建立 async generator
            gen = remove_one_from_custom_list(list_name, index, ctx.author.id)

            # 第一次 anext：取得歌曲資訊
            song_info = await anext(gen)

            if isinstance(song_info, str):
                # 錯誤或空清單
                await ctx.send(song_info)
                await gen.aclose()
                return

            # song_info is dict at this point
            song_title = song_info.get('title') or song_info.get('video_url')  # type: ignore[union-attr]

            view = discord.ui.View(timeout=60)

            async def cleanup():
                """清理 generator，釋放 db 連線"""
                try:
                    await gen.aclose()
                except:
                    pass

            button_check = discord.ui.Button(emoji='✅', label='Yes', style=discord.ButtonStyle.green)
            async def button_check_callback(interaction: discord.Interaction):
                button_reject.disabled = True
                button_check.disabled = True

                try:
                    await anext(gen)  # 第二次 anext：執行刪除
                except StopAsyncIteration:
                    pass

                await interaction.response.edit_message(
                    content=(await get_translate('send_remove_one_from_custom_list_success', interaction)).format(
                        list_name=list_name,
                        title=song_title
                    ),
                    embed=None,
                    view=None
                )
                await cleanup()

            button_check.callback = button_check_callback

            button_reject = discord.ui.Button(emoji='❌', label='No', style=discord.ButtonStyle.red)
            async def button_reject_callback(interaction: discord.Interaction):
                button_reject.disabled = True
                button_check.disabled = True
                await interaction.response.edit_message(
                    content=await get_translate('send_clear_cancelled', interaction),
                    embed=None,
                    view=None
                )
                await cleanup()

            button_reject.callback = button_reject_callback

            view.add_item(button_check)
            view.add_item(button_reject)

            '''i18n'''
            eb = load_translated((await get_translate('embed_remove_one_confirm', ctx)))[0]
            title = eb.get('title').format(
                title=song_title,
                list_name=list_name
            )
            ''''''

            eb = create_basic_embed(title, color=ctx.author.color)
            eb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
            await ctx.send(embed=eb, view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(CustomList(bot))
