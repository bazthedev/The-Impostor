import discord
from discord.ext import commands
from colorama import Fore
import random
import dbl
import asyncio
import datetime, time
import json
from func import spon
from main import uses

cms = ["Hold your horses!", "Stop in the name of the law!", "Woah there buckaroo!", "You are sus", "Stop before we eject you"]

cnf = ["What are you talking about?", "You are speaking jibberish", "Can I help you?"]

start = time.time()

urls = ["https://discord.bots.gg/bots/759436027529265172", "https://top.gg/bot/759436027529265172/vote", "https://discordbotlist.com/bots/the-impostor", "https://discords.com/bots/bot/759436027529265172"]

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

class Basic(commands.Cog):

  def __init__(self, client):
    self.client = client   


  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandNotFound):
      print(error)
    if isinstance(error, commands.CommandOnCooldown):
      if error.retry_after >= 60:
        x = int(round(error.retry_after) / 60)
        timeout = f"{x} minutes"
        if x >= 60:
          x = int(round(x) / 60)
          timeout = f"{x} hours"
          if x >= 24:
            x = int(round(x) / 24)
            timeout = f"{x} days"
      else:
        timeout = f"{int(round(error.retry_after))} seconds"
      embedCooldown = discord.Embed(
        title="Command on Cooldown!",
        description=f"{random.choice(cms)}\nYou can try this command again in **{timeout}**!",
        colour=discord.Colour.red()
        )
      embedCooldown.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      await ctx.send(embed=embedCooldown)
      
      print(error)
    if isinstance(error, commands.MissingPermissions):
        embedMP = discord.Embed(
          title="Invalid Permissions!",
          description="```diff\n- {}\n```".format(error),
          colour=discord.Colour.red()
          )
        embedMP.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        await ctx.author.send(embed=embedMP)

    if isinstance(error, commands.BotMissingPermissions):
        embedBMP = discord.Embed(
          title="Missing Permissions!",
          description=f"{ctx.author.mention}\nI do not have permission to perform this action!\n```diff\n{error}\n```",
          colour=discord.Colour.red()
          )
        embedBMP.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        await ctx.author.send(embed=embedBMP)
    if isinstance(error, commands.NotOwner):
      await ctx.send("This command will not run because of 1 of 3 reasons:\n- This command is still in development\n- This command has been disabled\n- This command is reserved for the bot owner only")
    print(error)
    await spon(ctx)
    
        
 
  @commands.Cog.listener()
  async def on_reaction_add(self, reaction, user):
    pass

  @commands.Cog.listener()
  async def on_reaction_remove(self, reaction, user):
    pass
    #print(f"{user.display_name} unreacted with {reaction.emoji}")
  
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    pass

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    pass

  @commands.command()
  async def help(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "Welcome to the impostor!")
    embedTwo = discord.Embed(
        title="Help",
        description="Join my support server here:\nhttps://discord.gg/Sun4mtFjwE\n\nUse the prefix or `@The Impostor`", # `$` 
        colour=discord.Colour.red()
      )
    embedTwo.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
    embedTwo.add_field(name="Informative Commands",value="help\ninfo\nversion\nfeedback\ncreator\nping\nvote (site)\nuptime\nbadges (user)", inline=True)
    embedTwo.add_field(name="Impostor Commands", value="eject {user} {role}\nsus\nkill {username}\nsabotage\nvent", inline=True)
    embedTwo.add_field(name="Crewmate Commands", value="scan\ndownload\nweather\ninspect\nshower\nswipe\nreboot\nlaunch {doorlogs}\nreport")
    embedTwo.add_field(name="Bean Commands", value="All tasks now give you a random number of beans\nbeans\ndaily\nshop\ninventory\nslots", inline=True)
    #embedTwo.add_field(name="Halloween Commands", value="trickortreat\nhauntedhouse", inline=True)
    #embedTwo.add_field(name="Christmas Commands", value="gift {user}\ncracker {user}", inline=True)
    #embedTwo.add_field(name="Birthday Commands", value="cake\nopen", inline=True)
    #embedTwo.add_field(name="Partners", value="partners\nscrappie | https://bazbots.github.io/The-Impostor/scrappie\nnyrone | https://nyrone.net/")
    embedTwo.add_field(name="Special Commands", value="6", inline=True)
    embedTwo.add_field(name="Patreon Commands", value="patreon\nplans\nredeem {code}", inline=True)
    embedTwo.add_field(name="Crewmate Plan commands:", value="develop", inline=True)
    embedTwo.add_field(name="Impostor Plan Commands:", value="All Crewmate Commands\nmeme", inline=True)
    embedTwo.add_field(name="Hacker Plan Commands", value="All Impostor Commands\nfuel\nflex\n", inline=True)
    embedTwo.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
    embedTwo.set_footer(text=f"Invoked by {ctx.author}\n© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedTwo)
    await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
    



  @commands.command(aliases=["information", "i", "about", "invite", "website", "server", "github"])
  async def info(self, ctx):
    embedTen = discord.Embed(
      title="Useful Bot Links",
      colour=discord.Colour.red()
      )
    embedTen.set_image(url="https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png")
    embedTen.add_field(name="Invite Link", value="https://discord.com/api/oauth2/authorize?client_id=759436027529265172&permissions=8&redirect_uri=https%3A%2F%2Fbazbots.github.io%2FThe-Impostor%2Fthanks&response_type=code&scope=identify%20bot%20email", inline=True)
    embedTen.add_field(name="Website", value="https://bazbots.github.io/The-Impostor", inline=True)
    embedTen.add_field(name="Patreon", value="https://www.patreon.com/theimpostor", inline=True)
    embedTen.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
    embedTen.set_footer(text=f"Invoked by {ctx.author}\n© Baz - The Impostor - Among Us bot for Discord")
    embedTen.add_field(name="Support Server Link:", value="https://discord.gg/Sun4mtFjwE", inline=True)
    embedTen.add_field(name="Top.gg Voting Link:", value="https://top.gg/bot/759436027529265172/vote", inline=True)
    embedTen.add_field(name="DiscordBotList.com Voting Link:", value="https://discordbotlist.com/bots/the-impostor", inline=True)
    embedTen.add_field(name="Discord.Bots.gg Voting Link:", value="https://discord.bots.gg/bots/759436027529265172", inline=True)
    embedTen.add_field(name="Discords.com Voting Link:", value="https://discords.com/bots/bot/759436027529265172", inline=True)
    embedTen.add_field(name="Github Repository", value="https://github.com/Bazbots/The-Impostor", inline=True)
    await ctx.message.add_reaction(emoji="<:impostor:774673531786625024>")
    await ctx.send(embed=embedTen)
    
    
    
  @commands.command(aliases=["ver"])
  async def version(self, ctx):
    embedV = discord.Embed(
      colour=discord.Colour.red()
    )
    embedV.add_field(name="Current Version:", value="1.9.8", inline=True)
    embedV.add_field(name=":inbox_tray:What's new to this update::inbox_tray:", value="Nothing... still", inline=True)
    embedV.add_field(name=":outbox_tray:What we removed::outbox_tray:", value="Christmas Commands", inline=True)
    embedV.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedV)
    await ctx.message.delete()
  

  @commands.command(aliases=["c", "baz", "owner", "o"])
  async def creator(self, ctx):
    embedC = discord.Embed(
      url="https://discord.gg/5jKA9kj",
      colour = discord.Colour.red()
    )
    embedC.add_field(name="Who created The Impostor", value=":placard:The Impostor was a bot created by Baz and was first launched on the 1st of February 2021!:placard:", inline=True)
    embedC.add_field(name="About", value=":one:This is actually his first ever coded bot!:one:\n:snake:It is a discord.py bot!:snake:", inline=True)
    embedC.add_field(name=":sparkling_heart:Show some love and join his server!:sparkling_heart:", value="https://discord.gg/5jKA9kj", inline=True)
    await ctx.send(embed=embedC)
   
	  
	  
  @commands.command(aliases=["f"])
  async def feedback(self, ctx):
	  await ctx.send(":pencil:Please answer this short survey to let us know how you feel about the bot::pencil:\nhttps://docs.google.com/forms/d/e/1FAIpQLSeS_fcVh5_GRBmYCFw5qkxU29lSLU1zsTkioePy7Kp8roTVig/viewform?usp=sf_link")
	  print(f"{ctx.author} has triggered the feedback command")
	  

  @commands.command(aliases=["u", "upvote"])
  async def vote(self, ctx):
    await vibe_check(ctx, "Thanks for voting!")
    embedV = discord.Embed(
      title = "Vote for the Impostor",
      colour = discord.Colour.red(),
      url=random.choice(urls)
    )
    embedV.add_field(name="Vote for the bot on top.gg", value="https://top.gg/bot/759436027529265172/vote", inline=True)
    embedV.add_field(name="Vote for the bot on discordbotlist.com", value="https://discordbotlist.com/bots/the-impostor", inline=True)
    embedV.add_field(name="Vote for the bot on discord.bots.gg", value="https://discord.bots.gg/bots/759436027529265172", inline=True)
    embedV.add_field(name="Vote for the bot on discords.com", value="https://discords.com/bots/bot/759436027529265172", inline=True)
    await ctx.send(embed=embedV)
    
    
    
  
  @commands.command(aliases=["s", "g", "guilds", "players"])
  async def servers(self, ctx):
    embedSeven = discord.Embed(
	    colour=discord.Colour.red())
    embedSeven.add_field(name="Current Servers", value=f"Currently playing Among Us in **{len(self.client.guilds)}** servers with **{uses}** players!", inline=True)
    embedSeven.set_thumbnail(
	    url=
	    "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
	  )
    embedSeven.set_footer(
	    text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedSeven)
    await ctx.message.delete()

  @commands.command(aliases=["l", "p", "latency"])
  async def ping(self, ctx):
    embedPing = discord.Embed(
      title="Current Latency:",
      description=f"{ctx.author.mention}\nPong!\nYour ping is {round(self.client.latency * 1000)}ms!",
      colour=discord.Colour.red()
    )
    embedPing.set_footer(text=f"Invoked by {ctx.author}\n© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedPing)
   


  @commands.command()
  async def uptime(self, ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-start))))
    embedU = discord.Embed(
      title="Uptime",
      description=f"I have been online for {uptime}!",
      colour=discord.Colour.red()
    )
    await ctx.send(embed=embedU)
   
  @commands.command(aliases=["badges"])
  async def achievements(self, ctx, user:commands.MemberConverter = None):
    if user is None:
      user = ctx.author
    embed = discord.Embed(
      title=f"{user.name}'s Badges",
      colour=discord.Colour.red()
    )
    embed.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    with open("badges.json", "r") as f:
      ach = json.load(f)
      if str(user.id) in ach:
        embed.add_field(name="Total number of badges", value=f"{len(ach[str(user.id)])}", inline=True)
        #leng = 0
        for badge in ach[str(user.id)]:
          """if leng >= 24:
            embed2 = discord.Embed(title=f"{ctx.author.name}'s Badges (Page 2)", colour=discord.Colour.red())
            embed2.add_field(name=badge, value=None, inline=True)
            if leng == len(ach[str(user.id)]):
              await ctx.send(embed=embed2)
              return
            leng = leng + 1
            continue"""
          embed.add_field(name=str(badge), value=None, inline=True)
          #leng = leng + 1
      else:
        return "User has no badges"
    await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(Basic(client))
