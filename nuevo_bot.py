import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot llamado {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def bye(ctx):
    await ctx.send("bye" )    
@bot.command()
async def bye(ctx):
    await ctx.send("bye" )
bot.run("MTI1NDE3MTgzODQ0Mzk1MDEwMQ.Gh1Zze.ls3okr6GH1uUG2ceO9zyk4po0taTXhVc4v32PQ")