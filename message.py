import json
import discord







def message(client):

       galis = ["fuck", "shit", "gay" , "chudi", "chod", "ass" ,"pussy" , "boobs","magi" , "khanki"]
       @client.event
       async def on_message(message):
            if message.author == client.user: #boter commad e  react korbena
                return
            for badword in galis:
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
