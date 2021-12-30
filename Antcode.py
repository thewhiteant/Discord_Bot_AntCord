import discord
from discord import message
from discord.ext import commands
from Basic import basic
from mid import mid
from Advance import adv
from message import message

client = commands.Bot(command_prefix="/", help_command=None,intents=discord.Intents.all())




basic(client)
mid(client)
adv(client)
message(client)

client.run("NzgwNDM4NzgyMjQyODQ4ODA5.X7vGQQ.KgrTdktPBEh3coSrmeotd9ooCjg")

