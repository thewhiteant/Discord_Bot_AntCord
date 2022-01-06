from pythonping import ping as pongo
import discord
import random
import requests
from discord.ext import commands





def quoteCOl():
    data = requests.get("https://zenquotes.io/api/random")
    if data.status_code == 200:
        final = data.json()
        return final[0]['q'] + " --" + final[0]['a']



def basic(client):




    @client.command()
    async def ping(ctx):
        ranchs = ["https://www.speedtest.net/","https://fast.com/","http://speedtest.googlefiber.net/","http://www.speedtest.com.sg/","https://www.highspeedinternet.com/tools/speed-test"]

        ping = round(client.latency*1000)
        googleres = int(pongo("google.com", size=32,count=1).rtt_avg_ms)
        faceres = int(pongo("facebook.com", size=32,count=1).rtt_avg_ms)
        ytres = int(pongo("youtube.com", size=32, count=1).rtt_avg_ms)
        twires = int(pongo("twitter.com", size=32, count=1).rtt_avg_ms)
        vlin1 = int(pongo("157.240.7.35", size=32, count=1).rtt_avg_ms)
        vlin2 = int(pongo("157.240.7.35", size=32, count=1).rtt_avg_ms)

        colorx = []
        for clr in range(0x00000, 0xfffff):
            colorx.append(clr)

        embed = discord.Embed(title=f"Ping: {ping} ms", description="Top Sites Ping's", color=random.choice(colorx))
        embed.set_author(name=ctx.author.name,url=random.choice(ranchs), icon_url=ctx.author.avatar_url)
        embed.add_field(name="Google", value=googleres, inline=True)
        embed.add_field(name="Facebook", value=faceres, inline=True)
        embed.add_field(name="Youtube", value=ytres, inline=True)
        embed.add_field(name="Twitter", value=twires, inline=True)
        embed.add_field(name="Valorant In_1", value=vlin1, inline=True)
        embed.add_field(name="Valorant In_2", value=vlin2, inline=True)
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.send(embed=embed)


    @client.command()
    async def quote(ctx):
         await ctx.send(f"> **{quoteCOl()}**")


    # @client.command()
    # async def rl(ctx):
    #     role = discord.utils.get(ctx.guild.roles, name="Ntx")
    #     await ctx.author.add_roles(role)

    # @client.command()
    # async def rel(ctx):
    #     role = discord.utils.get(ctx.guild.roles, name="Memeber")
    #     await ctx.author.remove_roles(role)

    @client.command()  # Invite to your dm
    async def invite(ctx):

        inv = await ctx.channel.create_invite(max_age='200')
        await ctx.author.send(inv)
        embed = discord.Embed(title=ctx.author.name, description="Invite Already Sent To Your DM 😉 \n `If Dm are not available, Click Team Jucy on top of this`", color=0x01d9f1)
        embed.set_author(name="Team JUCY", url=inv, icon_url="https://cdn.discordapp.com/splashes/557864258617081858/053c45339b4d85c9cca13ffdc151d720.jpg?size=2048")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.send(embed=embed)


    @client.command()
    async def dm(ctx, user: discord.User, *, msg):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Private DM Sent To {user.name}....")
        await user.send(msg)





