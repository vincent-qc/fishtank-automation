import discord
from discord.ext import commands
from neopixels.neopixel_controller import NeopixelController

import json

intents = discord.Intents.default()
config = open("config.json")
data = json.load(config)


cogs: list = ["commands.misc", "commands.neopixels"]

client = commands.Bot(command_prefix=data["prefix"], help_command=None, intents=intents)


@client.event
async def on_ready():
    print("Bot Online")

    # Change Bot Status
    await client.change_presence(status=discord.Status.online, activity=discord.Game(data["status"]))

    # Load All Commands
    for c in cogs:
        try:
            client.load_extension(c)
            print("{} command loaded".format(c))
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("{} command failed to load:\n{}".format(c, exc))

    NeopixelController.start()

client.run(data["token"])
