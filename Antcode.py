from os import cpu_count
import discord
from discord import message
from discord import user
from discord.ext import commands


client = commands.Bot(command_prefix="/")


msg_content = {
    "hello": "U Say Hello? Aloooha",
    "hi hhere": "Chiki Chiki "
}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        for i in msg_content:
            mess = message.content.lower()
            if mess == (i):
                await message.channel.send(msg_content[i])
    await client.process_commands(message)
@client.command()
async def test(ctx,*,msg):
        await ctx.send(msg)




@client.event
async def on_channel_update(x,y):
    print(x,y)


@client.event
async def on_member_update(x,y):
    print(x, y)


@client.event
async def on_server_role_update(x,y):
    print(x, y)


@client.event
async def on_voice_state_update(x,before, after):
    print(f"B: {before.channel}")
    print(f"A : {after.channel}")










client.run("NzgwNDM4NzgyMjQyODQ4ODA5.X7vGQQ.nQezCnXU_yyXIWjcuVi_yFk7vmo")
