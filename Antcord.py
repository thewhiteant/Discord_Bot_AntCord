from aiohttp.helpers import NO_EXTENSIONS
import discord
from discord import user
from discord.ext import commands, tasks
from discord.flags import BaseFlags
from discord.utils import get
import random
import asyncio
import os
from gtts import gTTS
import asyncio
from pythonping import ping as pongo
from mutagen.mp3 import MP3
from mal import AnimeSearch, Anime
from bs4 import BeautifulSoup as soup
import sys
import re
import genshinstats as gsk
from googlesearch import search
from tinydb import TinyDB , Query
import requests
from datetime import date, datetime


gsk.set_cookie(ltuid=161804324, ltoken="V9R22r8dOIio7a6vquP5GbVkd3AjQ81G4hLDQvXH")


client = commands.Bot(command_prefix="x.", help_command=None,intents=discord.Intents.all())

timegg = datetime.now()



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("> **Command Not Found Type: ** 'x.help'")

#voice Welcome

va = []
@client.event
async def on_voice_state_update(member, before, after):   
        if (after.channel is not None) and (before.channel is None):
            if member != client.user:
                if member.name not in ["JucyT", "Rythm", "MEE6", "Pancake", "Hydra", "VoiceMaster", "Carl-bot"]:
                    if member.guild.name == "Team JUCY":
                        global gTTS
                        speech = gTTS(text=f"Welcome {member.name}", lang="en-us", slow=False)
                        speech.save("wlcome.mp3")
                        await asyncio.sleep(2)
                        voice = get(client.voice_clients, guild=member.guild)
                        if not voice:
                            voice = await member.voice.channel.connect()
                        voice.play(discord.FFmpegPCMAudio('wlcome.mp3'))
                        voice.is_playing()
                        await asyncio.sleep(4)
                        os.remove("wlcome.mp3")
                        await voice.disconnect()

    ##on rady

@client.command()
async def help(ctx):
    color = []
    for clr in range(0x00000, 0xfffff):
        color.append(clr)
    inv = await ctx.channel.create_invite(max_age='10', max_uses=1)
    embed = discord.Embed(title=ctx.author.name, description="You Got This!", url= inv , color=color[0])
    embed.set_author(name="  All Commands",url="", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail( url="https://cdn.discordapp.com/avatars/929066952104767488/4b2e42b5bf544f2e19bad001563b3705.webp?size=1024")
    embed.add_field(name="x.ping", value="Test Ping", inline=False)
    embed.add_field(name="x.mangatx manga_name ", value="Search Your Favorite Manga", inline=False)
    embed.add_field(name="x.anime anime_name", value="Search your favorite anime details ", inline=True)
    embed.add_field(name="x.gs search_key", value="Search anything on google", inline=True)
    embed.add_field(name="x.gen uid", value="Genshin DB Search Your Id Detail With UID", inline=True)
    embed.add_field(name="x.gv facebook_link ", value="Share Facebook Video", inline=True)
    embed.add_field(name="x.t message ", value="Text To speech With Bot", inline=True)
    embed.set_footer(text="Copyright © White-Ant")
    await ctx.send(embed=embed)
@client.event
async def on_ready():
    print("Bot Running------------>")
    activity = discord.Activity(name="with JucyT 💦", type=1)  #
    await client.change_presence(activity=activity)


galis = TinyDB("Galidb.json")
q = Query()

def checkgal(words):
    for data in galis:
        if data["gali"] == words:
            return True
    return False

@client.event
async def on_message(message):
            if message.author == client.user: #boter commad e  react korbena
                return
            for badword in galis:
                badword = badword['gali']
                if badword in message.content.lower():
                    embed = discord.Embed(title="Warning!!", description=f"{message.author.name} Dont Use Badword!!", color=0xe40101)
                    embed.set_author(name= client.user.name , url="https://discord.gg/32rGZFTFEk", icon_url=message.author.avatar_url)
                    embed.set_thumbnail(url="https://cdn1.vectorstock.com/i/thumb-large/01/85/triangular-red-warning-hazard-symbol-vector-25180185.jpg")
                    embed.set_footer(text="Copyright \u00a9 White-Ant")
                    await message.channel.purge(limit=1)
                    await message.channel.send(embed=embed)
                    embed = discord.Embed(title="Warning!!", description="Be Careful With Your Word Sir!!", color=0xe40101)
                    embed.set_author(name=message.author.name, url="https://discord.gg/32rGZFTFEk", icon_url=message.author.avatar_url)
                    embed.add_field(name="**Bad Word**", value=f"{badword}", inline=True)
                    embed.set_thumbnail(url="https://cdn1.vectorstock.com/i/thumb-large/01/85/triangular-red-warning-hazard-symbol-vector-25180185.jpg")
                    embed.set_footer(text="Copyright \u00a9 White-Ant")
                    await message.author.send(embed = embed)
            await client.process_commands(message)


@commands.has_role("Whiteant")
@client.command()
async def addgali(ctx,*,data):
        if checkgal(data) == False:
                galis.insert({"gali": data})



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
async def delt(ctx, dat):
        await ctx.channel.purge(limit=int(dat))
 
    
    #role up
@commands.has_role("Whiteant")
@client.command()
async def rl(ctx,*,name):
        role = discord.utils.get(ctx.guild.roles, name=name)
        await ctx.author.add_roles(role)





@commands.has_role("Whiteant")
@client.command()
async def rerl(ctx,*,name):
        role = discord.utils.get(ctx.guild.roles, name=name)
        await ctx.author.remove_roles(role)



        #dm role
@commands.has_role("Whiteant")
@client.command()
async def dm(ctx, user: discord.User, *, msg):
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Private DM Sent To {user.name}....")
        await user.send(msg)



@commands.has_role("Whiteant")
@client.command()
async def leavex(ctx):
        print(ctx.guild.name)
        await ctx.send("I am leaving this guild!")
        await ctx.guild.leave()




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
           
           
        #anime search
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
        embed.add_field(name=f"Charecter {y}", value=iname, inline=True)
    embed.set_footer(text="Copyright \u00a9 White-Ant")
    await ctx.send(embed=embed)
        
        
        
        #video down
@client.command(pass_context=True)
async def gv(ctx, url):
    class Fbdl:
        def __init__(self):
            self.req = requests.Session()
            self.banner()
        def banner(self):
            ur = url
            rl = ur.replace('https://m.', 'https://mbasic.').replace('https://www.', 'https://mbasic.')
            self.getlnk(rl)
        def getlnk(self, url):
            r = self.req.get(url)
            rr = re.findall(r'<a href="(.*?)"', r.text)
            all_video = []
            for x in rr:
                if "/video_redirect/?src=" in x:
                    all_video.append(x)
            data = all_video[0]
            self.dl(data)
        def dl(self, link):
            re = link.replace('/video_redirect/?src=', '')
            ree = urllib.parse.unquote(re)
            print("Downloading ... ")
            with open(f"Video.mp4", "wb") as f:
                response = requests.get(ree, stream=True)
                total_length = response.headers.get('content-length')
                if total_length is None:
                     pass
                else:
                    dlw = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        ges = int(100*dlw/total_length)
                        dlw += len(data)
                        f.write(data)
                        done = int(25*dlw/total_length)
                        sys.stdout.write(f"\r[{'>'*done}{'='*(25-done)}] {ges+1}% ")
                        sys.stdout.flush()
    try:
        Fbdl()
        await ctx.channel.purge(limit=1)
        await ctx.send(file=discord.File("Video.mp4"))
        print("new video")
        if os.path.isfile('Video.mp4') == True:
                os.remove("Video.mp4")
    except:
        await ctx.send("Video Is not found / Too Large!! 8MB limit")
        await ctx.send(url)
        if os.path.isfile('Video.mp4') == True:
                os.remove("Video.mp4")
           

        #kd bot command
@client.command()
async def t(ctx,*,text):
            global gTTS
            speech = gTTS(text=text, lang="en-us", slow=False)
            speech.save("audio.mp3")
            voice = get(client.voice_clients, guild=ctx.guild)
            if not voice:
                voice = await ctx.author.voice.channel.connect()
            voice.play(discord.FFmpegPCMAudio('audio.mp3'))    
            audio = MP3("audio.mp3")
            duration = audio.info.length
            await asyncio.sleep(duration)
            os.remove("audio.mp3")
            await voice.disconnect()

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
                  # anim = stats["anemoculi"]
                  # geo = stats["geoculi"]
                  # elec = stats["electroculi"]
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
                  # embed.add_field(name="Anemoculus", value=f"{anim}/65", inline=True)
                  # embed.add_field(name="Geoculus", value=f"{geo}/160.", inline=True)
                  # embed.add_field(name="Anemoculus", value=f"{elec}/181", inline=True)
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


bddb = TinyDB("bd.json")
k = Query()
chk = []
@tasks.loop(seconds=1)
async def check():   
    await asyncio.sleep(10)
    today = str(date.today())
    bddate = bddb.search(k.bd==today)
    for ik in bddate:
        bd = ik["bd"]
        sal = int(timegg.year) - int(bd[0:4]) 
        idx =  ik['id']
        bdchen = client.get_channel(929061417825501266)
        if not chk:
            if today == bd:
                    await bdchen.send(f"**Happy {sal}th Birthday ** <@{idx}> ** From Team Jucy **\n @everyone")
    chk.append(today)
    if today != chk[0]:
        chk.clear()
check.start()

@commands.has_role("Whiteant")
@client.command()
async def alladd(ctx):
        members = ctx.message.guild.members
        for member in members:
               bddb.insert({"id":member.id,"bd":""})


@commands.has_role("Whiteant")
@client.command()
async def seid(ctx,name):
            data = bddb.search(k.id == int(name))[0] 
            idc = data['id']
            name = client.get_user(idc)
            age = int(timegg.year) - int(data['bd'][0:4])           
            await ctx.send(f"**Name: {name.name} \nBirthday: {data['bd']} \nAge: {age} **")


@commands.has_role("Jucy")
@client.command()
async def addbd(ctx, member: discord.User,date):
            bddb.update({"bd":date},k.id== member.id)
            await ctx.send("**Update Success**")





client.run("OTI5MDY2OTUyMTA0NzY3NDg4.Ydh7Bg.coEGUST0ErXPUTaUZOi-v1pascc")



