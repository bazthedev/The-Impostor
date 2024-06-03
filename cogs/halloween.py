import discord
from discord.ext import commands
import random
import json
import asyncio
import string

totl = ["trick", "treat"]
tricks = [
    "scare", "scare", "scare", "scare", "rickroll", "rickroll", "rickroll",
    "nothing", "nothing", "nothing", "nothing", "troll"
]
treats = [
    "crewmate", "badge", "crewmate", "nothing", "nothing", "nothing", "nothing"
]

hhstuff = ["badge", "spook", "broken", "beans", "gift", "spook", "spook", "broken", "broken", "mg"]

async def banned(ctx):
    with open("bans.json", "r") as f:
        bans = json.load(f)
        if str(ctx.author.id) in bans:
            await ctx.send(
                "You have been banned from using this bot. If you wish to appeal for an unban, please go to my support server (https://discord.gg/Sun4mtFjwE) or directly contact Baz at bazthedev@gmail.com"
            )
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

async def vibe_check(ctx, badge):
    with open("badges.json", "r") as f:
        ach = json.load(f)
        if str(ctx.author.id) in ach:
            if badge in ach[str(ctx.author.id)]:
                return
            else:
                ach[str(ctx.author.id)].append(badge)
                await ctx.author.send(
                    "You have unlocked the badge [{}]".format(badge))
        elif str(ctx.author.id) not in ach:
            ach[str(ctx.author.id)] = [badge]
    with open("badges.json", "w") as f:
        json.dump(ach, f, indent=4)


class Halloween(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["tot"])
    @commands.is_owner()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def trickortreat(self, ctx):
        if await banned(ctx):
            return
        await vibe_check(ctx, "It's the Spooky Month (Halloween 2023)")
        tot = random.choice(totl)
        if tot.lower() == "trick":
            trick = random.choice(tricks)
            if trick.lower() == "rickroll":
                embedrr = discord.Embed(
                    title="Treat!",
                    description=
                    "Wow\nYou just got treated free The Impostor Hacker Tier!\nYou can claim it here!\nhttps://bazbots.github.io/The-Impostor/reward",
                    colour=0xfc7303)
                embedrr.set_thumbnail(
                    url=
                    "https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/1539706/halloween-candy-clipart-xl.png"
                )
                await ctx.send(embed=embedrr)
            elif trick.lower() == "nothing":
                await ctx.send("Nothing happened here...")
            elif trick.lower() == "scare":
                await ctx.send("...")
                await asyncio.sleep(6)
                await ctx.author.send("ooga booga")
                await vibe_check(ctx, "ooga booga")
            elif trick.lower() == "troll":
                ed = await ctx.send("Wow! You just won **$1000000**")
                await asyncio.sleep(10)
                await ed.edit(content="~~Wow! You just won $1000000~~")
                await ctx.send("Oops...")
                await ctx.send("Meant to say $1 xD")
                await vibe_check(ctx, "It may not be a million but...")
        elif tot.lower() == "treat":
            treat = random.choice(treats)
            if treat.lower() == "badge":
                await ctx.send(
                    "Wow! You recieved the exclusive Trick or Treat Badge!")
                await vibe_check(ctx, "Trick or Treat! (Halloween 2023)")
            elif treat.lower() == "nothing":
                await ctx.send("Nothing happened here...")
            elif treat.lower() == "crewmate":
                code = str(random.randint(0, 9)) + random.choice(
                    string.ascii_letters) + str(random.randint(
                        0, 9)) + random.choice(string.ascii_letters) + str(
                            random.randint(0, 9)) + random.choice(
                                string.ascii_letters)
                await ctx.send(
                    f"Hey! You just won free Crewmate Tier! Join the support server [https://discord.gg/Sun4mtFjwE] and message Baz with this unique code ({code}) and/or a screenshot to claim it!"
                )
                with open("codes.json", "r") as f:
                    codes = json.load(f)
                    codes[str(code)] = {
                        "Tier": "Crewmate",
                        "One time use": True
                    }
                with open("codes.json", "w") as f:
                    json.dump(codes, f, indent=4)
                    return "added code to codes.json"
        else:
            await ctx.send("```\n- Unexpected error occured\n```")


# ooga booga https://www.youtube.com/watch?v=YEqYo5gH1gM


    @commands.command(aliases=["hh"])
    @commands.is_owner()
    async def hauntedhouse(self, ctx):
        await banned(ctx)
        await chkdsk(ctx)
        await vibe_check(ctx, "It's the Spooky Month (Halloween 2023)")
        embed = discord.Embed(
            title="Visit a haunted house!",
            description=
            "Spend 250 beans to visit the haunted house and you might win a souvenir, but you might also get spooked!",
            colour=0xfc7303
        )
        await ctx.send(embed=embed)
        await ctx.send(f"Hey {ctx.author.mention}, are you sure you want to visit the Haunted House?\nThis is gonna cost you <:bean:908267086348955648> 250 (Yes/No)")
        try:
          confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
        except asyncio.TimeoutError:
          await ctx.send(f"I don't know where you went, so maybe you chickened out or something.")
        else:
          if confirm.content[0].lower() != "y":
            await ctx.send("Ok, maybe you can go another time.")
            return
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if bals[str(ctx.author.id)]["benz"] < 250:
              await ctx.send(f"{ctx.author.mention}, you need at least <:bean:908267086348955648> 250 to buy a ticket to the Haunted House")
              return
            if str(ctx.author.id) not in bals:
              bals[str(ctx.author.id)] = {
                "benz":100,
                "Inventory":{},
                "xp":0,
                "lvl":0
              }
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
            if str(ctx.author.id) not in bals:
              await ctx.send(f"Hey {ctx.author.mention}, you haven't got enough to visit the Haunted House! Do some tasks and then you will earn some beans")
              return
            after_benz = bals[str(ctx.author.id)]["benz"] - 250
            bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          hhitem = random.choice(hhstuff)
          if hhitem == "badge":
            await vibe_check(ctx, "No chicken! Entered the Haunted House in 2023")
            await ctx.send("Wow! You just got the badge to show how brave you were!")
          elif hhitem == "beans":
            await ctx.send("Nice! Someone got so spooked that they dropped their wallet with <:bean:908267086348955648> 500!")
            with open("accounts.json", "r") as f:
              bals = json.load(f)
              after_benz = bals[str(ctx.author.id)]["benz"] + 500
              bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          elif hhitem == "spook":
            await ctx.send("Wow! You got so spooked that your wallet fell out! I wonder if someone found it? (- <:bean:908267086348955648> 500")
            with open("accounts.json", "r") as f:
              bals = json.load(f)
              after_benz = bals[str(ctx.author.id)]["benz"] - 500
              bals[str(ctx.author.id)]["benz"] = after_benz
            with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
          elif hhitem == "broken":
            await ctx.send("Look's like one of the animatronics is broken, so your ticket is invalid!")
          elif hhitem == "gift":
            await ctx.send("You bought something from the souvenir shop on the way out!")
            
            # give user exclusive item and minigame (mg) is for different rooms with different rewards
        
    

def setup(client):
    client.add_cog(Halloween(client))
