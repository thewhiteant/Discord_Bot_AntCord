from os import cpu_count
import discord
from discord import message
from discord import user
from discord.ext import commands
from bs4 import BeautifulSoup as soup
import requests
import lxml
import random
import json

from Basic import basic
from mid import mid
from Advance import adv


client = commands.Bot(command_prefix="/", help_command=None,intents=discord.Intents.all())






@client.event
async def on_message(message):
     if message.author == client.user:
        return
     else:
         pass
     await  client.process_commands(message)


basic(client)
mid(client)
adv(client)


client.run("NzgwNDM4NzgyMjQyODQ4ODA5.X7vGQQ.nQezCnXU_yyXIWjcuVi_yFk7vmo")
