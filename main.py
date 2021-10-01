import discord
from discord.ext import commands
import requests


bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def bhemjo(ctx):
    e = discord.Embed()
    e.set_image(url="https://images-ext-2.discordapp.net/external/8rweBNc5wtZWXgExkhDd1OYSmjJq96yyI8Uk3EK3kFE/https/media.discordapp.net/attachments/798212050496126976/873430327064952872/PicsArt_08-06-09.31.01.png?width=671&height=671")
    await ctx.send(embed=e)
    
bot.run('<bot token>')