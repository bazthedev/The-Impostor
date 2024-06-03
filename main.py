"""
Baz 2021-2024 - The Impostor - Among Us Bot for Discord
"""
import discord
import os
#from fallback import fallback
from discord.ext import commands, tasks
from datetime import datetime
import asyncio
import dbl
from colorama import Fore
import random
import json
import patreon
import string

with open("accounts.json", "r") as f:
    useraccountcontrol = json.load(f)
    uses = len(useraccountcontrol)
now = datetime.now()

boot_time = now.strftime("%d/%m/%Y %H:%M:%S")

client = commands.Bot(command_prefix=commands.when_mentioned_or("$"),
                      description="An Among Us bot for Discord!",
                      case_insensitive=True, intents=None)
client.remove_command("help")

__version__ = "1.9.8"

# Birthday: 02/02/2021

#"https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png"


@client.event
async def on_guild_join(guild):
    print(Fore.GREEN + f"I have joined {guild} with {guild.member_count}" +
          Fore.RESET)
    channel = client.get_channel(838465155582394390)
    console = discord.Embed(
        title="Console",
        description=f"I have joined {guild} with {guild.member_count}")
    await channel.send(embed=console)
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            embedHi = discord.Embed(
                title="Thanks for adding me!",
                description=
                f"<:impostor:774673531786625024>I am the Impostor - a bot created by Baz!<:impostor:774673531786625024>\n\n<:nft:972489865847517184>You can join my support server by running $help and you can view all of my commands here as well!<:nft:972489865847517184>\n\n<:patreon:839897502925062165> Feel free to go to https://www.patreon.com/theimpostor to gain access to cool premium commands! <:patreon:839897502925062165>\nIf you join the <:purple:839879572631453696> Hacker Plan <:purple:839879572631453696>, then you will recieve all premium commands, a special role, early access to commands and even work in progress updates!\n:partying_face:Have fun!:partying_face:\n\n\n<:ping:757276110252670986>When you added this bot, it was in version {__version__}<:ping:757276110252670986>",
                url="https://www.patreon.com/theimpostor",
                colour=discord.Colour.red())
            embedHi.set_thumbnail(
                url=
                "https://cdn1.iconfinder.com/data/icons/logos-brands-in-colors/231/among-us-player-red-512.png"
            )
            embedHi.set_image(
                url=
                "https://cdn.discordapp.com/attachments/764132789670117406/833380621686145095/impostor_thumbnail.png"
            )
            embedHi.set_footer(
                text="© Baz - The Impostor - Among Us bot for Discord")
            await channel.send(embed=embedHi)
        break


@client.event
async def on_guild_remove(guild):
    print(Fore.GREEN + f"I have left {guild} with {guild.member_count}" +
          Fore.RESET)
    channel = client.get_channel(838465155582394390)
    console = discord.Embed(
        title="Console",
        description=f"I have left {guild} with {guild.member_count}")
    await channel.send(embed=console)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name="Starting up..."))
    print(
        Fore.BLUE +
        f'Successful login to {client.user}\nVersion {__version__}\nBot is in {len(client.guilds)} servers with {uses} accounts\nClient ID: {client.user.id}\nRemember to add 1 hour to time: {boot_time}'
    )
    with open("games.json", "r") as f:
        games = json.load(f)
        print("Current open games: {}".format(len(games)))
    change_status.start()
    channel = client.get_channel(838465155582394390)
    console = discord.Embed(
        title="Console",
        description=
        f"Bot has started in {len(client.guilds)} servers\nVersion: {__version__}\nID: {client.user.id}\nStart time (add one hour to): {boot_time}"
    )
    await channel.send(embed=console)


lotto = 918419575312379974


@tasks.loop(seconds=600)
async def change_status():
    await client.change_presence(activity=random.choice(activities))
    print(Fore.GREEN + "Successfully changed status!")


status = [
    "Among Us on Discord! | $help, $info",
    "https://www.patreon.com/theimpostor | $patreon",
    "https://bazbots.github.io/The-Impostor | $info",
    f"Version {__version__} | $version",
    "Vote for the bot by running $vote | $info",
    "The GitHub Repository | $info", "What do you think? | $feedback",
    "$help, $info", "Use the prefix $ or @The Impostor", "Created by Baz!",
    "$slots | Will you win big?",
    "$lotto | Buy a lottery ticket for 1000 beans!",
    f"{uses} players"
]
status =["[NOTICE] The Impostor is ending support soon, please join our support server (@The Impostor help) for further information."]

activities = [
    discord.Game(name=random.choice(status)),
    discord.Activity(type=discord.ActivityType.competing,
                     name=random.choice(status)),
    discord.Activity(type=discord.ActivityType.watching,
                     name=random.choice(status)),
    discord.Activity(type=discord.ActivityType.listening,
                     name=random.choice(status)),
    discord.Streaming(name=random.choice(status),
                      url="https://twitch.tv/bazthedev")
]


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    await client.load_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    await client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

Fore.RESET

#fallback()
client.run(os.getenv("TOKEN"))
