from pythonping import ping as pongo
import discord
import random
import requests





def quoteCOl():
    data = requests.get("https://zenquotes.io/api/random")
    if data.status_code == 200:
        final = data.json()
        return final[0]['q'] + " --" + final[0]['a']



def basic(client):
    @client.event
    async def on_member_join(member):
        await member.send("Test")

    @client.event
    async def on_member_remove(member):
        print("someone leave")

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
         await ctx.send(f"> **{quoteCOl()}**")

    #
    # @client.command()
    # async def rl(ctx):
    #     role = discord.utils.get(ctx.guild.roles, name="Ntx")
    #     await ctx.author.add_roles(role)

    @client.command()
    async def rel(ctx):
        role = discord.utils.get(ctx.guild.roles, name="Memeber")
        await ctx.author.remove_roles(role)


    @client.event
    async def on_voice_state_update(member, before, after):
        pass
    
    @client.command(pass_context=True)
    async def pvt(ctx, *, msg):
        print(f"{ctx.author.name} sent {msg}  Time: {x}")
        await ctx.channel.purge(limit=1)
        await ctx.send(msg)


    @client.command()  # Invite to your dm
    async def invite(ctx):

        inv = await ctx.channel.create_invite(max_age='300')
        await ctx.author.send(inv)
        embed = discord.Embed(title=ctx.author.name, description="Invite Already Sent To Your DM 😉 \n `If Dm are not available, Click Team Jucy on top of this`", color=0x01d9f1)
        embed.set_author(name="Team JUCY", url=inv, icon_url="https://cdn.discordapp.com/splashes/557864258617081858/053c45339b4d85c9cca13ffdc151d720.jpg?size=2048")
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_footer(text="Copyright \u00a9 White-Ant")
        await ctx.send(embed=embed)



    @client.command()
    async def delt(ctx, rang):
        rang = int(rang)
        await ctx.channel.purge(limit=rang)


    @client.command()
    async def dm(ctx, user: discord.User, *, msg):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Private DM Sent To {user.name}....")
        await user.send(msg)


    

    







