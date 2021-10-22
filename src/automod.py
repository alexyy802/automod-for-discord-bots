import discord
from discord.ext import commands
import json

client = commands.Bot(command_prefix="!")

client = discord.Client()

def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


@client.event
async def on_message(self,message):
      server = message.guild
      data = read_json("automod.json")
      automod = data["automodservers"]
      if server.id in automod:
        banword=['Put bad words here']

        if message.content in banword:
          await message.delete()
          e = discord.Embed(title=f"{message.author},Hey! that word isnt allowed here!")
          e.set_footer(text="Automod made by : NotAlexy_Kyu#4003") #<- dont remove this!
          e.set_image(url="https://www.kindpng.com/picc/m/65-650060_no-entry-png-transparent-png.png")
          await message.channel.send(embed=e)
        else:
          return

@client.command()
async def hello(ctx,member:discord.Member):
      await ctx.send('Hello,'+ ctx.author)
      return


client.run(discord-bot-token)
