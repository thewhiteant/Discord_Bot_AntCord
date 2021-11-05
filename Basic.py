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



def full(client):



        #Manga Source Command

        @client.command()
        async def nme(ctx, *, data):
            try:
                url = f"https://mangatx.com/?s={data}&post_type=wp-manga"
                getD = requests.get(url).text
                data = soup(getD, "lxml")
                all_Data = data.find_all("div", class_="row c-tabs-item__content")[0]
                link = all_Data.find("h3", class_="h4").a["href"]
                name = all_Data.find("h3", class_="h4").text
                thumb = all_Data.find("img")['data-src']
                genres = all_Data.find_all("div", class_="summary-content")[-2].text
                lch = all_Data.find("span", class_="font-meta chapter").text

                color = []

                for clr in range(0x00000, 0xfffff):
                    color.append(clr)

                embed = discord.Embed(title=name, color=random.choice(color))
                embed.set_image(url=thumb)
                embed.add_field(name="Genre", value=genres, inline=True)
                embed.add_field(name="Latest Chapter", value=lch, inline=False)
                embed.set_footer(text="©ZoroSama")
                await ctx.send(embed=embed)
            except:

                await ctx.send("Data Not Found / An Error Occurs")












#later

 # msg_content = {
        #     "hello": "U Say Hello? Aloooha",
        #     "hi hhere": "Chiki Chiki "
        # }

        # @client.event
        # async def on_message(message):
        #     if message.author == client.user:
        #         return
        #     else:
        #         for i in msg_content:
        #             mess = message.content.lower()
        #             if mess == (i):
        #                 await message.channel.send(msg_content[i])
        #     await client.process_commands(message)
        # @client.command()
        # async def test(ctx,*,msg):
        #         await ctx.send(msg)

        # @client.event
        # async def on_channel_update(x,y):
        #     print(x,y)

        # @client.event
        # async def on_member_update(x,y):
        #     print(x, y)

        # @client.event
        # async def on_server_role_update(x,y):
        #     print(x, y)

        # @client.event
        # async def on_voice_state_update(x,before, after):
        #     print(f"B: {before.channel}")
        #     print(f"A : {after.channel}")
        # #Webscrape data

