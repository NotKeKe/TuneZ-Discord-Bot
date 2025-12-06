from discord import Interaction, SelectOption, Message, errors, File
from discord.ui import View, button, select, Button
import traceback
import io
from typing import Optional

from .player import Player
from .utils import send_info_embed
from .utils import players

from core.utils import get_bot, get_member
from core.translator import get_translate


class MusicControlButtons(View):
    def __init__(self, player: Player, timeout = 180):
        super().__init__(timeout=timeout)
        self.player = player
        self.translator = player.translator
        self.locale = player.locale

    async def button_error(self, inter: Interaction, exception):
        if isinstance(exception, errors.Forbidden):
            bot = get_bot()
            u = bot.get_user(inter.user.id) or await bot.fetch_user(inter.user.id)
            await u.send("I'm missing some permissions:((")
        traceback.print_exc()
    
    @button(label='上一首歌', emoji='⏮️')
    async def previous_callback(self, interaction: Interaction, button: Button):
        try:
            await self.player.back()
            await send_info_embed(self.player, interaction)
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='暫停/繼續', emoji='⏯️')
    async def pause_resume_callback(self, interaction: Interaction, button: Button):
        try:
            if self.player.paused:
                await self.player.resume()
            else:
                await self.player.pause()
            r = await send_info_embed(self.player, interaction, if_send=False)
            if r is None: return
            embed, view = r
            await interaction.response.edit_message(embed=embed, view=view)
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='下一首歌', emoji='⏭️')
    async def next_callback(self, interaction: Interaction, button: Button):
        try:
            await self.player.skip()
            await send_info_embed(self.player, interaction)
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='停止播放', emoji='⏹️')
    async def stop_callback(self, interaction: Interaction, button: Button):
        try:
            if not interaction.guild: return
            member = await get_member(interaction)
            if not member: return
            
            if not member.voice: return await interaction.response.send_message(await get_translate('send_button_not_in_voice', interaction, self.locale))
            if not interaction.guild.voice_client: return await interaction.response.send_message(await get_translate('send_button_bot_not_in_voice', interaction, self.locale))

            player: Optional[Player] = players.get(interaction.guild.id)
            user = interaction.user.global_name

            if not player: return await interaction.response.send_message(await get_translate('send_button_player_crashed', interaction, self.locale))
            del players[interaction.guild.id]

            await interaction.guild.voice_client.disconnect() # type: ignore
            await interaction.response.send_message((await get_translate('send_button_stopped_music', interaction, self.locale)).format(user=user, channel_mention=player.ctx.channel.mention), ephemeral=True) # type: ignore ????, 類型檢查跟我說 ctx 會是 None?
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='循環', emoji='🔁')
    async def loop_callback(self, interaction: Interaction, button: Button):
        try:
            msg = interaction.message
            self.player.turn_loop()
            r = await send_info_embed(self.player, interaction, if_send=False)
            if r is None: return
            eb, view = r
            if msg:
                await msg.edit(embed=eb, view=view)
                
            new_msg = await interaction.response.send_message((await get_translate('send_button_loop_changed', interaction, self.locale)).format(loop_status=self.player.loop_status), ephemeral=True)
            if new_msg.resource:
                await new_msg.resource.delete(delay=30) # type: ignore
        except Exception as e:
            await self.button_error(interaction, e)
    
    @button(label='列表', emoji='📄')
    async def queue_callback(self, interaction: Interaction, button: Button):
        try:
            eb = await self.player.show_list()
            await interaction.response.send_message(embed=eb, ephemeral=True)
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='刷新', emoji='🔄')
    async def refresh_callback(self, interaction: Interaction, button: Button):
        try:
            r = await send_info_embed(self.player, interaction, if_send=False)
            if r is None: return
            eb, view = r
            await interaction.response.edit_message(embed=eb, view=view)
        except Exception as e:
            await self.button_error(interaction, e)

    @button(label='歌詞搜尋', emoji='🔍')
    async def search_callback(self, interation: Interaction, button: Button):
        try:
            await interation.response.defer(ephemeral=True, thinking=True)
            result = await self.player.search_lyrics()

            if len(result) > 2000:
                file = File(io.BytesIO(result.encode()), filename='lyrics.txt')
                result = result[:1996] + '...'
            else:
                file = None

            await interation.followup.send(result, **({'file': file} if file else {}), ephemeral=True) # type: ignore
        except Exception as e:
            await self.button_error(interation, e)

    @button(label='音量調整', emoji='🔊')
    async def volume_callback(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.send_message(view=VolumeControlButtons(self.player), ephemeral=True)
        except Exception as e:
            await self.button_error(interaction, e)

class VolumeControlButtons(View):
    def __init__(self, player: Player, timeout = 180):
        super().__init__(timeout=timeout)
        self.player = player

    @button(label='音量-50%', emoji='⏬')
    async def volume_down_50(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.defer()
            await self.player.volume_adjust(reduce=0.5)
        except Exception as e:
            traceback.print_exc()

    @button(label='音量-10%', emoji='➖')
    async def volume_down_10(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.defer()
            await self.player.volume_adjust(reduce=0.1)
        except Exception as e:
            traceback.print_exc()

    @button(label='正常音量', emoji='🔊')
    async def volume_normal(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.defer()
            await self.player.volume_adjust(volume=1.0)
        except Exception as e:
            traceback.print_exc()

    @button(label='音量+10%', emoji='➕')
    async def volume_up_10(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.defer()
            await self.player.volume_adjust(add=0.1)
        except Exception as e:
            traceback.print_exc()

    @button(label='音量+50%', emoji='🔼')
    async def volume_up_50(self, interaction: Interaction, button: Button):
        try:
            await interaction.response.defer()
            await self.player.volume_adjust(add=0.5)
        except Exception as e:
            traceback.print_exc()
