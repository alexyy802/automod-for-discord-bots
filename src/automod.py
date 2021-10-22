import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix="!")

client = discord.Client()


@client.event
async def on_message(self,message):
      server = message.guild
      data = read_json("automod.json")
      automod = data["automod"]
      if server.id in automod:
        banword=['Put bad words here']

        if message.content in banword:
          await message.delete()
          await message.channel.send(message.author.mention+", Hey! that word isnt allowed in here!")
        else:
          return
