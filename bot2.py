import discord
from discord.ext import commands
import random
import requests
from bot_mantik import gen_pass, yazi_tura, kalp
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command(name='kalp')
async def kalp_komut(ctx):
    sonuc = kalp()
    await ctx.send(sonuc)

@bot.command(name='yazi_tura')
async def yazi_tura_komut(ctx):
    sonuc = yazi_tura()
    await ctx.send(sonuc)

@bot.command(name='parola')
async def parola(ctx):
    sonuc = gen_pass(pass_length=10)
    await ctx.send(sonuc)

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def rastgele(ctx):
    ImageName = random.choice(os.listdir(r'C:\Users\CASPER\Desktop\Kodland\images'))
    with open(f"images/{ImageName}", "rb") as f:
        resim = discord.File(f)
        await ctx.send(file=resim)

# Örnek bir get_duck_image_url() fonksiyonu
def get_duck_image_url():
    url = "https://random-d.uk/api/v2/random"
    res = requests.get(url)
    return res.json()["url"]

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# Meme API'si kullanarak rastgele bir meme alan komut
def get_meme_image_url():
    url = "https://api.imgflip.com/get_memes"
    res = requests.get(url)
    memes = res.json()["data"]["memes"]
    return random.choice(memes)["url"]

@bot.command(name='meme')
async def meme(ctx):
    meme_url = get_meme_image_url()
    await ctx.send(meme_url)

















bot.run("")