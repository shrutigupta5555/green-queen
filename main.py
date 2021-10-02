import discord #type:ignore
from discord.embeds import Embed #type:ignore
# from discord import client
from discord.ext import commands #type:ignore
import requests #type:ignore
from dotenv import load_dotenv #type:ignore
import os
import random
from bs4 import BeautifulSoup #type:ignore
from PIL import Image, ImageFont, ImageDraw #type:ignore
import asyncio
bot = commands.Bot(command_prefix='!')
load_dotenv()


def find_products(product_type, loc, budget):
# def find_products():
    url = f"https://www.crueltyfreekitty.com/list-of-cruelty-free-brands/?sustainable=on&shipping_location={loc}&retailer=&price={budget}&product_type={product_type}"
    # url ='https://www.crueltyfreekitty.com/list-of-cruelty-free-brands/?sustainable=on&shipping_location=international&retailer=&price=Budget&product_type=body-care'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, features="html.parser")


    tracks=soup.find_all("div", attrs ={"class": "brand-list__list__item"})


    data = []

    if len(tracks) >= 1:
        if len(tracks) > 5:
            t = 5
        else:
            t = len(tracks)
        
        for i in range(t):
            shop_name = tracks[i].find("a", class_="heading heading--secondary brand-list__list__title").getText()
            shop_list_div = tracks[i].find("div", class_="brand-list__list__shops")
            shop_list = tracks[i].find_all("a", attrs={"class": "button button--green brand-list__list__shop-button"}, href=True)
            s = []
            for shop in shop_list:
                shop_title = shop.getText()
                shop_link = shop['href']
                
                temp = {"shop_title": shop_title, "shop_link": shop_link}
                s.append(temp)
            d = {
                "name" : shop_name,
                "shops" : s
            }

            data.append(d)

            print(data, "====")
    return data

# find_products()
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
    product_list = ['baby','body-care','cleaning','deodrant','tanning-products',' false-eyelashes', 'feminine-hygiene', 'for-men', 'fragrance','hair-care', 'hair-dye', 'hair-removal','laundry', 'makeup','nail-polish','oral-care','skincare','sunscreen', '']
    shipping_list = ['international', 'uk-europe','usa' ,'australia', 'canada', '']
    price_range_list = ['Budget', 'mid-range', 'high-end', '']
    await ctx.send('What do you wanna buy [Choose one of the following] \n 1. Baby Products \n 2. Body Care \n 3. Cleaning \n 4. Deodrant \n 5. Tanning products \n 6. False eyelashes \n 7. Feminine hygiene \n 8. For men \n 9. Fragrance \n 10. Hair care \n 11. Hair dye \n 12. Hair removal \n 13. Laundry \n 14. Makeup \n 15. Nail polish \n 16. Oral care \n 17. skincare \n 18. sunscreen \n 19. All Products')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and int(msg.content) in range(1,20)

    product = await bot.wait_for("message", check=check)

    
    await ctx.send(f"Shipping location? [Choose one of the following] \n 1. International \n 2. UK/Europe \n 3. USA \n 4. Australia \n 5. Canada \n 6. All Shipping Locations")
    loc = await bot.wait_for("message", check=check)

    await ctx.send(f"Price Range? [Choose one of the following] \n 1. Budget \n 2. Mid-range \n 3. High-Range \n 4. All Budget Range")
    price_range = await bot.wait_for("message", check=check)


    async with ctx.typing():

        data = find_products(product_list[int(product.content)-1], shipping_list[int(loc.content)-1], price_range_list[int(price_range.content)-1])
    
        embeded = Embed(
            title = f"We searched far and wide",
            description = "Below is a list of some brands that are strictly animal cruelty free and sustainable",
            color = 0x000000
        )
        embeded.add_field(name = chr(173), value = chr(173))
        for i in range(len(data)):
            embeded.add_field(name="Shop Name",value=data[i]['name'], inline=False)
            # embeded.add_field(name="Available shops", value="Available shops", inline=False)
            shop_list = data[i]['shops']
            for shop in shop_list:
                embeded.add_field(name=f"🌱 {shop['shop_title']}" , value=f"{shop['shop_title']} \n {shop['shop_link']}", inline=False)
            embeded.add_field(name = chr(173), value = chr(173))

    embeded.add_field(name="Congratulations!!!",value="🍀 You've earned 50 coins for choosing sustainable brands 🍀", inline=False)
    await ctx.send(embed=embeded)
    # await ctx.send(f"You said product:{product_list[int(product.content)-1]} loc: {shipping_list[int(loc.content)-1]}  price: {price_range_list[int(price_range.content)-1]}")


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

@bot.command()
async def trycry(ctx):
    embeded = discord.Embed(
        title ="TryCry",
        description = "more try cry",
        color = 0x000000,
    )

    embeded.add_field(name="aakash baamzi", value="baamzi queem")
    await ctx.send(embed=embeded)

bot.run(os.getenv('BOT_TOKEN'))
# bot.run('<bot token hehe>')
