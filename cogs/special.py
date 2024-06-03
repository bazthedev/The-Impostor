import discord
from discord.ext import commands
import json
import random
import asyncio


async def vibe_check(ctx, badge):
  with open("badges.json", "r") as  f:
    ach = json.load(f)
    if str(ctx.author.id) in ach:
      if badge in ach[str(ctx.author.id)]:
        return
      else:
        ach[str(ctx.author.id)].append(badge)
        await ctx.author.send("You have unlocked the badge [{}]".format(badge))
    elif str(ctx.author.id) not in ach:
      ach[str(ctx.author.id)] = []
  with open("badges.json", "w") as f:
    json.dump(ach, f, indent=4)

codes = ["CRITICAL PROCESS DIED", "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED", "IRQL_NOT_LESS_OR_EQUAL", "VIDEO_TDR_TIMEOUT_DETECTED", "PAGE_FAULT_IN_NONPAGED_AREA", "SYSTEM_SERVICE_EXCEPTION", "DPC_WATCHDOG_VIOLATION"]

async def banned(ctx):
  with open("bans.json", "r") as f:
    bans = json.load(f)
    if str(ctx.author.id) in bans:
      await ctx.send("You have been banned from using this bot. If you wish to appeal for an unban, please go to my support server (https://discord.gg/Sun4mtFjwE) or directly contact Baz at bazthedev@gmail.com")
      return True
    else:
      return False

class Special(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def youareanidiot(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "You are an idiot")
    embed = discord.Embed()
    embed.set_image(url="https://c.tenor.com/jx-vfRytp4oAAAAd/you-are-an-idiot-idiot.gif")
    await ctx.send(embed=embed)
    await ctx.message.delete()



  @commands.command(aliases=["jenson308"])
  async def jenson(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Like and Subscribe!")
    embedJ = discord.Embed(
      title ="Jenson308",
description="Congrats!\nYou unlocked a secret badge!\nSubscribe to Jenson308 on YouTube!",
      url="https://bazbots.github.io/The-Impostor/jenson",
      colour =discord.Colour.red()
    )
    await ctx.send(embed=embedJ)
    await ctx.message.delete()
  
  """@commands.command()
  async def spooky(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Spooky scary skeletons!")
    emb = discord.Embed()
    emb.set_image(url="https://c.tenor.com/SmKGlfj3-b8AAAAC/spooky-scary.gif")
    await ctx.send(embed=emb)
    await ctx.message.delete()"""

  @commands.command()
  async def secret(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "secret badge 😏")
    await ctx.message.delete()

  """@commands.command(aliases=["bsod"])
  @commands.cooldown(1, 300, commands.BucketType.user)
  async def bluescreen(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "taskkill /f /im svchost.exe /t")
    await vibe_check(ctx, random.choice(codes))
    emb = discord.Embed(colour=0x0502ab)
    emb.set_image(url="https://c.tenor.com/Q83Htf2gJzMAAAAC/bsod-error.gif")
    await ctx.send(embed=emb)
    await ctx.message.delete()

  @commands.command()
  async def pong(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "you spelt it wrong")
    await ctx.send("umm did you spell it wrong or something")
    await ctx.message.delete()"""


  @commands.command()
  async def windows(self, ctx):
    await vibe_check(ctx, "<:oldwin:919541654921281586>")
    wininit = await ctx.send("```\nMS-DOS Executive 7.06\n\nC:\\WIN98\\>winload.exe```")
    await asyncio.sleep(5)
    await wininit.edit(content="```\nMS-DOS Executive 7.06\n\nC:\\WIN98\\System32\\>winload.exe\n\nStarting Windows 98...```") # <:oldwin:919541654921281586>
    await asyncio.sleep(3)
    await wininit.edit(content="https://tenor.com/view/microsoft-windows98-bill-gates-windows98vaporwave-start-up-gif-14688825")
    await asyncio.sleep(7)
    await wininit.edit(content="https://tenor.com/view/bsod-gif-19406617")
    await asyncio.sleep(5)
    await wininit.edit(content="https://tenor.com/view/pc-computer-shutting-down-off-windows-computer-gif-17192330")
    await asyncio.sleep(10)
    await wininit.delete()
    await ctx.message.delete()
  
  @commands.command()
  async def afton(self, ctx):
    await ctx.send("Y̴̨͔͎̤͉̗̥̼̹̝͖̝̻̞̬̙̌͊̂͆̿̈̽͛͆̓̅̾̐̆͘͜͝͠ͅǫ̵̡̨̡̧̲̲͎̝͈͍̙̘̘̻̘̦̖͔̖̼͕̬̟̫͍̙̅̂̆̐̂̀͒̄̇͊͠ữ̴̗̭̞͕͖̤̼̤̜̗̣̦͚̰̯͓͔̍̇͒̊̊͆̄̾̋̌̾̏́͌͊̈̓̇͛̕͘͜͠ ̶̡̧̨̹͉͈̙̱͍͔̫̪̼̙͍̄͗͒͆̽̾̿͌̕̚͜ċ̴͔̤̳̰̰́ą̷̹̙̺̠̺̻͚̞͈̫̫̻̭̘͚́͛ͅņ̵̡̢̨̡̣̫̫͈̠͔̱̮̺̫̺̳̩͚͔̼͖͖͋̆́͂̎͊͠ͅ'̸̩͉̳̠̱̫̜̓̉̀̌̆́̏͗̉̐͒̏͛̓̾̅̽̚̕̕͠͝t̸̢̢̛͓̗̖̹̺̅̂͊̌̓̀̌̆̍̕̚͠͠͝")
    

  @commands.command()
  async def who(self, ctx, asked = None):
    await vibe_check(ctx, "No body.")
    try:
      await ctx.message.delete()
    except Exception:
      pass
    await ctx.send("Who?")
    await asyncio.sleep(5)
    await ctx.send("Asked?")
    if asked != None:
      await asked.send("No body.")

    
def setup(client):
  client.add_cog(Special(client))