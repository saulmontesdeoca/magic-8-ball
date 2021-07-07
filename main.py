# leave blank, we'll fill this in during the tutorial
from posix import times_result
import discord
import os
from discord import colour
from discord import embeds
from dotenv import load_dotenv
from discord.ext import commands
from random import randint


load_dotenv()

client = commands.Bot(command_prefix='!')
BOT_TOKEN = os.getenv("BOT_TOKEN")
embed_color = 0xAF00FA

fortunes = ['That\'s a weird question', 'Try again later', 'Probably yes', 'Probably no', 'Yes', 'No']

horoscopes = ['You should take risks today', 'Danger is near', 'Today be careful']

@client.event
async def on_ready():
    print('We are online')
    general_channel = client.get_channel(862028498180767786)
    await general_channel.send("Hello!")

@client.command(name='magic8')
async def magic8(ctx):
    info_embed = discord.Embed(title='The Magic 8 ball has been summoned',
    description='Hey',
    color=embed_color)

    info_embed.add_field(name='Want to see your future?', value='Type !future', inline=False)
    info_embed.add_field(name='Want to see your horoscope?', value='Click 🦄', inline=False)

    info_embed.set_thumbnail(url='https://media.giphy.com/media/7IW5OklceqGN9EmyZL/giphy.gif')


    info_msg = await ctx.send(embed=info_embed)
    await info_msg.add_reaction('🦄')

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    if reaction.emoji == '🦄':
        index = randint(0, len(horoscopes) -1)
    
    horoscope_embed = discord.Embed(title=horoscopes[index], description='', colour=embed_color)

    await user.send(embed=horoscope_embed)

@client.command(name='fortune')
async def fortune(ctx, *question):
    if len(question) == 0:
        await ctx.send('I need you to ask a question!')
    index = randint(0, len(fortunes) - 1)

    fortune_embed = discord.Embed(title=fortunes[index], description='', color=embed_color)

    await ctx.send(embed=fortune_embed)


client.run(BOT_TOKEN)