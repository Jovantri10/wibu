☄Random Character Json File's for a weebs discord bot and easy to use!
> Hello guys, follow this guide! [Click Here for go to json file. This just as example](https://github.com/Jovantri10/wibu/blob/master/src/weebchar.json), after go to json file, press the `raw` button for change that **as** rest api, and can to use [Click here to raw example](https://raw.githubusercontent.com/Jovantri10/wibu/master/src/weebchar.json). Easy? Try Now. Confused with code? We have some example here, scrool!

# Python Example
## main.py
``` python
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
```
## .env
```TOKEN = YOU_BOT_TOKEN```
