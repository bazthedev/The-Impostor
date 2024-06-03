import discord
from discord.ext import commands
from colorama import Fore
import asyncio
import random
import json

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
        myxp = bals[str(ctx.author.id)]["xp"] - 100
        if bals[str(ctx.author.id)]["xp"] >= 100:
          bals[str(ctx.author.id)]["lvl"] += 1
          bals[str(ctx.author.id)]["xp"] = 0
          bals[str(ctx.author.id)]["xp"] += myxp
          """with open("accounts.json", "w"):
            json.dump(bals, f, indent=4)"""
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
              amt = random.randint(1000, 2000)
              after_benz = bals[str(ctx.author.id)]["benz"] + amt
              bals[str(ctx.author.id)]["benz"] = after_benz
              with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
                await ctx.send(f"{ctx.author.mention}, you leveled up to level {str(bals[str(ctx.author.id)]['lvl'])} and recieved <:bean:908267086348955648> {amt}!")

        with open("accounts.json", "w") as f:
          json.dump(bals, f, indent=4)

emojis = ["💎", "🔔", "🗑", "🧲", "🔒", "🔵"]

roles = ["Crewmate", "Crewmate", "Crewmate", "Crewmate", "Crewmate", "Crewmate", "Crewmate", "Crewmate", "Impostor", "Impostor"]



all_tasks = ["Electrical: Download Data", "Balcony: Download Weather Patterns", "Medbay: Scan", "Medbay: Inspect Sample", "Communications: Reboot WiFi", "Main Hall: Decontaminate", "Admin: Swipe Card", "Main Hall: Develop Photos"]


class Testing(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.is_owner()
  async def test(self, ctx):
    #await grantxp(ctx)
    await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
    try:
      reaction, user = await self.client.wait_for("reaction_add", check=lambda reaction, user:user == ctx.author and reaction.emoji in ["<:impostor:774673531786625024>"], timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send(f"I don't know where you went, so {user.mention} didn't recieve a gift")
    else:
      if reaction.emoji == "<:impostor:774673531786625024>":
        await ctx.send("ok")

    
  @commands.command()
  @commands.is_owner()
  async def meeting(self, ctx):
    embedSix = discord.Embed(
      title="Emergency Meeting",
      colour=discord.Colour.blue()
      )
    embedSix.set_thumbnail(url="https://i.pinimg.com/originals/34/de/33/34de331902fcdc9db86248e1b4ff47c2.png")
    embedSix.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedSix)
    embedSixB = discord.Embed(
      title="Emergency Meeting",
      description="Why?\nWho?",
      colour=discord.Colour.blue()
      )
    embedSixB.set_thumbnail(url="https://i.pinimg.com/originals/34/de/33/34de331902fcdc9db86248e1b4ff47c2.png")
    embedSixB.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    

  @commands.command()
  @commands.is_owner()
  async def fans(self, ctx):
    code = [random.choice(emojis), random.choice(emojis), random.choice(emojis), random.choice(emojis)]
    await ctx.message.delete()
    strt = await ctx.send("[TIP] The code will be removed after 10 seconds!")
    await asyncio.sleep(5)
    await strt.delete()
    embedFans = discord.Embed(
      title="Code:",
      description=f"{code[0]}{code[1]}{code[2]}{code[3]}",
      colour=discord.Colour.red()
    )
    embedFans.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    embedAsk = discord.Embed(
      title="Please insert code:",
      description="[TIP] React to the symbol (in order) to type in the code!",
      colour=discord.Colour.red()
    )
    embedAsk.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    fan = await ctx.send(embed=embedFans)
    await asyncio.sleep(10)
    await fan.delete()
    count = 15
    fan = await ctx.send(f"Walk to the other Ventilation panel")
    await asyncio.sleep(3)
    for sus in range(1, 16):
      await fan.edit(content=f"Walking to the other Ventilation Panel ({count} seconds left)")
      count = count - 1
      await asyncio.sleep(1)
    await fan.delete()
    fan = await ctx.send(embed=embedAsk)
    for emoji in emojis:
      await fan.add_reaction(emoji)
    await ctx.wait_for_reaction(code[0], fan)




  @commands.command()
  #@commands.is_owner()
  async def play(self, ctx):
    with open("testers.json", "r") as f:
      pp = json.load(f)
      if str(ctx.author.id) not in pp:
        await ctx.send("I'm sorry, but you need to be a Beta Tester to access this command!")
    await ctx.message.delete()
    role = random.choice(roles)
    count = 5
    g = await ctx.send(f"Starting in {count}")
    for i in range(1,6):
      await g.edit(content=f"Starting in {count}")
      count = count - 1
      await asyncio.sleep(1)
    await g.delete()
    await asyncio.sleep(1)
    embedShh = discord.Embed(
      colour=discord.Colour.red()
    )
    embedShh.set_image(url="https://wonder-day.com/wp-content/uploads/2020/10/wonder-day-among-us-14.png")
    g = await ctx.send(embed=embedShh)
    await asyncio.sleep(3)
    await g.delete()
    if role[0].lower() == "c":
      embedCrew = discord.Embed(
        title="Crewmate",
        description="There are **2** Impostors Among Us...",
        colour=discord.Colour.blue()
      )
      c = await ctx.author.send(embed=embedCrew)
      await asyncio.sleep(5)
      await c.delete()
      c = await ctx.author.send(f"{ctx.author.mention}\nYou are a Crewmate!\nComplete Tasks or Vote out Impostors to win!")
      await asyncio.sleep(5)
      await c.delete()
      random.shuffle(all_tasks)
      embedTasks = discord.Embed(
        title="Tasks",
        description=f"Complete these to win!\n{all_tasks[0]}\n{all_tasks[1]}\n{all_tasks[2]}\n{all_tasks[3]}",
      colour=discord.Colour.blue()
      )
      c = await ctx.author.send(embed=embedTasks)
    elif role[0].lower() == "i":
      embedImp = discord.Embed(
        title="Impostor",
        colour=discord.Colour.red()
      )
      i = await ctx.author.send(embed=embedImp)
      await asyncio.sleep(5)
      await i.delete()
      i = await ctx.author.send(f"{ctx.author.mention}\nYou are an Impostor!\nUse your Impostor Commands to defeat the Crewmates!")
      await asyncio.sleep(5)
      await i.delete()
      em = discord.Embed(
        title="Impostor Commands",
        colour = discord.Colour.red()
      )
      em.add_field(name="$kill", value="Kill a crewmate", inline=True)
      em.add_field(name="$vent", value="Vent away from a crime scene, so you don't get caught", inline=True)
      em.add_field(name="$sabotage", value="Sabotage something to make it harder for the crewmates", inline=True)
      i = await ctx.author.send(embed=em)
      await asyncio.sleep(10)
      await i.delete()
    else:
      await ctx.author.send("I have no idea what went wrong here, if this happens again, join my support server!\nhttps://discord.gg/Sun4mtFjwE")

  """@commands.command()
  @commands.is_owner()
  async def temp(self, ctx):
    await ctx.message.delete()
    embed = discord.Embed(
      title="Partners",
      description="If you wish to become a partner of the bot, please DM Baz#2641",
      colour=discord.Colour.red(),
      url="https://bazbots.github.io/"
    )
    embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    embed.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
    embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
    await ctx.send(embed=embed)"""

def setup(client):
  client.add_cog(Testing(client))