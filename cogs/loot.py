import discord
from discord.ext import commands
import json
import random
import string

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

async def banned(ctx):
  with open("bans.json", "r") as f:
    bans = json.load(f)
    if str(ctx.author.id) in bans:
      await ctx.send("You have been banned from using this bot. If you wish to appeal for an unban, please go to my support server (https://discord.gg/Sun4mtFjwE) or directly contact Baz at bazthedev@gmail.com")
      return True
    else:
      return False

async def chkdsk(ctx):
  with open("accounts.json", "r") as f:
          uac = json.load(f)
          if str(ctx.author.id) not in uac:
            code = str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters) + str(random.randint(0, 9)) + random.choice(string.ascii_letters)
            uac[str(ctx.author.id)] = {
                "benz":100,
                "Inventory":{},
                "xp":0,
                "lvl":0,
                "code": code
              }
            await ctx.author.send(f"Hey {ctx.author.mention}, incase of something happening to your discord account, I have created you a unique code that you can use to redeem all of your beans and any premium tiers you may have had. Code: `{code}`, keep this safe.")
            with open("accounts.json", "w") as f:
                json.dump(uac, f, indent=4)

class Loot(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.is_owner()
  async def use(self, ctx, item = None, amount = 1):
    if await tester(ctx):
      return
    if await banned(ctx):
      return
    await chkdsk(ctx)
    if item is None:
      await ctx.send("You have to provide an actual lootbox name!")
      return
    rew = {}
    with open("accounts.json", "r") as f:
      bals = json.load(f)
      if item == "mira" or item == "shard":
        if bals[str(ctx.author.id)]["Inventory"]["Mira Lootbox"] >= 1:
          with open("lb.json", "r") as ff:
            lb = json.load(ff)
            item = random.choice(lb["mira"])
            rew[item] = random.randint(1, 3)
            for items in rew:
              if items not in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] = int(rew[items])
              if item in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] += int(rew[items])
            amt = random.randint(lb["mira"]["beansa"], lb["mira"]["beansb"])
            bals[str(ctx.author.id)]["benz"] += amt
            bals[str(ctx.author.id)]["Shards"] -= 1
      elif item == "polus":
        if bals[str(ctx.author.id)]["Inventory"]["Polus Lootbox"] >= 1:
          with open("lb.json", "r") as ff:
            lb = json.load(ff)
            item = random.choice(lb["polus"])
            rew[item] = random.randint(1, 3)
            for items in rew:
              if items not in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] = int(rew[items])
              if item in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] += int(rew[items])
            amt = random.randint(lb["polus"]["beansa"], lb["polus"]["beansb"])
            bals[str(ctx.author.id)]["benz"] += amt
            bals[str(ctx.author.id)]["Polus"] -= 1
      elif item.lower() == "airship":
        if bals[str(ctx.author.id)]["Inventory"]["Airship Lootbox"] >= 1:
          with open("lb.json", "r") as ff:
            lb = json.load(ff)
            item = random.choice(lb["air"])
            rew[item] = random.randint(1, 3)
            for items in rew:
              if items not in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] = int(rew[items])
              if item in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] += int(rew[items])
            amt = random.randint(lb["air"]["beansa"], lb["air"]["beansb"])
            bals[str(ctx.author.id)]["benz"] += amt
            bals[str(ctx.author.id)]["Inventory"]["Airship Lootbox"] -= 1
      elif item[:4].lower() == "star":
        if bals[str(ctx.author.id)]["Inventory"]["Stars"] >= 1:
          with open("lb.json", "r") as ff:
            lb = json.load(ff)
            item = random.choice(lb["star"])
            rew[item] = random.randint(1, 3)
            for items in rew:
              if items not in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] = int(rew[items])
              if item in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] += int(rew[items])
            amt = random.randint(lb["star"]["beansa"], lb["star"]["beansb"])
            bals[str(ctx.author.id)]["benz"] += amt
            bals[str(ctx.author.id)]["Stars"] -= 1
      elif item.lower() == "can":
        if bals[str(ctx.author.id)]["Inventory"]["Can of Beans"] >= 1:
          with open("lb.json", "r") as ff:
            lb = json.load(ff)
            item = random.choice(lb["air"])
            rew[item] = random.randint(1, 3)
            for items in rew:
              if items not in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] = int(rew[items])
              if item in bals[str(ctx.author.id)]["Inventory"]:
                bals[str(ctx.author.id)]["Inventory"][items] += int(rew[items])
            amt = random.randint(lb["air"]["beansa"], lb["air"]["beansb"])
            bals[str(ctx.author.id)]["benz"] += amt
            bals[str(ctx.author.id)]["Hats"] -= 1
      else:
        await ctx.send("This lootbox does not exist!")
        return
    with open("accounts.json", "w") as f:
      json.dump(bals, f, indent=4)


def setup(client):
  client.add_cog(Loot(client))