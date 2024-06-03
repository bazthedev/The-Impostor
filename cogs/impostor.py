import discord
from discord.ext import commands
from colorama import Fore
import random
import asyncio
import json
from func import spon

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

deaths = ["brutally murdered them", "ejected them into space", "no scoped them for a 180 headshot", "oofed them", "tripping them over and them making them fall into some conveniently placed lava", "`demonitised` them... I'm talking to you <@818571042267594755>!", "repeatedly stabbed them in the back", "hacked all of their `vbucks`", "summoned the enderdragon", "just killed them, this was **Shot on iPhone**"]

vents = ["to Polus", "to Mira HQ", "into the Nether...?", "to top.gg where they vote for The Impostor 😎😎😎😎", "to the airship map :O (that we have finally got)"]

places = ["Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

sabotages = ["Reactor", "Oxygen", "Lights", "Communications"]

suss = ["      ⠀⠀           ⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀\n ⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀\n⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀\n⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀\n⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀\n⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀\n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀\n⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀\n⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀\n⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀", "⠀⠀⡯⡯⡾⠝⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⠘⡮⣣⠪⠢⡑⡌\n⠀⠀⠀⠟⠝⠈⠀⠀⠀⠡⠀⠠⢈⠠⢐⢠⢂⢔⣐⢄⡂⢔⠀⡁⢉⠸⢨⢑⠕⡌\n⠀⠀⡀⠁⠀⠀⠀⡀⢂⠡⠈⡔⣕⢮⣳⢯⣿⣻⣟⣯⣯⢷⣫⣆⡂⠀⠀⠑⡌\n⢀⠠⠐⠈⠀⢀⢂⠢⡂⠕⡁⣝⢮⣳⢽⡽⣾⣻⣿⣯⡯⣟⣞⢾⢜⢆⠀⡀⠀⠪⣬\n⠂⠀⠀⢀⢂⢪⠨⢂⠥⣺⡪⣗⢗⣽⢽⡯⣿⣽⣷⢿⡽⡾⡽⣝⢎⠀⠀⠀⢡\n⣿⠀⠀⠀⢂⠢⢂⢥⢱⡹⣪⢞⡵⣻⡪⡯⡯⣟⡾⣿⣻⡽⣯⡻⣪⠧⠑⠀⠁⢐\n⣿⠀⠀⠀⠢⢑⠠⠑⠕⡝⡎⡗⡝⡎⣞⢽⡹⣕⢯⢻⠹⡹⢚⠝⡷⡽⡨⠀⠀⢔\n⣿⡯⠀⢈⠈⢄⠂⠂⠐⠀⠌⠠⢑⠱⡱⡱⡑⢔⠁⠀⡀⠐⠐⠐⡡⡹⣪⠀⠀⢘\n⣿⣽⠀⡀⡊⠀⠐⠨⠈⡁⠂⢈⠠⡱⡽⣷⡑⠁⠠⠑⠀⢉⢇⣤⢘⣪⢽⠀⢌⢎\n⣿⢾⠀⢌⠌⠀⡁⠢⠂⠐⡀⠀⢀⢳⢽⣽⡺⣨⢄⣑⢉⢃⢭⡲⣕⡭⣹⠠⢐⢗\n⣿⡗⠀⠢⠡⡱⡸⣔⢵⢱⢸⠈⠀⡪⣳⣳⢹⢜⡵⣱⢱⡱⣳⡹⣵⣻⢔⢅⢬⡷\n⣷⡇⡂⠡⡑⢕⢕⠕⡑⠡⢂⢊⢐⢕⡝⡮⡧⡳⣝⢴⡐⣁⠃⡫⡒⣕⢏⡮⣷⡟\n⣷⣻⣅⠑⢌⠢⠁⢐⠠⠑⡐⠐⠌⡪⠮⡫⠪⡪⡪⣺⢸⠰⠡⠠⠐⢱⠨⡪⡪⡰\n⣯⢷⣟⣇⡂⡂⡌⡀⠀⠁⡂⠅⠂⠀⡑⡄⢇⠇⢝⡨⡠⡁⢐⠠⢀⢪⡐⡜⡪⡊\n⣿⢽⡾⢹⡄⠕⡅⢇⠂⠑⣴⡬⣬⣬⣆⢮⣦⣷⣵⣷⡗⢃⢮⠱⡸⢰⢱⢸⢨⢌\n⣯⢯⣟⠸⣳⡅⠜⠔⡌⡐⠈⠻⠟⣿⢿⣿⣿⠿⡻⣃⠢⣱⡳⡱⡩⢢⠣⡃⠢⠁\n⡯⣟⣞⡇⡿⣽⡪⡘⡰⠨⢐⢀⠢⢢⢄⢤⣰⠼⡾⢕⢕⡵⣝⠎⢌⢪⠪⡘⡌⠀\n⡯⣳⠯⠚⢊⠡⡂⢂⠨⠊⠔⡑⠬⡸⣘⢬⢪⣪⡺⡼⣕⢯⢞⢕⢝⠎⢻⢼⣀⠀\n⠁⡂⠔⡁⡢⠣⢀⠢⠀⠅⠱⡐⡱⡘⡔⡕⡕⣲⡹⣎⡮⡏⡑⢜⢼⡱⢩⣗⣯⣟\n⢀⢂⢑⠀⡂⡃⠅⠊⢄⢑⠠⠑⢕⢕⢝⢮⢺⢕⢟⢮⢊⢢⢱⢄⠃⣇⣞⢞⣞⢾\n⢀⠢⡑⡀⢂⢊⠠⠁⡂⡐⠀⠅⡈⠪⠪⠪⠣⠫⠑⡁⢔⠕⣜⣜⢦⡰⡎⡯⡾⡽", """░█░█░█░█░█▀▀░█▀█                
░█▄█░█▀█░█▀▀░█░█                
░▀░▀░▀░▀░▀▀▀░▀░▀                
░▀█▀░█░█░█▀▀                    
░░█░░█▀█░█▀▀                    
░░▀░░▀░▀░▀▀▀                    
░▀█▀░█▄█░█▀█░█▀█░█▀▀░▀█▀░█▀█░█▀▄
░░█░░█░█░█▀▀░█░█░▀▀█░░█░░█░█░█▀▄
░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀
░▀█▀░█▀▀                        
░░█░░▀▀█                        
░▀▀▀░▀▀▀                        
░█▀▀░█░█░█▀▀                    
░▀▀█░█░█░▀▀█                    
░▀▀▀░▀▀▀░▀▀▀""",
"""
⠛⠛⣿⣿⣿⣿⣿⡷⢶⣦⣶⣶⣤⣤⣤⣀⠀⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⠀⠀⠉⠉⠉⠙⠻⣿⣿⠿⠿⠛⠛⠛⠻⣿⣿⣇⠀
⠀⠀⢤⣀⣀⣀⠀⠀⢸⣷⡄⠀⣁⣀⣤⣴⣿⣿⣿⣆
⠀⠀⠀⠀⠹⠏⠀⠀⠀⣿⣧⠀⠹⣿⣿⣿⣿⣿⡿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⠇⢀⣼⣿⣿⠛⢯⡿⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠴⢿⢿⣿⡿⠷⠀⣿⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣷⣶⣶⣤⣤⣤⣤⣤⣶⣦⠃⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⠟⠁
"""]


how = ["bruh did you kermit the frog or something?", "ok you are die", "do you need help or something?", "please don't"]

you = ["ha ha lol you can't kill me! im the impostor!", "you really thought", "you fool i"]


class Impostor(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def eject(self, ctx, name : commands.MemberConverter, role):
    if await banned(ctx):
      return
    if role[0].lower() == "c":
      embedC = discord.Embed(
        description = f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 <:red_sus:835814014290362379> 。 . 　　 • 　　　　•\n　ﾟ　　 {name.name} was not The Impostor.　 。　\n'　　。 . 　•　  1 Impostor remains 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •"
      )
      embedC.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedC)   
    elif role[0].lower() == "i":
      embedI = discord.Embed(
        description=f". 　　　。　　　　•　 　ﾟ　　。 　　.\n　.　　　 　　.　　　　　。　　 。　. \n.　　 。　　　　　 <:red_sus:835814014290362379> 。 . 　　 • 　　　　•\n　ﾟ　　 {name.name} was The Impostor.　 。　\n'　　。 . 　•　  0 Impostors remain 　 　　。\n。 . 　　 •　　　.　　　. ,　　　　。 . 　　 •"
      )
      embedI.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedI)
    else:
      await ctx.send("Please provide a valid role like \"crew\" or \"imp\"")
    await ctx.message.delete()

  @eject.error
  async def no_role(self, ctx, error):
    if await banned(ctx):
      return
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(f"{error}")
      print(Fore.GREEN + f"Error: {error}")
      await ctx.message.delete()

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def sus(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Sussy baka!")
    await ctx.send(random.choice(suss))
    await spon(ctx)
    await ctx.message.delete()

  
  @commands.command(aliases=["murder"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def kill(self, ctx, *, username  : commands.MemberConverter):
    if await banned(ctx):
      return
    
    embedOne = discord.Embed(
        description=f"{username.mention} has been killed by {ctx.author.mention} who {random.choice(deaths)}!",
        colour = discord.Colour.red()
    )
    embedOne.set_thumbnail(url="https://preview.redd.it/rnj1si3kzwn51.png?width=720&format=png&auto=webp&s=6e7243bb5c2d8f27921313b0f8ef27617523d604")
    embedOne.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedOne)
    await ctx.message.delete()

  @kill.error
  async def no_name(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      embedMAR = discord.Embed(
        title="Hmm...",
        description=f"Something's missing...\n\n{error}",
        colour=discord.Colour.red()
      )
      embedMAR.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedMAR)


  @commands.command()
  @commands.is_owner()
  async def alldeaths(self, ctx):
    await ctx.send(f"Deaths:\n{deaths}")
    await ctx.message.delete()
  
  @commands.command()
  @commands.is_owner()
  async def allvents(self, ctx):
    await ctx.send(f"All possible outcomes of $vent:\n{vents}\n\n{places}")
    await ctx.message.delete()
  
  @commands.command(aliases=["v"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def vent(self, ctx):
    if await banned(ctx):
      return
    embedThree = discord.Embed(description=f"{ctx.author.mention} goes to {random.choice(places)} and vents to {random.choice(vents)}",
      colour = discord.Colour.red()
    )
    embedThree.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/d/db/Vent.png/revision/latest/top-crop/width/360/height/360?cb=20210220170224")
    embedThree.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedThree)
    await ctx.message.delete()

  @commands.command()
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def sabotage(self, ctx, channel : commands.TextChannelConverter, sab=random.choice(sabotages)):
       if await banned(ctx):
        return
       await ctx.message.add_reaction(emoji="<:sabotage:850329714076680214>")
       if sab[0].lower() == "c":
         coms = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await coms.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await coms.edit(content="Please wait...")
           await asyncio.sleep(2)
         await coms.edit(content="Communtications Sabotaged in {}".format(channel))
         ctx.channel.permission.update(send_messages=False)
         await asyncio.sleep(10)
         await coms.delete()
         ctx.channel.permission.update(send_messages=True)
       elif sab[0].lower() == "r":
         countdown = 30
         reactor = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1,5):
           await reactor.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await reactor.edit(content="Please Wait...")
           await asyncio.sleep(2)
         for i in range(1, 31):
           await reactor.edit(content=f"Reactor Meltdown in {countdown}!")
           await asyncio.sleep(1)
           countdown = countdown - 1
           if countdown == 0:
             await reactor.edit(content="Reactor has Meltdown!\nAll crewmates have been eliminated")
           await asyncio.sleep(10)
           await reactor.delete()
       elif sab[0].lower() == "l":
         await vibe_check(ctx, "Who turned out the lights?")
         lights = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await lights.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await lights.edit(content="Please wait...")
           await asyncio.sleep(2)
         await lights.edit(content="Lights Pannel\n\n████████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n████")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n███")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n██")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\n█")
         await asyncio.sleep(1)
         await lights.edit(content="Lights Pannel\n\nOffline!")
         await asyncio.sleep(2)
         await lights.edit(content="Lights shut down in {}\nNo one can see messages".format(channel))
         await ctx.channel.permission.update(read_message_history=False)
         await asyncio.sleep(10)
         await lights.delete()
         await ctx.channel.permssion.update(read_message_history=True)
       elif sab[0].lower() == "o":
         countdowno = 30
         oxygen = await ctx.send("Please Wait...")
         await asyncio.sleep(2)
         for i in range(1, 5):
           await oxygen.edit(content="Beginning Sabotage...")
           await asyncio.sleep(2)
           await oxygen.edit(content="Please wait...")
           await asyncio.sleep(2)
         for i in range(1, 31):
           await oxygen.edit(content=f"Oxygen Depleteing in {countdowno}")
           await asyncio.sleep(1)
           countdowno = countdowno - 1
         await oxygen.edit(content="Oxygen has been Depleted!\nAll crewmates have been eliminated!")
         await asyncio.sleep(10)
         await oxygen.delete()
       else:
         await ctx.send(f"{ctx.author.mention}\nThis sabotage does not exist!")
       await ctx.message.delete()

  @sabotage.error
  async def sab_error(self, ctx, error):
    if await banned(ctx):
      return
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(
         title="Sabotage Menu", description=":radioactive: Reactor\n:zap: Lights\n:satellite: Communications\n:regional_indicator_o: Oxygen\n\nType $sabotage (sabotage) next time",
         colour=discord.Colour.red()
         )
      embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      embed.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/f/f3/Sabotage.png/revision/latest/top-crop/width/360/height/360?cb=20210220165836")
      await ctx.send(embed=embed)
      await ctx.message.delete()
      

  
def setup(client):
  client.add_cog(Impostor(client))