import discord
from discord.ext import commands
import json
from func import beanemo, vibe_check
import asyncio
import random
import string

async def banned(ctx):
  with open("bans.json", "r") as f:
    bans = json.load(f)
    if str(ctx.author.id) in bans:
      await ctx.send("You have been banned from using this bot. If you wish to appeal for an unban, please go to my support server (https://discord.gg/Sun4mtFjwE) or directly contact Baz at bazthedev@gmail.com")
      return True
    else:
      return False

async def tester(ctx):
  with open("testers.json", "r") as f:
    tests = json.load(f)
    if str(ctx.author.id) in tests or str(ctx.author.id) == "730043363671277638":
      return False
    else:
      await ctx.send("This command is for bot testers only, it will come out soon so until then please be patient")
      return True

cakes = ["beans", "cake", "fire", "impostor", "beans", "beans", "beans", "beans", "badge", "badge", "badge", "badge", "nothing", "nothing", "nothing", "cake", "impostor", "impostor", "cupcake"]

goodybags = ["toy", "squished", "empty"]

class Birthday(commands.Cog):

  def __init__(self, client):
     self.client = client

  @commands.command()
  @commands.is_owner()
  async def cake(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Happy Birthday! [The Impostor Birthday Event 2022]")
    await ctx.send(f"Do you want to buy and eat some cake for {beanemo} 500 (y/N)?")
    try:
      confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 20.0)
    except asyncio.TimeoutError:
      await ctx.send("You did not reply, so you didn't buy the cake")
      return
    else:
      if confirm.content[0].lower() == "y":
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          if str(ctx.author.id) not in bals:
            code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
            bals[str(ctx.author.id)] = {
                "benz":100,
                "Inventory":{},
                "xp":0,
                "lvl":0,
                "code": code
              }
            await ctx.author.send(f"Hey {ctx.author.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          if bals[str(ctx.author.id)]["benz"] < 500:
              await ctx.send("You can't buy this slice of cake, you don't have enough beans")
              return
          await ctx.send(f"You successfully bought a slice of cake for {beanemo} 500!")          
          bals[str(ctx.author.id)]["benz"] -= 500
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
      elif confirm.content[0].lower() == "n":
        await ctx.send("You did not buy the slice of cake")
        return
      else:
        await ctx.send("I did not understand, please rerun this command if you want to try again")
        return
    sliced = random.choice(cakes)
    if sliced == "beans":
      amt = random.randint(1000, 10000)
      await ctx.send(f"You ate some cake and got {amt} {beanemo} beans, must have been a bean flavoured cake")
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        bals[str(ctx.author.id)]["benz"] += amt
      with open("accounts.json", "w") as f:
        json.dump(bals, f, indent=4)
        return
    elif sliced == "cake":
      await ctx.send("You ate some cake and got more cake - that makes sense")
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        if "cake" not in bals[str(ctx.author.id)]["Inventory"]:
          bals[str(ctx.author.id)]["Inventory"]["cake"] = 1
        else:
          bals[str(ctx.author.id)]["Inventory"]["cake"] += 1
        with open("accounts.json", "w") as f:
          json.dump(bals, f, indent=4)
    elif sliced == "cupcake":
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        if "cupcake" not in bals[str(ctx.author.id)]["Inventory"]:
          bals[str(ctx.author.id)]["Inventory"]["cupcake"] = 1
        else:
          await ctx.send("Don't be greedy you already have a cupcake")
        return
    elif sliced == "fire":
      await ctx.send("You blew out the candle on your cake, and your house caught fire, along with you so you lost all your items.")
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        bals[str(ctx.author.id)]["benz"] = 0
      with open("accounts.json", "w") as f:
        json.dump(bals, f, indent=4)
      return
    elif sliced == "nothing":
      await ctx.send("You ate the cake and nothing happened, because it's cake")
      return
    elif sliced == "impostor":
      await ctx.send("You ate the cake and got a free Impostor tier subscription!")
      code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
      await ctx.author.send(f"Hey! You just won free Impostor Tier! Join the support server [https://discord.gg/Sun4mtFjwE] and message Baz with this unique code ({code}) and/or a screenshot to claim it!")
      with open("codes.json", "r") as f:
          codes = json.load(f)
          codes[str(code)] = {"Tier":"Impostor", "One time use":True}
      with open("codes.json", "w") as f:
          json.dump(codes, f, indent=4)
      return
    elif sliced == "badge":
      await ctx.send("You got a secret badge!")
      await vibe_check(ctx, "cake is yum")
      return
    else:
      await ctx.send("```\nFATAL:\n01000001 01101110 00100000 01110101 01101110 01101011 01101110 01101111 01110111 01101110 00100000 01100101 01110010 01110010 01101111 01110010 00100000 01101111 01100011 01100011 01110101 01110010 01110010 01100101 01100100 00101100 00100000 01110000 01101100 01100101 01100001 01110011 01100101 00100000 01100011 01101111 01101110 01110100 01100001 01100011 01110100 00100000 01101010 01101111 01101001 01101110 00100000 01101101 01111001 00100000 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01110011 01100101 01110010 01110110 01100101 01110010 00100000 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100100 01110011 01100011 00101110 01100111 01100111 00101111 01101001 01101101 01110000 01101111 01110011 01110100 01101111 01110010 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01100001 01101110 01100100 00100000 01100011 01110010 01100101 01100001 01110100 01100101 00100000 01100001 00100000 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01110100 01101001 01100011 01101011 01100101 01110100 00101110\n```")
      return
    

  @commands.command(aliases=["goody", "goodybag", "bag"])
  @commands.is_owner()
  async def open(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Happy Birthday! [The Impostor Birthday Event 2022]")
    await ctx.send(f"Do you want to open a goody bag for {beanemo} 250 (y/N)?")
    try:
      confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout = 20.0)
    except asyncio.TimeoutError:
      await ctx.send("You did not reply, so you didn't open the goody bag")
      return
    else:
      if confirm.content[0].lower() == "y":
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          if str(ctx.author.id) not in bals:
            code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
            bals[str(ctx.author.id)] = {
                "benz":100,
                "Inventory":{},
                "xp":0,
                "lvl":0,
                "code": code
              }
            await ctx.author.send(f"Hey {ctx.author.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          if bals[str(ctx.author.id)]["benz"] < 250:
              await ctx.send("You can't buy this goody bag, you don't have enough beans")
              return
          await ctx.send(f"You successfully bought a goody bag for {beanemo} 250!")          
          bals[str(ctx.author.id)]["benz"] -= 250
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
      elif confirm.content[0].lower() == "n":
        await ctx.send("You did not buy the goody bag")
        return
      else:
        await ctx.send("I did not understand, please rerun this command if you want to try again")
        return
    x = random.choice(goodybags)
    if x == "toy":
      with open("accounts.json", "r") as f:
        acc = json.load(f)
        if "Toy" not in acc[str(ctx.author.id)]["Inventory"]:
          acc[str(ctx.author.id)]["Inventory"]["Toy"] = 1
        else:
          acc[str(ctx.author.id)]["Inventory"]["Toy"] += 1
      with open("accounts.json", "w") as f:
        json.dump(acc, f, indent=4)
        await ctx.send("You opened your goody bag and recieved a toy!")
    elif x == "empty":
      await ctx.send("You opened your bag and it was empty")
      return
    elif x == "squished":
      await ctx.send("You opened your bag and you got some cake, but it was squashed, so you lost 1000 beans")
      with open("accounts.json", "r")as f:
        ac = json.load(f)
        if ac[str(ctx.author.id)]["benz"] <= 1000:
          ac[str(ctx.author.id)]["benz"] = 0
        else:
          ac[str(ctx.author.id)]["benz"] -= 1000
        with open("accounts.json", "w") as f:
          json.dump(ac, f, indent=4)
          return
    else:
      await ctx.send("```\nFATAL:\n01000001 01101110 00100000 01110101 01101110 01101011 01101110 01101111 01110111 01101110 00100000 01100101 01110010 01110010 01101111 01110010 00100000 01101111 01100011 01100011 01110101 01110010 01110010 01100101 01100100 00101100 00100000 01110000 01101100 01100101 01100001 01110011 01100101 00100000 01100011 01101111 01101110 01110100 01100001 01100011 01110100 00100000 01101010 01101111 01101001 01101110 00100000 01101101 01111001 00100000 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01110011 01100101 01110010 01110110 01100101 01110010 00100000 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100100 01110011 01100011 00101110 01100111 01100111 00101111 01101001 01101101 01110000 01101111 01110011 01110100 01101111 01110010 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01100001 01101110 01100100 00100000 01100011 01110010 01100101 01100001 01110100 01100101 00100000 01100001 00100000 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01110100 01101001 01100011 01101011 01100101 01110100 00101110\n```")
      return

def setup(client):
  client.add_cog(Birthday(client))