import dbl
import discord
from discord.ext import commands
import os
import requests
import json


# EXAMPLE OF VOTE:
# {'bot': '759436027529265172', 'user': '576442029337477130', 'type': 'upvote', 'query': '', 'isWeekend': False}

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


class Vote(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.token = os.getenv("TOPGG_TOKEN")
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True, webhook_path="/dblwebhook", webhook_auth=os.getenv("TOPGG_WEBPWD"), webhook_port=5000)
    

    @commands.Cog.listener()
    async def on_guild_post(self):
        print("[Top.gg] Server count was updated successfully")


    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        print("[Top.gg] Received an upvote: ", "\n", data, sep="")
        user = int(data["user"])
        print(f"Voter name: {user}")
        embedThx = discord.Embed(
          title="Thanks for voting!",
          description=f"Thanks <@{user}> for voting for the bot!\n\nVoting Rewards are coming soon!",
          colour=discord.Colour.red()
        )
        embedThx.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
        embedThx.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
        await user.send(embed=embedThx)
    
    @commands.Cog.listener()
    async def on_dbl_test(self, data):
      print("[Top.gg] Received a test upvote:", "\n", data, sep="")
      user = int(data["user"])
      print(f"Voter name: {user}")
      embedThx = discord.Embed(
          title="Thanks for voting!",
          description=f"Thanks <@{user}> for voting for the bot!\n\nVoting Rewards are coming soon!",
          colour=discord.Colour.red()
        )
      embedThx.set_footer(text="© Baz - The Impostor - Among Us bot for Discord")
      embedThx.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png")
      await user.send(embed=embedThx)

def setup(client):
    client.add_cog(Vote(client))