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
@client.command()
async def square(number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value))
@client.command(pass_context=True)
async def ping(ctx):
    resp = await client.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await client.edit_message(resp, 'Pong! That took {:.1f}ms.'.format(1000*diff.total_seconds()))
@client.command(pass_context=True, hidden=True)
async def stdown(ctx):
    await client.say("Checking if you are the owner...")
    if ctx.message.author.id == '353501847324983299':
        await client.say("Owner verified. shutting down...")
        await client.logout()
    else:
        await client.say("Verification failed.")
client.loop.create_task(list_servers())
client.run(os.getenv("TOKEN"))
