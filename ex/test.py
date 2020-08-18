import discord, os, random
from discord.ext import commands

weebs = commands.Bot(command_bot="!", owner_id=YOUR_ID)

@weebs.event()
async def on_ready():
  print("Am ready to you server! Owo")

@weebs.command(aliases=["animchar"])
async def animecharacter(ctx):
  weeb = random.choice("https://raw.githubusercontent.com/Jovantri10/wibu/master/src/weebchar.json")
  await ctx.send(weeb)

UWU = os.environ.get("TOKEN")
weebs.login(UWU)
