import discord
from discord.ext.commands import Bot, Context
from discord.ext import commands, tasks
import os
import requests
import json



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


@client.comm


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspire'):
    ctx = await client.get_context(Message)
    #Do whatever you want
    quote = get_quote()
    await message.channel.send(quote)


@client.event
async def on_message(Message):
    

client.run(('key'))