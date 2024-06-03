import random
from discord import Webhook, AsyncWebhookAdapter
import discord
import json
import aiohttp
import os
import asyncio
from discord.ext import commands, tasks
import string
import json

#weburl = os.getenv("WEBURL")
weburl = os.getenv("WEB")

file = open("lotto.json", "r")
lot = json.load(file)

async def draw_winner():
    win = random.choice(lot)
    return win

async def lottery_main(self):
    win = await draw_winner()
    user = self.client.get_user(730043363671277638)
    lembed = discord.Embed(
      title = "Lottery",
      description=f"<@{win}> just won <:bean:908267086348955648> 10000000!",
      colour=discord.Colour.red()
    )
    await foo(lembed)
    """with open("accounts.json", "r") as f:
          bals = json.load(f)
          code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
          bals[str(user.id)] = {
              "benz":100,
              "Inventory":{},
              "xp":0,
              "lvl":0,
              "code": code
            }
          await user.send(f"Hey {user.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
          with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
          amt = 10000000
          after_benz = bals[str(user.id)]["benz"] + amt
          bals[str(user.id)]["benz"] = after_benz
          with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
          await user.send("You just won the lottery and recieved 10 million beans!")"""
    with open("lotto.json", "r") as f:
      lots = json.load(f)
      for human in lots:
        lots.pop(str(human))
    with open("lotto.json", "w"):
      json.dump(lots, f, indent=4)

async def foo(emb):
    async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(weburl, adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=emb, username='The Impostor Lottery')

async def tester(ctx):
  with open("testers.json", "r") as f:
    tests = json.load(f)
    if str(ctx.author.id) in tests or str(ctx.author.id) == "730043363671277638":
      return False
    else:
      await ctx.send("This command is for bot testers only, it will come out soon so until then please be patient")
      return True

class Lotto(commands.Cog):

  def __init__(self,client):
    self.client = client
    #self.ltmain.start()

  @tasks.loop(seconds=60)
  async def ltmain(self):
    await lottery_main(self)

  @commands.command()
  async def lotto(self, ctx):
    if await tester(ctx):
      return
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
      with open("lotto.json", "r") as f:
        lott = json.load(f)
        if str(ctx.author.id) in lott:
          await ctx.send(f"{ctx.author.mention}, you have already bought a lotto ticket!")
          return
        await ctx.send(f"{ctx.author.mention}, do you want to buy a lotto ticket for <:bean:908267086348955648> 1000?")
        try:
          confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
        except asyncio.TimeoutError:
          await ctx.send("I don't know where you went, so we can always do this later")
        else:
          if confirm.content[0].lower() == "y":
            pass
          elif confirm.content[0].lower() == "n":
            await ctx.send("You did not buy this lottery ticket")
            return
          else:
            await ctx.send("I don't understand")
            return
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
          if bals[str(ctx.author.id)]["benz"] < 1000:
            await ctx.send("You do not have enough to buy a lottery ticket")
          amt = 1000
          after_benz = bals[str(ctx.author.id)]["benz"] - amt
          bals[str(ctx.author.id)]["benz"] = after_benz
          with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
        lott.append(str(ctx.author.id))
        await ctx.send(f"{ctx.author.mention}, you successfully bought a lottery ticket for <:bean:908267086348955648> 1000!")
      with open("lotto.json", "w") as f:
        json.dump(lott, f, indent=4)

def setup(client):
  client.add_cog(Lotto(client))