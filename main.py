import discord
# from discord import client
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
import random

bot = commands.Bot(command_prefix='!')
load_dotenv()



@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def bhemjo(ctx):
    e = discord.Embed()
    e.set_image(url="https://images-ext-2.discordapp.net/external/8rweBNc5wtZWXgExkhDd1OYSmjJq96yyI8Uk3EK3kFE/https/media.discordapp.net/attachments/798212050496126976/873430327064952872/PicsArt_08-06-09.31.01.png?width=671&height=671")
    await ctx.send(embed=e)
    
@bot.command()
async def guess(ctx):
    computer = random.randint(1, 10)
    await ctx.send('Guess my number')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    msg = await bot.wait_for("message", check=check)

    if int(msg.content) == computer:
        await ctx.send("Correct")
    else:
        await ctx.send(f"Nope it was {computer}")


@bot.command()
async def find(ctx):
    # computer = random.randint(1, 10)
    product_list = ['baby','body-care','cleaning','deodrant','tanning-products',' false-eyelashes', 'feminine-hygiene', 'for-men', 'fragrance','hair-care', 'hair-dye', 'hair-removal','laundry', 'makeup','nail-polish','oral-care','skincare','sunscreen']
    shipping_list = ['international', 'uk-europe','usa' ,'australia', 'canada', '']
    price_range_list = ['budget', 'mid-range', 'high-range']
    await ctx.send('What do you wanna buy [Choose one of the following] \n 1. Baby Products \n 2. Body Care \n 3. Cleaning \n 4. Deodrant \n 5. Tanning products \n 6. False eyelashes \n 7. Feminine hygiene \n 8. For men \n 9. Fragrance \n 10. Hair care \n 11. Hair dye \n 12. Hair removal \n 13. Laundry \n 14. Makeup \n 15. Nail polish \n 16. Oral care \n 17. skincare \n 18. sunscreen')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in range(1,20)

    product = await bot.wait_for("message", check=check)

    
    await ctx.send(f"Shipping location? [Choose one of the following] \n 1. International \n 2. UK/Europe \n 3. USA \n 4. Australia \n 5. Canada \n 6. All Shipping Locations")
    loc = await bot.wait_for("message", check=check)

    await ctx.send(f"Price Range? [Choose one of the following] \n 1. Budget \n 2. Mid-range \n 3. High-Range")
    price_range = await bot.wait_for("message", check=check)

    await ctx.send(f"You said product:{product_list[int(product.content)-1]} loc: {shipping_list[int(loc.content)-1]}  price: {price_range_list[int(price_range.content)-1]}")

bot.run(os.getenv('BOT_TOKEN'))