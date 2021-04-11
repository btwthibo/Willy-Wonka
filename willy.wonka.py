import discord
from discord.ext import commands
import datetime
import random
import os
from urllib import parse, request
import re

bot = commands.Bot(command_prefix='-', description="This is willy wonka")


responses = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Thibos's mom told me yes", "Thibos's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]


@bot.command(aliases=['FortuneTeller'])
async def FurtureTeller(ctx, *, question):
    responses = ["As I see it, yes", "Yes", "No", "Very likely", "Not even close", "Maybe", "Very unlikely", "Thibos's mom told me yes", "Thibos's mom told me no", "Ask again later", "Better not tell you now", "Concentrate and ask again", "Don't count on it", " It is certain", "My sources say no", "Outlook good", "You may rely on it", "Very Doubtful", "Without a doubt"]
    
    await ctx.send(F'Question {question}\nAnswer: {random.choice(responses)}')

    if message.content.startswith("!m8b"):
        lucky_num = random.randint(0,len(response_list) - 1)
        await message.channel.send(response_list[lucky_num])


@bot.command()
async def pretty(ctx):
	await ctx.send('Nope you are not.')
	
@bot.command()
async def wonka?(ctx):
    await ctx.send('Wonka bars are the best chcolate bars in the world. created by willy wonka. did you know willy wonka is very sexy!')
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'pong {round(bot.latency * 1000))}ms')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="-ping shows latency", url="http://www.twitch.tv/accountname"))
    print('Willy wonka')

bot.run('token')
