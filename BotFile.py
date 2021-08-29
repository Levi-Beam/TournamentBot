import os
import discord
from replit import db

# Key that has the bot access code
my_secret = os.environ['T0KEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith("!Enter"):
        await message.author.send("Hello! Thank you so much for entering the tournament. This bot is here to take your information so you can know as fast as possible if you and your teammates will be playing in the Tournament! First off, what is your Teams Name?")

# Makes sure bot is activating properly in the discord server
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


client.run(my_secret)
