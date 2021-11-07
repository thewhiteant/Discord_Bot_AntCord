from pythonping import ping as pongo
import discord
import random
import requests


def quoteCOl():
    data = requests.get("https://zenquotes.io/api/random")
    if data.status_code == 200:
        final = data.json()
        return final[0]['q'] + "-" + final[0]['a']



def basic(client):
    dpLi= []
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
                          await i.channel.purge(limit=2)
                   elif payload.emoji.name ==  "⬇":
                           embed = discord.Embed(title="Download", url=dic[index], color=random.choice(colorx))
                           await  i.remove_reaction(payload.emoji, payload.member)
                           await i.channel.send(embed=embed)



    @client.command()
    async def dp(ctx, user: discord.User):
         emoji = "❌"
         downEmji = "⬇"
         msg = await ctx.send(user.avatar_url)
         await msg.add_reaction(emoji)
         await msg.add_reaction(downEmji)
         dpLi.append(msg)
         url = "https://cdn.discordapp.com/avatars/780438782242848809/fc046136916301ce2d820d095378f511.webp?size=1024"
         url = url[0:-4] + "4096"
         dic.append(url)



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
         await ctx.send(f"> {quoteCOl()}")


