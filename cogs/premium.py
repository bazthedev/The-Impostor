import discord
from discord.ext import commands
import json
import asyncio
import random
import time
import string

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


crewmates = []
impostors = [737414795896160297, 513283671353196585]
hackers = [730043363671277638, 818571042267594755, 720195126793863200, 819608297447489606, 818461529921159229]


vents = ["to Polus", "to Mira HQ", "into the Nether...?", "to top.gg where they vote for The Impostor 😎😎😎😎", "to the airship map :O (that we have finally got)"]

places = ["Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

wtiiss = ["https://imgur.com/bmit9SE", "https://i.ytimg.com/vi/0bZ0hkiIKt0/maxresdefault.jpg", "https://www.voicy.network/Content/Clips/Images/2c730b2a-ba62-4aa5-88ec-600dfc47ed2c-small.jfif", "https://static.planetminecraft.com/files/image/minecraft/texture-pack/2021/153/13949499-suscraftbanner_l.jpg", "https://i.ytimg.com/vi/arvcoC4uMpY/mqdefault.jpg", "http://images7.memedroid.com/images/UPLOADED703/60396de11b5aa.jpeg", "https://i.chzbgr.com/full/9559827456/h92AEFD24/animal-imposter-but-win-just-kept-lying-and-kept-working", "https://wompampsupport.azureedge.net/fetchimage?siteId=7682&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fcdn.ebaumsworld.com%2F2020%2F09%2F22%2F055653%2F86396220%2Famong-us-memes-and-jokes-38.jpg", "https://i.pinimg.com/736x/e6/b6/06/e6b606eb91c6fcab993888bc32683f5c.jpg", "https://64.media.tumblr.com/9c1156897ad4f1d16923f5097fa86ac7/511370e73e319827-83/s1280x1920/925c680c3ed072d61167432db8c24c95d2b241f3.jpg", "http://images3.memedroid.com/images/UPLOADED13/605a31c2b4fc2.jpeg", "https://i.pinimg.com/originals/12/13/36/12133616909280156f37de72fe978653.jpg", "https://preview.redd.it/x8ctwh8qlgu51.jpg?width=960&crop=smart&auto=webp&s=32f4402c31647ff595f845a29610270e61ae0080", "https://cdn.ebaumsworld.com/2020/09/22/055926/86396228/among-us-memes-and-jokes-47.jpg", "https://i.imgflip.com/54q4p7.jpg"]


class Premium(commands.Cog):
  
  def __init__(self, client):
    self.client = client


   
      
  @commands.command(aliases=["patron"])
  async def patreon(self, ctx):
    embed = discord.Embed(
      title="<a:rainbow:839861408581419058> Patreon - The Impostor <a:rainbow:839861408581419058>",
      url="https://www.patreon.com/theimpostor",
      colour=discord.Colour.red(),
      description="Click the link above to visit the official Patreon site for the bot!\nYou can type `$plan (hacker/crewmate/impostor)` to view all current plans!"
    )
    embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    embed.set_thumbnail(url="https://cdn.vox-cdn.com/thumbor/ynrXTDCVJZ7NI1OV8q2n6mjqb8I=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/9833961/patreon.jpg")
    await ctx.send(embed=embed)

  
  

  
  @commands.command(aliases=["plan"])
  async def plans(self, ctx, plan):
    if plan[0].lower() == "i":
      embedI = discord.Embed(
        title="<:red_sus:835814014290362379> Impostor Plan <:red_sus:835814014290362379>",
        description="**Price: £5.00/Month**\n- All perks from the Crewmate Tier\n- Exclusive commands\n- Special Role\n- Access to the Giveaway Section in the Support Server\n- Access to special polls\n10000 Beans <:bean:908267086348955648>",
        url="https://www.patreon.com/theimpostor",
        colour=discord.Colour.red()
      )
      embedI.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedI)
    elif plan[0].lower() == "h":
      embedH = discord.Embed(
        title="<:purple:839879572631453696> Hacker Plan <:purple:839879572631453696>",
        description="**Price: £7.50/Month**\n- All Features of Impostor tier\n- Early Access to all commands\n- Special Role\n- Access to special polls\n- Work-in-progress updates (delivered by e-mail)\n100000 Beans <:bean:908267086348955648>",
        url="https://www.patreon.com/theimpostor",
        colour=discord.Colour.purple()
      )
      embedH.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedH)
    elif plan[0].lower() == "c":
      embedC = discord.Embed(
        title="<:cyan:839879549705388043> Crewmate Plan <:cyan:839879549705388043>",
        description="**Price: £2.50/Month**\n- A special role & chat\n- Certain Exclusive Commands\n1000 Beans <:bean:908267086348955648>",
        url="https://www.patreon.com/theimpostor",
        colour=discord.Colour.blue()
      )
      embedC.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedC)
    else:
      await ctx.send(f"{ctx.author.mention}\nThe plan you have provided ({plan}) does not exist!")

  @plans.error
  async def no_plan(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embedPl = discord.Embed(
        title="Current Plans:",
        url="https://www.patreon.com/join/TheImpostor/checkout",
        colour=discord.Colour.red()
      )
      embedPl.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
      embedPl.add_field(name="<:cyan:839879549705388043> Crewmate Plan <:cyan:839879549705388043>", value="**Features:**\n\n\n- A special role & chat\n- Certain Exclusive Commands\n1000 Beans <:bean:908267086348955648>\n\n**Price: £2.50/Month**", inline=True)
      embedPl.add_field(name="<:red_sus:835814014290362379> Impostor Plan <:red_sus:835814014290362379>", value="**Features:**\n\n- All perks from the Crewmate Tier\n- Exclusive commands\n- Special Role\n- Access to the Giveaway Section in the Support Server\n10000 Beans <:bean:908267086348955648>\n\n**Price: £5.00/Month**", inline=True)
      embedPl.add_field(name="<:purple:839879572631453696> Hacker Plan <:purple:839879572631453696>", value="**Features**\n\n- All Features of Impostor tier\n- Early Access to all commands\n- Special Role\n- Access to special polls\n- Work-in-progress updates (delivered by e-mail)\n100000 Beans <:bean:908267086348955648>\n\n**Price: £7.50/Month**", inline=True)
      embedPl.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedPl)


  @commands.command()
  async def flex(self, ctx):
    # Hacker Only
    with open("premium.json", "r") as f:
      plus = json.load(f)
      if plus[str(ctx.author.id)] != "Hacker":
        await ctx.send("You must have Hacker Tier to use this command")
        return
    await ctx.send(f"<:purple:839879572631453696><:purple:839879572631453696><:purple:839879572631453696>{ctx.author.mention} is in hacker tier <:purple:839879572631453696><:purple:839879572631453696><:purple:839879572631453696>")

  @commands.command()
  @commands.is_owner()
  async def update(self, ctx):
    with open("premium.json", "r") as f:
      plus = json.load(f)
      if plus[str(ctx.author.id)] != "Hacker":
        await ctx.send("You must have Hacker Tier to use this command")
        return
    embedWIP = discord.Embed(
      title="Hello there Hacker!\nHere is what we are planning to add soon!\nWork in Progress:",
      description="<:purple:839879572631453696> Badges\n<:purple:839879572631453696> $trickortreat\n<:purple:839879572631453696>",
      colour=discord.Colour.purple()
    )
    embedWIP.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.author.send(embed=embedWIP)

  @commands.command(alisases=["engine", "fuelengine"])
  async def fuel(self, ctx):
    # Hacker Only
    with open("premium.json", "r") as f:
      plus = json.load(f)
      if plus[str(ctx.author.id)] != "Hacker":
        await ctx.send("You must have Hacker Tier to use this command")
        return  
    eng = await ctx.send("```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│________│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(3)
    await eng.edit(content="Upper Engine Fuelled!")
    await asyncio.sleep(3)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│_________│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│		│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(1)
    await eng.edit(content="```\n_________\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│\n│████████│```")
    await asyncio.sleep(3)
    await eng.edit(content="Lower Engine Fuelled!")
    await asyncio.sleep(5)
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
    after_benz = bals[str(ctx.author.id)]["benz"] + amt
    bals[str(ctx.author.id)]["benz"] = after_benz
    with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
    await eng.edit(content=f"Task Complete - You recieved <:bean:908267086348955648> {amt}!")
    await ctx.message.delete()

# │
# █

  @commands.command(aliases=["photos", "photo"])
  async def develop(self, ctx):
    with open("premium.json", "r") as f:
      plus = json.load(f)
      if plus[str(ctx.author.id)] != "Crewmate" and plus[str(ctx.author.id)] != "Impostor" and plus[str(ctx.author.id)] != "Hacker":
        await ctx.send("You must have Crewmate Tier or above to use this command")
        return
    await vibe_check(ctx, "Photographer!")
    count = 15
    embedPhotos = discord.Embed(
      title="Develop Photos",
      colour=discord.Colour.red()
    )
    embedPhotos.set_image(url="https://static.wikia.nocookie.net/among-us-wiki/images/e/ec/Develop_Photos.png/revision/latest?cb=20210409205839")
    embedPhotos.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    embedPDone = discord.Embed(
      title="Development Complete!",
      colour=discord.Colour.red()
    )
    embedPDone.set_image(url="https://static.wikia.nocookie.net/among-us-wiki/images/2/2c/Develop_Photos_stage_2.png/revision/latest?cb=20210409210011")
    embedPDone.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    dp = await ctx.send(embed=embedPhotos)
    await asyncio.sleep(5)
    await dp.delete()
    dp = await ctx.send("Beginning Photo Development...")
    await asyncio.sleep(2)
    for sus in range(1, 16):
      await dp.edit(content=f"Developing...\nCome back in `{count} seconds`")
      count = count - 1
      await asyncio.sleep(1)
    await dp.edit(content="Photos have been developed!")
    await asyncio.sleep(5)
    await dp.delete()
    dp = await ctx.send(embed=embedPDone)
    await ctx.message.delete()


  @commands.command(aliases=["wtiis", "memes"])
  async def meme(self, ctx):
    await vibe_check(ctx, "epok fun meme")
    with open("premium.json", "r") as f:
      plus = json.load(f)
      if plus[str(ctx.author.id)] != "Impostor" and plus[str(ctx.author.id)] != "Hacker":
        await ctx.send("You must have Impostor Tier or above to use this command")
        return
    embedMeme = discord.Embed()
    embedMeme.set_image(url=random.choice(wtiiss))
    await ctx.send(embed=embedMeme)
    await ctx.message.delete()

  @commands.command(aliases=["get"])
  @commands.is_owner()
  async def redeem(self, ctx, *, code):
    with open("premium.json", "r") as f:
      isin = json.load(f)
      if isin[str(ctx.author.id)] == "Hacker":
        await ctx.send(f"You already have {isin[str(ctx.author.id)]} Tier")
        return
      #elif str(ctx.author.id) not in isin:
      with open("codes.json", "r") as f:
          codes = json.load(f)
          if str(code) in codes:
            isin[str(ctx.author.id)] = codes[str(code)]["Tier"]
            channel = self.client.get_channel(838465155582394390)
            embedC = discord.Embed(title="Console", description=f"{ctx.author} has redeemed {code}")
            await channel.send(embed=embedC)
          elif str(code) not in codes:
            await ctx.send("The code provided does not exist")
            return
          if codes[str(code)]["once"] == True:
              codes.pop(str(code))
              with open("codes.json", "w") as f:
                json.dump(codes, f, indent=4)
          with open("premium.json", "w") as f:
            json.dump(isin, f, indent=4)
      if isin[str(ctx.author.id)] == "Crewmate":
        embed = discord.Embed(
          title="Welcome to Crewmate Tier!",
          colour=discord.Colour.blue()
        )
        embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/5/51/Cyan_old_design.png/revision/latest/scale-to-width-down/250?cb=20201013061549")
        embed.add_field(name="Benefits:", value="- A special role & chat\n- Certain Exclusive Commands\n1000 Beans <:bean:908267086348955648>", inline=True)
        await ctx.send(embed=embed)
      elif isin[str(ctx.author.id)] == "Impostor":
        embed = discord.Embed(
          title="Welcome to Impostor Tier!",
          colour=discord.Colour.red()
        )
        embed.add_field(name="Benefits:", value="- All perks from the Crewmate Tier\n- Exclusive commands\n- Special Role\n- Access to the Giveaway Section in the Support Server\n- Access to special polls\n10000 Beans <:bean:908267086348955648>", inline=True)
        embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/c/c7/Red_old_design.png/revision/latest/scale-to-width-down/250?cb=20210307225556")
        await ctx.send(embed=embed)
      elif isin[str(ctx.author.id)] == "Hacker":
        embed = discord.Embed(
          title="Welcome to Hacker Tier!",
          colour=discord.Colour.purple()
        )
        embed.add_field(name="Benefits:", value="- All Features of Impostor tier\n- Early Access to all commands\n- Special Role\n- Access to special polls\n- Work-in-progress updates (delivered by e-mail)\n100000 Beans <:bean:908267086348955648>", inline=True)
        embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/9/91/Purple_old_design.png/revision/latest/scale-to-width-down/250?cb=20201013061517")
        await ctx.send(embed=embed)
    await ctx.message.delete()
  
  @redeem.error
  async def nocode(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("You need to provide a code!")


"""
# Crewmate +
with open("premium.json", "r") as f:
  users = json.load(f)
  if ctx.author.id not in users:
    await ctx.send("You must have at least crewmate tier to use this command!")
    return "403 Forbidden - Not in crewmate tier +"
# Impostor +
with open("premium.json", "r") as f:
  users = json.load(f)
  if ctx.author.id not in users or users[ctx.author.id] == "Crewmate":
    await ctx.send("You must have at least impostor tier to use this command!")
    return "403 Forbidden - Not in impostor tier +"
# Hacker Only
with open("premium.json", "r") as f:
  users = json.load(f)
  if ctx.author.id not in users:
    await ctx.send("You must have at least crewmate tier to use this command!")
    return "403 Forbidden - Not in crewmate tier +"
if ctx.author.id not in hackers:
  await ctx.send("You must have Hacker Tier to use this command")
  return
"""
      




def setup(client):
  client.add_cog(Premium(client))