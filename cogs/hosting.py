import discord
from discord.ext import commands
import json
import asyncio 

# Find a way to get the voice channel and make setup for room

async def banned(ctx):
  with open("bans.json", "r") as f:
    bans = json.load(f)
    if str(ctx.author.id) in bans:
      await ctx.send("You have been banned from using this bot. If you wish to appeal for an unban, please go to my support server (https://discord.gg/Sun4mtFjwE) or directly contact Baz at bazthedev@gmail.com")
      return True
    else:
      return False

class Hosting(commands.Cog):

  def __init__(self, client):
    self.client = client


  @commands.command()
  @commands.guild_only()
  @commands.is_owner()
  async def host(self, ctx):
    if await banned(ctx):
      return
    # Make interactive setup
    embedSetup = discord.Embed(
      title="Welcome to the Interactive Among Us Voice Hosting Setup via The Impostor!",
      description="Momentarily, this message will be edited and you will be prompted with a series of questions",
      colour=discord.Colour.red()
    )
    s = await ctx.send(embed=embedSetup)
    await asyncio.sleep(10)
    embedPriv = discord.Embed(
      title="Please select your privacy:",
      description="React to the appropriate symbol:\n🔒 Private (Must use code to join)\n🔓 Public (Only those in your server can join)",
      colour=discord.Colour.red()
    )
    await s.edit(embed=embedPriv)
    await s.add_reaction(emoji="🔓")
    await s.add_reaction(emoji="🔒")
    """
    def check(reaction, user):
      user == ctx.author and str(reaction.emoji) == '🔒'

    try:
            reaction, user = await client.wait_for('reaction_add', timeout=10.0, check=check)
    except asyncio.TimeoutError:
            await ctx.send("```diff\n- Your request has timed out (60 Second Limit)")
    else:
      await ctx.send("")  
    """
    with open("games.json", "r") as f:
      games = json.load(f)
      if ctx.author.name in games and ctx.guild.id in games[ctx.author.name]["Guild"]:
        await ctx.send("```diff\n- 403 Forbidden: You already have a room under your name and in the same guild!\n```")
        return "403 Forbidden"
      games[ctx.author.name] = {"Guild":ctx.guild.id, "Users": [], "Owner": ctx.author.id, "Privacy": None}
    with open("games.json", "w") as f:
      json.dump(games, f, indent=4)
      embedDone = discord.Embed(
        title="Successfully Created the room",
        description="The room {}, has been successfully created".format(ctx.author.name),
        colour=discord.Colour.green()
      )
      await ctx.send(embed=embedDone)

  
  @commands.command()
  @commands.is_owner()
  async def join(self, ctx, owner : commands.MemberConverter):
    if await banned(ctx):
      return
    with open("games.json", "r") as f:
      games = json.load(f)
      if owner.name not in games:
        embedN = discord.Embed(
          title="Unable to join game",
          description="The game you have provided `{}` does not exist".format(owner.name),
          colour=discord.Colour.red()
          )
        await ctx.send(embed=embedN)
        return "404 Not found"
      elif games[owner.name]["Guild"] != ctx.guild.id:
        await ctx.send("This room is in an external guild, meaning that you can only join if you are in that server")
        return "403 Forbidden"
      elif ctx.author.id in games[owner.name]["Users"]:
        await ctx.send("403 Forbidden\nYou are already in this room!")
        return "403 Forbidden"
      else:
        if ctx.author.name == games[owner.name]:
          await ctx.send("You cannot join the game as you are the owner!")
          return "403 Forbidden"
        else:
          games[owner.name]["Users"].append(ctx.author.id)
    with open("games.json", "w") as f:
      json.dump(games, f, indent=4)
      embedDone = discord.Embed(
        title="Successfully joined the room!",
        description="{}\nYou have joined the room `{}`".format(ctx.author.mention, owner.name),
        colour=discord.Colour.green()
      )
      await ctx.send(embed=embedDone)
      

  @commands.command()
  @commands.is_owner()
  async def leave(self, ctx):
    if await banned(ctx):
      return
    with open("games.json", "r") as f:
      games = json.load(f)
      if ctx.author.id not in games:
        return "404 Not found"
      games["Users"].pop(ctx.author.id)
      embedYes = discord.Embed(
        title="Successfully Left the Room!",
        description="{}\nYou have successfully left the room `{}`!".format(ctx.author.mention, games["owner"]),
        colour=discord.Colour.green()
      )
      await ctx.send(embed=embedYes)
    with open("games.json", "w") as f:
      json.dump(games, f, indent=4)

  @commands.command()
  @commands.is_owner()
  async def close(self, ctx):
    if await banned(ctx):
      return
    with open("games.json", "r") as f:
      games = json.load(f)
      if ctx.author.name not in games:
        embedFail = discord.Embed(
          title="Error Closing the room",
          description="There are currently no open rooms under the name {}!".format(ctx.author.name),
          colour=discord.Colour.red()
          )
        await ctx.send(embed=embedFail)
        return "404 Not found"
      elif games[ctx.author.name]["Guild"] != ctx.guild.id:
        embedFail = discord.Embed(
          title="Error closing the room",
          description="There are no rooms in you current guild, {}".format(ctx.guild.name),
          colour=discord.Colour.red()
        )
        await ctx.send(embed=embedFail)
        return "404 Not found"
      else:
        embedClose = discord.Embed(
          title="Successfully closed the room!",
          description=f"{ctx.author.mention}\nThe room: `{ctx.author.name}` has been closed!",
          colour=discord.Colour.green()
        )
        await ctx.send(embed=embedClose)
        games.pop(ctx.author.name)
        with open("games.json", "w") as f:
          json.dump(games, f, indent=4)
        
  


def setup(client):
  client.add_cog(Hosting(client))