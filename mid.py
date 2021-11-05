import discord
from bs4 import BeautifulSoup as soup
import requests
import random



def mid(client):


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





