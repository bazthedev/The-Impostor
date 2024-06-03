import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
from discord.ext import commands, tasks
import json
import random
import asyncio
import string
import os
import schedule
from func import spon

file = open("lotto.json", "r")
lot = json.load(file)

beanies =["<:bean:908267086348955648>", "<:goldenbean:911612797920608256>", "<:diamondbean:914149176974114908>", "<:emeraldbean:914151580629078046>", "<:7_:914156948176379934>", "<:purple:839879572631453696>", "<:starcmc:914472001140310026>", "<:polus:914518988002852905>", "<:toppat:914518916141826098>", "<:mirashards:914518926971514982>"]

weburl = os.getenv("WEBURL")

mira = []

polus = []

airship = []

lembed = discord.Embed(
  title = "Lottery",
  description="{} just won <:bean:908267086348955648> 10000000!",
  colour=discord.Colour.red()
)

async def foo():
  async with aiohttp.ClientSession() as session:
        webhook = Webhook.from_url(weburl, adapter=AsyncWebhookAdapter(session))
        await webhook.send(embed=lembed, username='The Impostor Lottery')

async def tester(ctx):
  with open("testers.json", "r") as f:
    tests = json.load(f)
    if str(ctx.author.id) in tests or str(ctx.author.id) == "730043363671277638":
      return False
    else:
      await ctx.send("This command is for bot testers only, it will come out soon so until then please be patient")
      return True

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

async def grantxp(ctx):
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
        tmp = random.randint(1, 10)
        bals[str(ctx.author.id)]["xp"] += tmp
        with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
        await ctx.send(f"{ctx.author.mention}, you recieved {tmp} xp!") # xp emoji
        myxp = bals[str(ctx.author.id)]["xp"]
        if bals[str(ctx.author.id)]["xp"] >= 100:
          bals[str(ctx.author.id)]["lvl"] += 1
          if bals[str(ctx.author.id)]["lvl"] == 1:
            await vibe_check(ctx, "Level 1")
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
              amt = random.randint(200, 400)
              after_benz = bals[str(ctx.author.id)]["benz"] + amt
              bals[str(ctx.author.id)]["benz"] = after_benz
              with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          if bals[str(ctx.author.id)]["xp"] > 100:
            bals[str(ctx.author.id)]["xp"] - 100
            bals[str(ctx.author.id)]["xp"] = 0
            bals[str(ctx.author.id)]["xp"] += myxp
        with open("accounts.json", "w") as f:
          json.dump(bals, f, indent=4)

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


      

class Beans(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["bal", "beans", "bean"])
  async def balance(self, ctx, member : discord.Member = None):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Beans beans, the more you eat the more you :flushed:")
    if not member == None and not member == ctx.author:
      ctx.author = member
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
        embedBal = discord.Embed(
            title=f"<:bean:908267086348955648> {ctx.author.name}'s Bean Balance <:bean:908267086348955648>",
            description="Total Amount: <:bean:908267086348955648> {0:,}".format(bals[str(ctx.author.id)]["benz"]),
            colour=discord.Colour.red()
          )
        await ctx.send(embed=embedBal)
        return "Added to beans"
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        embedBal = discord.Embed(
            title=f"<:bean:908267086348955648> {ctx.author.name}'s Bean Balance <:bean:908267086348955648>",
            description="Total Amount: <:bean:908267086348955648> {0:,}".format(bals[str(ctx.author.id)]["benz"]),
            colour=discord.Colour.red()
          )
        await ctx.send(embed=embedBal)

  @commands.command()
  async def shop(self, ctx, *, item = None):
    if await banned(ctx):
      return
    if item == None:
      em = discord.Embed(title = "Shop", colour=discord.Colour.red())
      with open("shop.json", "r") as f:
        mainshop = json.load(f)
        for key in mainshop:
          desc = mainshop[key]["desc"]
          if mainshop[key]["price"] == 0:
            continue
            pric = "Not for Sale" 
          else:
            pric = str(mainshop[key]["price"])
          emo = mainshop[key]["emoji"]
          if mainshop[key]["type"] == "p":
            typ = "Power Up"
          elif mainshop[key]["type"] == "c":
            typ = "Collectable"
          elif mainshop[key]["type"] == "t":
            typ = "Tool"
          elif mainshop[key]["type"] == "lb":
            typ = "Loot Box"
          else:
            await ctx.send("If you are seeing this message, then an unknown exception has occured. Please contact Baz#2641 (https://discord.gg/Sun4mtFjwE) and create a support ticket")
            return
          em.add_field(name=f"{str(key)} | {str(emo)}", value=f"**Description:**\n{desc}\n**Price:**\n<:bean:908267086348955648> {pric}\n**Type:**\n{typ}")
          em.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        await ctx.send(embed=em)
    else:
      with open("shop.json", "r") as f:
        shop = json.load(f)
        if item not in shop:
          for pro in shop:
            if item in shop[pro]["aliases"]:
              pric = shop[pro]["price"]
              if pric == 0:
                pric = "Not for Sale"
              em = discord.Embed(
                title=str(item),
                colour=discord.Colour.red()
              )
              em.add_field(name="Description:", value=shop[pro]["desc"], inline=True)
              em.add_field(name="Appearance:", value=shop[pro]["emoji"], inline=True)
              em.add_field(name="Price:", value=f'<:bean:908267086348955648> {str(pric)}', inline=True)
              em.add_field(name="Aliases", value=shop[pro]["aliases"], inline=True)
              em.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
              await ctx.send(embed=em)
        elif item in shop:
              typ = None
              if shop[item]["type"] == "p":
                typ = "Power Up"
              elif shop[item]["type"] == "c":
                typ = "Collectable"
              elif shop[item]["type"] == "t":
                typ = "Tool"
              elif shop[item]["type"] == "lb":
                typ = "Loot Box"
              pric = shop[item]["price"]
              if pric == 0:
                pric = "Not for Sale"
              em = discord.Embed(
                title=item,
                colour=discord.Colour.red()
              )
              em.add_field(name="Description:", value=shop[item]["desc"], inline=True)
              em.add_field(name="Appearance:", value=shop[item]["emoji"], inline=True)
              em.add_field(name="Price:", value=f"<:bean:908267086348955648> {str(pric)}", inline=True)
              em.add_field(name="Aliases:", value=f'{shop[item]["aliases"]}', inline=True)
              em.add_field(name="Type:", value=typ, inline=True)
              em.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
              await ctx.send(embed=em)
        else:
          await ctx.send("If you are seeing this message, then an unknown exception has occured. Please contact Baz#2641 (https://discord.gg/Sun4mtFjwE) and create a support ticket")

  @commands.command(aliases=["inventory"])
  async def inv(self, ctx, user : commands.MemberConverter = None):
    if await banned(ctx):
      return
    if user == None:
      user = ctx.author
    with open("accounts.json", "r") as f:
      uac = json.load(f)
      if str(user.id) not in uac:
        await ctx.send("You do not have an account, please run a task command to setup your account")
        return
      embed=discord.Embed(
        title="{}'s Inventory".format(user.name), colour=discord.Colour.red()
      )
      for item in uac[str(user.id)]["Inventory"]:
        embed.add_field(name=f"Item: {item}", value=f"Amount: {uac[str(user.id)]['Inventory'][item]}", inline=True)
      await ctx.send(embed=embed)

  @commands.command(aliases=["level", "rank"])
  @commands.is_owner()
  async def xp(self, ctx, user : commands.MemberConverter = None):
    if user is None:
      user = ctx.author
    if await tester(ctx):
      return
    if await banned(ctx):
      return
    with open("accounts.json", "r") as f:
        bals = json.load(f)
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
        embedxp = discord.Embed(
          title=f"{user.name}'s Level",
          description=f"Experience: {str(bals[str(user.id)]['xp'])}\nLevel: {str(bals[str(user.id)]['lvl'])}",
          colour=discord.Colour.red()
        )
        await ctx.send(embed=embedxp)

  @commands.command()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  async def daily(self, ctx,):
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
        else:
          amt = 1000
          after_work = bals[str(ctx.author.id)]["benz"] + amt
          bals[str(ctx.author.id)]["benz"] = after_work
          embed = discord.Embed(
            title="Daily Reward",
            description=f"You recieved <:bean:908267086348955648> {amt}",
            colour=discord.Colour.red()
          )
          await ctx.send(embed=embed)
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
            await spon(ctx)

  @commands.command()
  async def buy(self, ctx, item = None, amount = 1):
    if await tester(ctx):
      return
    if item == None:
      await ctx.send(f"{ctx.author.mention} you can't buy nothing")
      return "404 Not found"
    with open("shop.json", "r") as f:
      dashop = json.load(f)
      if item not in dashop:
        for pro in dashop:
          if item in dashop[pro]["aliases"]:
            if dashop[pro]["price"] == 0:
              await ctx.send("This item is currently not available for purchase.")
              return
            pro in dashop
            with open("accounts.json", "r") as f:
              acc = json.load(f)
              if acc[str(ctx.author.id)]["benz"] == 0:
                await ctx.send("You don't have any beans, come back after you have done some tasks")
                return
              price = amount * dashop[pro]["price"]
              if item in acc[str(ctx.author.id)]["Inventory"]:
                if acc[str(ctx.author.id)]["benz"] < price:
                  await ctx.send(f"Hey {ctx.author.mention}, you need at least {price} <:bean:908267086348955648>")
                  return
                await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to buy {item}?\nThis is gonna cost you <:bean:908267086348955648> {price} (Yes/No)")
                try:
                  confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                except asyncio.TimeoutError:
                  await ctx.send("I don't know where you went, so you were charged nothing")
                else:
                  if confirm.content[0].lower() == "y":
                    pass
                  elif confirm.content[0].lower() == "n":
                    await ctx.send(f"You did not buy {item}!")
                    return
                  else:
                    await ctx.send(f"Hey {ctx.author.mention}, you have to say yes or no, not {confirm.content}!")
                    return
                acc[str(ctx.author.id)]["benz"] -= dashop[pro]["price"] * amount
                acc[str(ctx.author.id)]["Inventory"][pro] += amount
                await ctx.send(f"{ctx.author.mention}, you bought {amount} {item}s for <:bean:908267086348955648> {price}")
              else:
                if acc[str(ctx.author.id)]["benz"] < price:
                  await ctx.send(f"Hey {ctx.author.mention}, you need at least {price} <:bean:908267086348955648>")
                  return
                await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to buy {item}?\nThis is gonna cost you <:bean:908267086348955648> {price} (Yes/No)")
                try:
                  confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
                except asyncio.TimeoutError:
                  await ctx.send("I don't know where you went, so you were charged nothing")
                else:
                  if confirm.content[0].lower() == "y":
                    pass
                  elif confirm.content[0].lower() == "n":
                    await ctx.send(f"You did not buy {item}!")
                    return
                  else:
                    await ctx.send(f"Hey {ctx.author.mention}, you have to say yes or no, not {confirm.content}!")
                    return
                
                acc[str(ctx.author.id)]["benz"] -= dashop[pro]["price"] * amount
                acc[str(ctx.author.id)]["Inventory"][pro] += amount
                await ctx.send(f"{ctx.author.mention}, you bought {amount} {item}s for <:bean:908267086348955648> {price}")
            with open("accounts.json", "w") as f:
              json.dump(acc, f, indent=4)
              await spon(ctx)
              return "used aliases"
        await ctx.send("This item does not exist")
        return "404 Item not found"
      if item in dashop:
        if dashop[item]["price"] == 0:
              await ctx.send("This item is currently not available for purchase.")
              return
        with open("accounts.json", "r") as f:
          acc = json.load(f)
          if acc[str(ctx.author.id)]["benz"] == 0:
            await ctx.send("You don't have any beans, come back after you have done some tasks")
            return
          price = amount * dashop[item]["price"]
          if item in acc[str(ctx.author.id)]["Inventory"]:
            if acc[str(ctx.author.id)]["benz"] < price:
              await ctx.send(f"Hey {ctx.author.mention}, you need at least {price} <:bean:908267086348955648>")
              return
            await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to buy {item}?\nThis is gonna cost you <:bean:908267086348955648> {price} (Yes/No)")
            try:
                  confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
            except asyncio.TimeoutError:
                  await ctx.send("I don't know where you went, so you were charged nothing")
            else:
                  if confirm.content[0].lower() == "y":
                    pass
                  elif confirm.content[0].lower() == "n":
                    await ctx.send(f"You did not buy {item}!")
                    return
                  else:
                    await ctx.send(f"Hey {ctx.author.mention}, you have to say yes or no, not {confirm.content}!")
                    return
            acc[str(ctx.author.id)]["benz"] -= dashop[item]["price"] * amount
            acc[str(ctx.author.id)]["Inventory"][item] += amount
            await ctx.send(f"{ctx.author.mention}, you bought {amount} {item}s for <:bean:908267086348955648> {price}")
          else:
            if acc[str(ctx.author.id)]["benz"] < price:
              await ctx.send(f"Hey {ctx.author.mention}, you need at least {price} <:bean:908267086348955648>")
              return
            await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to buy {item}?\nThis is gonna cost you <:bean:908267086348955648> {price} (Yes/No)")
            try:
                  confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
            except asyncio.TimeoutError:
                  await ctx.send("I don't know where you went, so you were charged nothing")
            else:
                  if confirm.content[0].lower() == "y":
                    pass
                  elif confirm.content[0].lower() == "n":
                    await ctx.send(f"You did not buy {item}!")
                    return
                  else:
                    await ctx.send(f"Hey {ctx.author.mention}, you have to say yes or no, not {confirm.content}!")
                    return
            acc[str(ctx.author.id)]["benz"] -= dashop[item]["price"] * amount
            acc[str(ctx.author.id)]["Inventory"][item] += amount
            await ctx.send(f"{ctx.author.mention}, you bought {amount} {item}s for <:bean:908267086348955648> {price}")
        with open("accounts.json", "w") as f:
          json.dump(acc, f, indent=4)
          await spon(ctx)


  @commands.command()
  async def eat(self, ctx, *, amt):
    if await tester(ctx):
      return
    if await banned(ctx):
      return
    em = discord.Embed(
      title="yum",
      description=f"You ate <:bean:908267086348955648> {amt} beans and was very yummy",
      colour=0x129ae3
    )
    await ctx.send(embed=em)
    await asyncio.sleep(5)
    await ctx.send("you did a big fard cos you ate a lot of beans")

  @commands.command(aliases=["gamble"])
  async def slots(self, ctx, *, override_code = None):
    if await banned(ctx):
      return
    if override_code == "@override:slots.instawin = true":
      beanies = ["<:7_:914156948176379934>"]
      channel = self.client.get_channel(838465155582394390)
      em = discord.Embed(
title="Console",
        description=f"{ctx.author} has used the override code in {ctx.guild.name} with {ctx.guild.member_count}")
      await channel.send(embed=em)
      await ctx.message.delete()
    if override_code != "@override:slots.instawin = true":
      beanies =["<:bean:908267086348955648>", "<:goldenbean:911612797920608256>", "<:diamondbean:914149176974114908>", "<:emeraldbean:914151580629078046>", "<:7_:914156948176379934>", "<:purple:839879572631453696>", "<:starcmc:914472001140310026>", "<:polus:914518988002852905>", "<:toppat:914518916141826098>", "<:mirashards:914518926971514982>"]
    await ctx.send(f"{ctx.author.mention}, how many beans do you want to put down?")
    try:
      gambled = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send("Ok, maybe we can try this another time")
      return
    else:
      if gambled.content.lower() == "cancel":
        await ctx.send("Ok, I will cancel the requested action")
        return
      else:
        try:
          gamb = int(gambled.content)
        except Exception:
          await ctx.send("You need to provide a number")
          return
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
          if gamb > uac[str(ctx.author.id)]["benz"]:
            await ctx.send("You do not have enough beans to gamble this much!")
            return
          if gamb < 1:
            await ctx.send("I'm afraid that number is too small")
            return
        await ctx.send(f"You put down <:bean:908267086348955648> {gambled.content}, so let's play slots!")
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          after_benz = bals[str(ctx.author.id)]["benz"] - gamb
          bals[str(ctx.author.id)]["benz"] = after_benz
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
        await asyncio.sleep(5)
    b1 = random.choice(beanies)
    b2 = random.choice(beanies)
    b3 = random.choice(beanies)
    embed = discord.Embed(
      title="Slots",
      description="[ <:hash:914156948256063498> ][ <:hash:914156948256063498> ][ <:hash:914156948256063498> ]",
      colour=discord.Colour.red()
    )
    e = await ctx.send(embed=embed)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {random.choice(beanies)} ][ <:hash:914156948256063498> ][ <:hash:914156948256063498> ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ <:hash:914156948256063498> ][ <:hash:914156948256063498> ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {random.choice(beanies)} ][ <:hash:914156948256063498> ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ <:hash:914156948256063498> ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ {random.choice(beanies)} ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ {b3} ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    if b1 == "<:purple:839879572631453696>":
      if b2 == "<:purple:839879572631453696>":
        if b3 == "<:purple:839879572631453696>":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            await ctx.send(f"You lost <:bean:908267086348955648> {gamb}!")
            res = gamb
            after_benz = bals[str(ctx.author.id)]["benz"] - res
            bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            return
    if b1 == "<:bean:908267086348955648>":
      if b2 == "<:bean:908267086348955648>":
        if b3 == "<:bean:908267086348955648>":
          with open("accounts.json", "r") as f:
            res = gamb * 2
            bals = json.load(f)
            after_benz = bals[str(ctx.author.id)]["benz"] + res
            bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You got <:bean:908267086348955648> {res} from gambling!")
            return
    if b1 == "<:goldenbean:911612797920608256>":
      if b2 == "<:goldenbean:911612797920608256>":
        if b3 == "<:goldenbean:911612797920608256>":
          with open("accounts.json", "r") as f:
            res = 1
            bals = json.load(f)
            bals[str(ctx.author.id)]["Inventory"]["Golden Bean"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved 1 <:goldenbean:911612797920608256> from gambling!")
            return
    if b1 == "<:diamondbean:914149176974114908>":
      if b2 == "<:diamondbean:914149176974114908>":
        if b3 == "<:diamondbean:914149176974114908>":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if gamb >= 10000000000:
              res = gamb + 10000000000
            else:
              res = 10000000000
            after_benz = bals[str(ctx.author.id)]["benz"] + res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You recieved <:bean:908267086348955648> {res} from gambling!")
            return
    if b1 == "<:7_:914156948176379934>":
      if b2 == "<:7_:914156948176379934>":
        if b3 == "<:7_:914156948176379934>":
          with open("accounts.json", "r") as f:
            res = gamb * 7
            bals = json.load(f)
            after_benz = bals[str(ctx.author.id)]["benz"] + res
            bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You got <:bean:908267086348955648> {res} from gambling!")
            return
    if b1 == "<:emeraldbean:914151580629078046>":
      if b2 == "<:emeraldbean:914151580629078046>":
        if b3 == "<:emeraldbean:914151580629078046>":
          with open("accounts.json", "r") as f:
            res = 1
            bals = json.load(f)
            if "Emerald Bean" not in bals[str(ctx.author.id)]["Inventory"]:
              bals[str(ctx.author.id)]["Inventory"]["Emerald Bean"] = 1
            else:
              bals[str(ctx.author.id)]["Inventory"]["Emerald Bean"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved 1 <:emeraldbean:914151580629078046> from gambling!")
            return
            # <:starcmc:914472001140310026>
    if b1 == "<:starcmc:914472001140310026>":
      if b2 == "<:starcmc:914472001140310026>":
        if b3 == "<:starcmc:914472001140310026>":
          with open("accounts.json", "r") as f:
            res = random.randint(1, 5)
            bals = json.load(f)
            if "Stars" not in bals[str(ctx.author.id)]:
              bals[str(ctx.author.id)]["Stars"] = res
            else:
              bals[str(ctx.author.id)]["Stars"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved {} <:starcmc:914472001140310026> from gambling!".format(res))
            return
    if b1 == "<:polus:914518988002852905>":
      if b2 == "<:polus:914518988002852905>":
        if b3 == "<:polus:914518988002852905>":
          with open("accounts.json", "r") as f:
            res = random.randint(1, 5)
            bals = json.load(f)
            if "Polus" not in bals[str(ctx.author.id)]:
              bals[str(ctx.author.id)]["Polus"] = res
            else:
              bals[str(ctx.author.id)]["Polus"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved {} <:polus:914518988002852905> from gambling!".format(res))
            return
    if b1 == "<:toppat:914518916141826098>":
      if b2 == "<:toppat:914518916141826098>":
        if b3 == "<:toppat:914518916141826098>":
          with open("accounts.json", "r") as f:
            res = random.randint(1, 5)
            bals = json.load(f)
            if "Hats" not in bals[str(ctx.author.id)]:
              bals[str(ctx.author.id)]["Hats"] = res
            else:
              bals[str(ctx.author.id)]["Hats"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved {} <:toppat:914518916141826098> from gambling!".format(res))
            return
    if b1 == "<:mirashards:914518926971514982>":
      if b2 == "<:mirashards:914518926971514982>":
        if b3 == "<:mirashards:914518926971514982>":
          with open("accounts.json", "r") as f:
            res = random.randint(1, 5)
            bals = json.load(f)
            if "Shards" not in bals[str(ctx.author.id)]:
              bals[str(ctx.author.id)]["Shards"] = res
            else:
              bals[str(ctx.author.id)]["Shards"] += res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send("You recieved {} <:mirashards:914518926971514982> from gambling!".format(res))
            return 
    await ctx.send("You did not win anything")


def setup(client):
  client.add_cog(Beans(client))