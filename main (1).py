import discord
from discord.ext import commands
import os
import requests
import json
import random
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '!', intents = discord.Intents().all())

sad_words = ["ضوجه", "ملل", "طاكه روحي", "ضوجة", "طاكة روحي", "ضايج", "مالي خلك", "مالي خلق"]

starter_pray = [
    "كوم صلي اخذهة مني",
    "حتى اني وداعتك",
    "شنسوي هي هاي الحياة",
    "من شنو؟!",
    "متسوة",
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    await client.change_presence(
        activity = discord.Activity(type = discord.ActivityType.playing, name = 'valorant 🖥️ '))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(starter_pray))


@client.command()
async def hi(ctx):
    await ctx.send("hi there :partying_face")

keep_alive()
client.run(os.getenv('token'))