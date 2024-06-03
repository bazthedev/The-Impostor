import discord
from discord.ext import commands
import random
import json
from func import spon

where = ["somewhere", "at top.gg where you vote for the impostor", "Electrical", "Medbay" , "Security", "Cafeteria", "Navigation", "Storage", "Admin", "Shields", "Oxygen", "Office", "Laboratory"]

colours = ["Yellow", "Red", "Blue", "Cyan", "Orange", "Lime", "Green", "Pink", "Purple", "Black", "White", "Brown"]

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

class Crewmate(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["r"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def report(self, ctx):
    if await banned(ctx):
      return
    await vibe_check(ctx, "snitch")
    embedFour = discord.Embed(
      title=":loudspeaker: Dead Body Reported :loudspeaker:",
      description=f"{random.choice(colours)}'s body has been found in {random.choice(where)}!",
      colour = discord.Colour.red()
      )
    embedFour.set_thumbnail(url="https://static.wikia.nocookie.net/among-us-wiki/images/9/94/Report.png/revision/latest/top-crop/width/360/height/360?cb=20210220165923")
    embedFour.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
    await ctx.send(embed=embedFour)
    await spon(ctx)
    
def setup(client):
  client.add_cog(Crewmate(client))