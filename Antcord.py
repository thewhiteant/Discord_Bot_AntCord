import discord
from discord import message
from discord import channel
from discord.ext import commands
from gtts import tts
from Basic import basic
from mid import mid
from Advance import adv
from message import message
from discord.utils import get
import random
import asyncio
import os
from gtts import gTTS
import asyncio

client = commands.Bot(command_prefix="/", help_command=None,intents=discord.Intents.all())

dpLi = []
dic = []

@client.event
async def on_raw_reaction_add(payload):
    colorx = []
    for clr in range(0x00000, 0xfffff):
        colorx.append(clr)
    if payload.member == client.user:
        return
    else:
        for i in dpLi:
           index = dpLi.index(i)
           if payload.emoji.name == "❌":
                await i.channel.purge(limit=1)
        #    elif payload.emoji.name == "⬇":
        #         embed = discord.Embed(title="Download", url=dic[index], color=random.choice(colorx))
        #         await i.remove_reaction(payload.emoji, payload.member)
        #    await i.channel.send(embed=embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("> **Command Not Found Type: ** '/help'")


@client.event
async def on_voice_state_update(member, before, after):

        if after.channel is not None:
            if member != client.user:
        
                global gTTS
                speech = gTTS(text=f"Welcome {member.name}", lang="en-us", slow=False)
                speech.save("wlcome.mp3")

                await asyncio.sleep(2)
                voice = get(client.voice_clients, guild=member.guild)
                if not voice:
                    voice = await member.voice.channel.connect()
                voice.play(discord.FFmpegPCMAudio('wlcome.mp3'), after=None)
                voice.is_playing()
                await asyncio.sleep(4)
                os.remove("wlcome.mp3")
                await voice.disconnect()




basic(client)
mid(client)
adv(client)
message(client)

client.run("NzgwNDM4NzgyMjQyODQ4ODA5.X7vGQQ.KgrTdktPBEh3coSrmeotd9ooCjg")

