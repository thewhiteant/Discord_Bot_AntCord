import readchar
import discord
from bs4 import BeautifulSoup as soup
import requests
import random
from discord.ext import commands
from mal import AnimeSearch, Anime



import os
# load our local env so we dont have the token in public
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import ffmpeg


#pip install PyNaCl

def mid(client):


        #Manga Source Command

        @client.command()
        async def mangatx(ctx, *, data):
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
                embed.set_footer(text="Copyright \u00a9 White-Ant")
                await ctx.send(embed=embed)
            except:

                await ctx.send("Data Not Found / An Error Occurs")

        @client.command()
        async def anime(ctx, *, data):
         
                    search = AnimeSearch(data)
                    malid = search.results[0].mal_id
                    anime = Anime(malid)
                    title = anime.title.strip(' \n\t ')
                    title_japanese = anime.title_japanese.strip(' \n\t ')
                    title_synonyms = anime.title_synonyms
                    url = anime.url
                    image_url = anime.image_url
                    types = anime.type
                    status = anime.status.strip(' \n\t ')
                    genres = anime.genres
                    themes = anime.themes
                    score = anime.score
                    rank = anime.rank
                    popularity = anime.popularity
                    episodes = anime.episodes
                    aired = anime.aired.strip(' \n\t ')
                    rating = anime.rating.strip(' \n\t ')
                    characters = anime.characters


                    color = []

                    for clr in range(0x00000, 0xfffff):
                        color.append(clr)

                    embed = discord.Embed(title=title, url=url, description=f"Japanese Name : {title_japanese} \nSynonyms : {title_synonyms} ", color=random.choice(color))
                    embed.set_image(url=image_url)
                    embed.add_field(name="Types", value=types, inline=True)
                    embed.add_field(name="Genre", value=genres, inline=True)
                    embed.add_field(name="Episodes", value= episodes , inline=True)
                    embed.add_field(name="Rating", value=rating, inline=True)
                    embed.add_field(name="Rank",value=rank, inline=True)
                    embed.add_field(name="Score", value=score, inline=True)
                    embed.add_field(name="Status", value=status, inline=True)
                    embed.add_field(name="First Aired", value=aired, inline=True)
                    embed.add_field(name="Popularity", value=popularity, inline=True)
                    embed.add_field(name="Theme", value=themes, inline=True)
                    y = 0
                    for i in characters:
                        y += 1
                        iname = i.name.strip(' \n\t ')
                        vac = i.voice_actor.strip(' \n\t ')
                        role = i.role.strip(' \n\t ')
                    #     print(iname)
                    #     print(vac)
                    #     print(role)





                    # print(title)
                    # print(title_japanese)
                    # print(title_synonyms)
                    # print(url)
                    # print(types)
                    # print(rating)
                    # print(aired)
                    # print(episodes)
                    # print(popularity)
                    # print(rank)
                    # print(score)
                    # print(genres)
                    # print(status)
                    # print(themes)

                        embed.add_field(name=f"Charecter {y}", value=iname, inline=True)
                    embed.set_footer(text="Copyright \u00a9 White-Ant")
                    await ctx.send(embed=embed)
                       





        # command to play sound from a youtube URL
        @client.command()
        async def play(ctx,*,url):

            channel = ctx.message.author.voice.channel
            voice = get(client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected():
                await voice.move_to(channel)
            else:
                voice = await channel.connect()

            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            voice = get(client.voice_clients, guild=ctx.guild)



            with YoutubeDL(YDL_OPTIONS) as ydl:
                if url[0:4] == "https":
                    info = ydl.extract_info(url, download=False)
                else:
        
                  info = ydl.extract_info(f"ytsearch:{url}", download=False)['entries'][0]
            URL = info['url']
            voice.play(FFmpegPCMAudio(URL,executable="ffmpeg.exe", **FFMPEG_OPTIONS))
            # voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="test.mp3"))
            voice.is_playing()
            await ctx.send('Bot is playing')




        # command to resume voice if it is paused
        @client.command()
        async def resume(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)

            if not voice.is_playing():
                voice.resume()
                await ctx.send('Bot is resuming')


        # command to pause voice if it is playing
        @client.command()
        async def pause(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)

            if voice.is_playing():
                voice.pause()
                await ctx.send('Bot has been paused')


        # command to stop voice
        @client.command()
        async def stop(ctx):
            voice = get(client.voice_clients, guild=ctx.guild)

            if voice.is_playing():
                voice.stop()
                await ctx.send('Stopping...')




