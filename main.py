import discord
from discord.ext import commands
import requests
from PIL import Image, ImageFont, ImageDraw

bot = commands.Bot(command_prefix='!')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def bhemjo(ctx):
    e = discord.Embed()
    e.set_image(url="https://images-ext-2.discordapp.net/external/8rweBNc5wtZWXgExkhDd1OYSmjJq96yyI8Uk3EK3kFE/https/media.discordapp.net/attachments/798212050496126976/873430327064952872/PicsArt_08-06-09.31.01.png?width=671&height=671")
    await ctx.send(embed=e)

@bot.command()
async def stats(ctx):
    # e = discord.Embed()
    my_image = Image.open("template.png")
    title_font = ImageFont.truetype('Poppins-Medium.ttf', 25)
    hehe_font =ImageFont.truetype('Poppins-Medium.ttf', 20) 
    tag_font = ImageFont.truetype('Poppins-Medium.ttf', 15)
    name = str(ctx.message.author.display_name)
    tag = str(ctx.message.author)
    score = 200

    level = 3
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((30,30), name, ((255,255,255)), font=title_font)
    image_editable.text((30,70), tag, ((255,255,255)), font=tag_font)
    image_editable.text((100,120), str(score), ((255,255,255)), font=hehe_font)
    image_editable.text((250,120), str(level), ((255,255,255)), font=hehe_font)
    my_image.save("result.png")
    # e.set_image("result.png")

    # file = discord.File("result.png", filename="...") 
    # await ctx.send("content", file=file)
    # await bot.send_file(ctx, "filepath.png")
    # await bot.send_file(ctx, "result.png", content="...", filename="...")
    # await ctx.send(embed=e)
    await ctx.send(file=discord.File('result.png'))



bot.run('<bot token hehe>')