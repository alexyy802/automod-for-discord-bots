# automod-for-discord-bots
A automod for discord.py 


# Introduction

Hello, im alexy im a discord.py developer and i love learning new things.In this github rep i will show you how to make a automod from little exp!


# Startup
I assume you all know what discord.py is and what it does, so im going to get straight to the point!

# Automod Files

For my version of a automod its just deleting a banned message, but with a twist because we are going to make a function that enables the user to turn off and on the automod 
Lets create a file called `automod.json` dont forget to import `json` once you have that go over to that json file and put something like this :

```json
{
  "automodserver":[]
}
```

# Setting up functions

We are going to make 2 functions to `write` the data and delete the data, why do we need this you ask? well to enable the automod we have to write the guild.id into the `automod.json` and store it so the bot know's witch server that has automod enabled or disabled

For the read use : 

```py
def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data
```

And for the write :

```py
def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
```

Nice! we got our functions setup almost there :D

# Making commands

Now lets make a command for the automod! 

For disable automod :
```py
guild = ctx.guild
data = read_json("autoserver.json")
automod = data["autoserver"]
if guild.id not in automod:
  await ctx.send('You did not enable automod yet! :no:')
  return
guild = ctx.guild
data = read_json("autoserver.json")
data["autoserver"].remove(guild.id)
write_json(data, "autoserver.json")
await ctx.send('Automod disabled! :white_check_mark:')
```

For Enable automod:
```py
guild = ctx.guild
data = read_json("autoserver.json")
automod = data["autoserver"]
if guild.id in automod:
  await ctx.send('Automod has already been enabled in this server! :no:') #if the server id is already in the json file 
  return
data = read_json("autoserver.json")
data["autoserver"].append(guild.id)
write_json(data, "autoserver.json")
await ctx.send('Automod enabled! :white_check_mark:')
```

And you schould be good to go!

# NOTE

This project is for edcucation **DONT COPY AND PASTE** If you copy and paste from the code above you wont learn anything and if there is any errors just make a PR (pull request) and if you dont understand anything because you just copy and paste its on you.

Full code in the src folder!
