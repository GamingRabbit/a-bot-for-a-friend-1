from discord import Game
from discord.ext.commands import Bot #not needed
import discord
from discord.ext import commands
import random
import os
import asyncio
import aiohttp

BOT_PREFIX=("cat!","msg!cat.")

client = Bot(command_prefix=BOT_PREFIX)
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="msg!cat.help"))
    print("Logged in as " + client.user.name)
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
@client.command()
async def say(*,message):
         await client.say(message)


@client.command(name = "8ball")
async def eightball():
    responses =["no","maybe""yes", "idk, ask again later", "Definitely", "nope", "yes", "of course!"]
    await client.say(random.choice(responses))

@client.event
async def on_member_join(member):
    await client.send_message(member, "
client.loop.create_task(list_servers())
client.run(os.getenv("TOKEN"))
