from os import name
from googlesearch import search
import  discord
import  random
import genshinstats as gsk
import asyncio
import os
from discord.utils import get
from gtts import gTTS 

gsk.set_cookie(ltuid=161804324, ltoken="V9R22r8dOIio7a6vquP5GbVkd3AjQ81G4hLDQvXH")


def adv(client):
      # to searcht



      @client.command()
      async def gs(ctx,query):

            if query is not None:

                  color = []
                  for clr in range(0x00000, 0xfffff):
                        color.append(clr)

                  url = f"https://www.google.com/search?q={query}"
                  embed = discord.Embed(title="Google Search Links", url=url , description=f"Search Results Links",color=random.choice(color))
                  embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
                  embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSR_BFrkWhROKKC1YzmlN3N33ZjiP-jym5IZ3fW-Hyf5vW9p94ltAeo0ZXyJdwT4rINWQY&usqp=CAU")
                  v = 0
                  for j in search(query, tld="com", num=10, stop=10):
                        v+=1
                        embed.add_field(name=f"{v}. Found ", value=j,inline=False)

                  await ctx.send(embed=embed)

            else:
                  await ctx.send("Search Key Req")

      #whiteant 831148294
      #gandu 806723089
      #nutcracker 815723573
      #demo 808118884

      @client.command()
      async def gen(ctx,uid):

            if uid == "ant":
                uid = 831148294
            elif uid == "mando":
                uid = 806723089
            elif uid == "nut":
                uid = 815723573
            elif uid == "demo":
                uid = 808118884

            try:
                  data = gsk.get_user_stats(uid)
                  stats = data["stats"]
                  characters = data["characters"]
                  achive = stats["achievements"]
                  actived = stats["active_days"]
                  chrcount = stats["characters"]
                  spiralab = stats["spiral_abyss"]
                  anim = stats["anemoculi"]
                  geo = stats["geoculi"]
                  elec = stats["electroculi"]

      
                  fivs  = []
                  for i in characters:
                        if i["rarity"] == 5:
                              fivs.append(i)

                  color = []
                  for clr in range(0x00000, 0xfffff):
                        color.append(clr)
                  embed = discord.Embed( title="Genshin Tracker", description="All Stats Genshin Imapact" , color=random.choice(color))
                  embed.set_author(name=f"User {uid}", icon_url=ctx.author.avatar_url)


                  embed.set_image(url="https://img.republicworld.com/republic-prod/stories/promolarge/xhdpi/3cw05gwejs5pf8ms_1603975477.jpeg?tr=w-1200,h-900")
                  embed.add_field(name="Active Days" , value=actived ,inline=False)
                  embed.add_field(name="Anemoculus", value=f"{anim}/65", inline=True)
                  embed.add_field(name="Geoculus", value=f"{geo}/160.", inline=True)
                  embed.add_field(name="Anemoculus", value=f"{elec}/181", inline=True)
                  embed.add_field(name="spiral abyss",value=spiralab, inline=False)
                  embed.add_field(name="Total Charecter ", value=chrcount, inline=True)
                  embed.add_field(name="achievement", value=actived, inline=True)
                  for i in fivs:
                        embed.add_field(name= i["name"] , value=f"Level: {i['level']}", inline=False)
                  await ctx.send(embed=embed)
                  
            except:

                await ctx.send("**Your Data Is Private Make It Public** https://gamewith.net/genshin-impact/article/show/23967")

      @client.command()
      async def tgs(ctx, *, text: str):
            await ctx.purge(limit=1)
            await ctx.send(text,tts=True)
            
