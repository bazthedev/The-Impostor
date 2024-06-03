import discord
from discord.ext import commands
import asyncio
import json
import random
import string
from datetime import datetime


async def tester(ctx):
  with open("testers.json", "r") as f:
    tests = json.load(f)
    if str(ctx.author.id) in tests or str(ctx.author.id) == "730043363671277638":
      return False
    else:
      await ctx.send("This command is for bot testers only, it will come out soon so until then please be patient")
      return True

class Secure(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def restore(self, ctx, user : commands.MemberConverter = None, code = None):
    await ctx.message.delete()
    if await tester(ctx):
      return
    if user is None:
      await ctx.send("You need to provide the ID, mention or name the account that you are trying to swap with")
      return
    if user == ctx.author:
      await ctx.send("You can't do this with yourself")
      return
    if code is None:
      await ctx.send("Hey, you need to provide a code for this to work")
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
            await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
      elif "code" not in bals[str(ctx.author.id)]:
        code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
        bals[str(ctx.author.id)]["code"] = code
        await ctx.author.send(f"Hey {ctx.author.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
            await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
    if code == None:
      await ctx.send(f"{ctx.author.mention}, you need to provide a valid restore code in order to use this command")
      return
    with open("accounts.json", "r") as f:
      uac = json.load(f)
      if code == uac[str(ctx.author.id)]["code"]:
        await ctx.send(f"{ctx.author.mention}, this is your current account's restore code!")
        await ctx.message.delete()
        return
      await ctx.send(f"{ctx.author.mention}, are you sure you want to perform this action - this is irreversible and will completely reset your current account, moving all existing data from the provided code holder's account to your's. (YES/n)")
      try:
        confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
      except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention}, I don't know where you went, so we can always do this another time")
        return
      else:
        if confirm.content == "YES":
          await ctx.send("Are you 100% sure you are ok with this, if you are, then please type `I UNDERSTAND` exactly how you see it here")
          try:
            confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
          except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author.mention}, I don't know where you went, so we can always do this another time")
            return
          else:
            if confirm.content == "I UNDERSTAND":
              await ctx.send(f"{ctx.author.mention}, ok, please wait whilst I migrate your account, this will overwrite all existing data on your account")
            elif confirm.content[0].lower() == "n":
              await ctx.send(f"Ok, I will cancel the requested action...")
              return
            else:
              await ctx.send(f"That is an invalid response, meaning that I will take that as a no")
              return
        elif confirm.content[0].lower() == "n":
          await ctx.send(f"Ok, I will cancel the requested action...")
          return
        else:
          await ctx.send(f"That is an invalid response, meaning that I will take that as a no")
          return
      for u in bals:
        if code == bals[str(u.id)]["code"]:
          bals[str(ctx.author.id)] = bals[str(u.id)]
          bals[str(u.id)].pop()
          with open("accounts.json"):
            json.dump(bals, f, indent=4)
            await ctx.send("Your account has been transfered.")
          with open("transfers.json", "r") as f:
            trans = json.load(f)
            now = datetime.now()
            now.strftime("%d/%m/%Y %H:%M:%S")
            trans[str(ctx.author.id)] = {
              "users": f"{ctx.author} ({str(ctx.author.id)}) and ({str(u.id)})",
              "code":code,
              "time":now
            }
            with open("transfers.json", "w"):
              json.dump(trans, f, indent=4)
              return
      await ctx.send("I had trouble finding the used code in my database")

  @commands.command(aliases=["id"])
  async def code(self, ctx):
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
            await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
            return
      elif "code" not in bals[str(ctx.author.id)]:
        code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
        bals[str(ctx.author.id)]["code"] = code
        await ctx.author.send(f"Hey {ctx.author.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
            await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
            return
      else:
        m = await ctx.author.send(f"{ctx.author.mention}, here is your unique account restore code. Do not share this with anyone as it could cause your account to be compromised.\n`{bals[str(ctx.author.id)]['code']}`")
        await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
        await asyncio.sleep(30)
        await m.delete()
        

def setup(client):
  client.add_cog(Secure(client))