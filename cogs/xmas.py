import discord
from discord.ext import commands
import json
import random
import asyncio
import string

gifts = ["nothing", "coal", "beans", "impostor", "badge", "easter egg", "pirate"]

cracked = ["badge", "crew", "bean", "joke"]
whom = ["ctx", "usr"]

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
      ach[str(ctx.author.id)] = [badge]
  with open("badges.json", "w") as f:
    json.dump(ach, f, indent=4)

async def user_vibe_check(user, badge):
  with open("badges.json", "r") as  f:
    ach = json.load(f)
    if str(user.id) in ach:
      if badge in ach[str(user.id)]:
        return
      else:
        ach[str(user.id)].append(badge)
        await user.send("You have unlocked the badge [{}]".format(badge))
    elif str(user.id) not in ach:
      ach[str(user.id)] = [badge]
  with open("badges.json", "w") as f:
    json.dump(ach, f, indent=4)

class Xmas(commands.Cog):

  def __init__(self, client):
      self.client = client

  @commands.command()
  #@commands.is_owner()
  async def gift(self, ctx, user : commands.MemberConverter):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Merry Christmas! (Xmas '23)")
    if user.id == ctx.author.id:
      await ctx.send("Hey you can't gift something to your self, that's just being greedy")
      return
    if str(user.id) == "759436027529265172":
      await ctx.send("As much as I'd like one, I'm afraid you cannot send me a gift")
      return
    await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to send {user} a gift?\nThis is gonna cost you <:bean:908267086348955648> 500 (Yes/No)")
    try:
      confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send(f"I don't know where you went, so {user.mention} didn't recieve a gift")
    else:
      if confirm.content[0].lower() == "y":
        await vibe_check(ctx, "Spreading Christmas Cheer")
        await ctx.send(f"Sweet! Let's get {user.mention} a gift <:present:911658390604873778>")
      elif confirm.content[0].lower() == "n":
        await vibe_check(ctx, "You Scrooge!")
        await ctx.send(f"That's sad, {user.mention} did not recieve a gift, but at least you kept your 500 beans <:bean:908267086348955648>!")
        return
      else:
        await ctx.send(f"Hey {ctx.author.mention}, you have to say yes or no, not {confirm.content}!")
        return
      daprize = random.choice(gifts)
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        if bals[str(ctx.author.id)]["benz"] < 500:
          await ctx.send(f"{ctx.author.mention}, you need at least <:bean:908267086348955648> 500 to buy someone a gift")
          return
        if str(user.id) not in bals:
          bals[str(user.id)] = {
            "benz":100,
            "Inventory":{},
            "xp":0,
            "lvl":0
          }
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
        if str(ctx.author.id) not in bals:
          await ctx.send(f"Hey {ctx.author.mention}, you haven't got enough to buy {user.mention} a gift! Do some tasks and then you will earn some beans")
          return
        after_benz = bals[str(ctx.author.id)]["benz"] - 500
        bals[str(ctx.author.id)]["benz"] = after_benz
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
      if daprize == "nothing":
        await ctx.send(f"{user.mention} recieved nothing, that's a bit of a waste of money isn't it?")
        return
      elif daprize == "impostor":
        code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
        await user.send(f"Hey! You just won free Impostor Tier! Join the support server [https://discord.gg/Sun4mtFjwE] and message Baz with this unique code ({code}) and/or a screenshot to claim it!")
        with open("codes.json", "r") as f:
          codes = json.load(f)
          codes[str(code)] = {"Tier":"Impostor", "One time use":True}
        with open("codes.json", "w") as f:
          json.dump(codes, f, indent=4)
        await ctx.send(f"Wow! You gave {user.mention} a free Impostor Tier Subscription to the bot!")
        return
      elif daprize == "badge":
        await user_vibe_check(user, "'Tis the season of giving")
        await vibe_check(ctx, "'Tis the season of giving")
        await ctx.send("Both of you recieved an exclusive badge!")
      elif daprize == "coal":
        await ctx.send(f"You sent {user.mention} a lump of coal, were they on the naughty list?")
        with open("accounts.json", "r") as f:
          acc = json.load(f)
          if "Coal" not in acc[str(user.id)]["Inventory"]:
            acc[str(user.id)]["Inventory"]["Coal"] = 1
          else:
            acc[str(user.id)]["Inventory"]["Coal"] += 1
        with open("accounts.json", "w") as f:
          json.dump(acc, f, indent=4)
      elif daprize == "beans":
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          if str(user.id) not in bals:
            bals[str(user.id)] = {
                "benz":100,
                "Inventory":{},
                "xp":0,
                "lvl":0
              }
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          amt = random.randint(1000, 3000)
          bals[str(user.id)]["benz"] += amt
          with open("accounts.json", "w") as f:
                    json.dump(bals, f, indent=4)
          await ctx.send(f"{user.mention} was just gifted <:bean:908267086348955648> {amt}!")
      elif daprize == "easter egg":
        await ctx.send(f"You gave {user.mention} an easter egg!")
        await asyncio.sleep(6)
        await ctx.send("Wait a minute what's that doing here?")
        await vibe_check(ctx, "It's a bit early for that, or is it too late?")
        await user_vibe_check(user, "It's a bit early for that, or is it too late?")
      elif daprize == "pirate":
        await ctx.send("Yo ho ho!")
        await asyncio.sleep(5)
        await ctx.send("Wait that's not what Santa says!")
        await vibe_check(ctx, "That my friend is a pirate")
        await user_vibe_check(user, "That my friend is a pirate")
      else:
        await ctx.send("If you are seeing this message, then an unknown exception has occured. Please contact Baz#2641 (https://discord.gg/Sun4mtFjwE) and create a support ticket")

  @gift.error
  async def no_human(self, ctx, error):
    if await tester(ctx):
      return
    if await banned(ctx):
      return
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"Hey {ctx.author.mention}, you have to provide a valid discord user to send someone a gift!")
      
  @commands.command(aliases=["pull"])
  #@commands.is_owner()
  async def cracker(self, ctx, user : commands.MemberConverter):
    if await banned(ctx):
      return
    if user.id == ctx.author.id:
      await ctx.send("Hey you can't pull a cracker with yourself, that beats the whole objective!")
      return
    if str(user.id) == "759436027529265172":
      await ctx.send("I can't pull a Christmas Cracker, I got no arms!")
      return
    await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to pull a cracker with {user}?\nThis is gonna cost you <:bean:908267086348955648> 200 (Yes/No)")
    try:
      confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send(f"I don't know where you went, so looks like you're not going to pull a cracker")
    else:
      if confirm.content[0].lower() == "y":
        await ctx.send(f"Ok {ctx.author.mention}, let's pull a cracker with {user.mention}")
      elif confirm.content[0].lower() == "n":
        await ctx.send(f"Ok {ctx.author.mention}, you won't pull a cracker with {user.mention}")
        return
      else:
        await ctx.send("I don't understand, please provide yes or no")
        return
      gif = random.choice(cracked)
      who = random.choice(whom)
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        if bals[str(ctx.author.id)]["benz"] < 500:
          await ctx.send(f"{ctx.author.mention}, you need at least <:bean:908267086348955648> 200 to buy a cracker")
          return
        if str(user.id) not in bals:
          bals[str(user.id)] = {
            "benz":100,
            "Inventory":{},
            "xp":0,
            "lvl":0
          }
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
        if str(ctx.author.id) not in bals:
          await ctx.send(f"Hey {ctx.author.mention}, you haven't got enough to buy {user.mention} a gift! Do some tasks and then you will earn some beans")
          return
        after_benz = bals[str(ctx.author.id)]["benz"] - 200
        bals[str(ctx.author.id)]["benz"] = after_benz
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
      if gif == "badge":
        if who == "ctx":
          await ctx.send(f"{ctx.author.mention} got the good end of the cracker and got an exclusive badge!")
          await vibe_check(ctx, "A cracking joke")
          return
        else:
          await ctx.send(f"{user.mention} got the good end of the cracker and got an exclusive badge!")
          await user_vibe_check(user, "A cracking joke")
          return          
      elif gif == "crew":
        if who == "ctx":
          await ctx.send(f"{ctx.author.mention} got the good end of the cracker and also got a free crewmate tier subscription!")
          code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
          await ctx.author.send(f"Hey! You just won free Crewmate Tier! Join the support server [https://discord.gg/Sun4mtFjwE] and message Baz with this unique code ({code}) and/or a screenshot to claim it!")
          with open("codes.json", "r") as f:
            codes = json.load(f)
            codes[str(code)] = {"Tier":"Crewmate", "One time use":True}
          with open("codes.json", "w") as f:
            json.dump(codes, f, indent=4)
        else:
          await ctx.send(f"{user.mention} got the good end of the cracker and also got a free crewmate tier subscription!")
          code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
          await user.send(f"Hey! You just won free Crewmate Tier! Join the support server [https://discord.gg/Sun4mtFjwE] and message Baz with this unique code ({code}) and/or a screenshot to claim it!")
          with open("codes.json", "r") as f:
            codes = json.load(f)
            codes[str(code)] = {"Tier":"Crewmate", "One time use":True}
          with open("codes.json", "w") as f:
            json.dump(codes, f, indent=4)      
      elif gif == "bean":
        if who == "ctx":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if str(ctx.author.id) not in bals:
              bals[str(ctx.author.id)] = {
                  "benz":100,
                  "Inventory":{},
                  "xp":0,
                  "lvl":0
                }
              with open("accounts.json", "w") as f:
                  json.dump(bals, f, indent=4)
            amt = random.randint(500, 1500)
            bals[str(ctx.author.id)]["benz"] += amt
            with open("accounts.json", "w") as f:
                      json.dump(bals, f, indent=4)
            await ctx.send(f"{ctx.author.mention} got the good end of the cracker and got <:bean:908267086348955648> {amt}!")
            return
        else:
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if str(user.id) not in bals:
              bals[str(user.id)] = {
                  "benz":100,
                  "Inventory":{},
                  "xp":0,
                  "lvl":0
                }
              with open("accounts.json", "w") as f:
                  json.dump(bals, f, indent=4)
            amt = random.randint(500, 1500)
            bals[str(user.id)]["benz"] += amt
            with open("accounts.json", "w") as f:
                      json.dump(bals, f, indent=4)
            await ctx.send(f"{user.mention} got the good end of the cracker and got <:bean:908267086348955648> {amt}!")
      elif gif == "joke":
        if who == "ctx":
          await ctx.send(f"{ctx.author.mention} got the good end of the cracker and got a joke?")
          await asyncio.sleep(2)
          await ctx.send("It said:\nQ: Why did the Impostor lose the Crewmate?\nA: They forgot which way they vent!")
        else:
          await ctx.send(f"{ctx.author.mention} got the good end of the cracker and got a joke?")
          await asyncio.sleep(2)
          await ctx.send("It said:\nQ: Why did the Impostor lose the Crewmate?\nA: They forgot which way they vent!")
      else:
        await ctx.send("If you are seeing this message, then an unknown exception has occured. Please contact Baz#2641 (https://discord.gg/Sun4mtFjwE) and create a support ticket")

def setup(client):
  client.add_cog(Xmas(client))
