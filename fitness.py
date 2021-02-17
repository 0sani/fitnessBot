import discord
from discord.ext import commands
from datetime import datetime
import sys, os
import random
import json

client = commands.Bot(command_prefix="!")

token = sys.argv[1]

configFile = "config.json"

def get_data():

    with open(configFile, "r") as f:
        data = json.load(f)
        f.close()
    
    return data

def write_data(data):

    with open(configFile, "w") as f:
        json.dump(data, f)
        f.close()

def get_exercise():

    exerciseList = {
        "push-ups" : random.randint(1,4)*5,
        "sit-ups" : random.randint(2,5)*5,
        "squats" : random.randint(3,6)*5,
        "burpees" : random.randint(1,2)*5
    }

    return random.choice(list(exerciseList.items()))


@client.event
async def on_ready():
    if (not os.path.isfile(configFile)):
        config = {}

        config["botId"] = client.user.id

        config["servers"] = {}

        

        for server in client.guilds:
            config["servers"][server.id] = {
                "odds" : 50, #default odds
                "message" : ": do",
                "excludedUsers" : [],
                "excludedChannels" : []
            }
        
        with open(configFile, "w") as f:
            json.dump(config, f)
            f.close()
    
    print(f"Bot started at {datetime.now()}")

@client.event
async def on_message(msg):

    if (msg.author == client.user): #checks if sent by itself
        return

    data = get_data()

    number = random.randint(1, int(data["servers"][str(msg.guild.id)]["odds"])) #gets a random int based on the odds

    message = data["servers"][str(msg.guild.id)]["message"]
    exercise = get_exercise()

    if (number == 1):
        await msg.channel.send(f"{msg.author.mention}{message} {exercise[1]} {exercise[0]}")
    
    await client.process_commands(msg)


@client.command(hidden=True)
async def change_odds(ctx, newOdd):

    if (not ctx.author.guild_permissions.administrator):
        await ctx.send("You do not have the permissions needed to use this command")
        return
    
    odd = int(newOdd)

    data = get_data()

    data["servers"][str(ctx.guild.id)]["odds"] = odd

    write_data(data)

    await ctx.send(f"New odds: 1 in {newOdd}")

@client.command(hidden=True)
async def change_message(ctx, newMsg):
    
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send("You do not have the permissions needed to use this command")
        return

    data = get_data()

    data["servers"][str(ctx.guild.id)]["message"] = newMsg

    write_data(data)

    await ctx.send(f"Changed message to <mentions user>: {newMsg} <exercise>")

@client.command(hidden=True)
async def exclude_channel(ctx, channel): #takes in channel id

    if (not ctx.author.guild_permissions.administrator):
        await ctx.send("You do not have the permissions needed to use this command")
        return

    channel = int(channel) 

    data = get_data()

    excludedChannels = data["servers"][str(ctx.guild.id)]["excludedChannels"]  

    channels = [channel.id for channel in ctx.guild.channels] 

    if (channel not in channels):
        await ctx.send("That is not a channel in this server")
        return

    if (channel in excludedChannels):
        await ctx.send("This channel is already exluded")
        return
    
    excludedChannels.append(channel)

    data["servers"][str(ctx.guild.id)]["excludedChannels"] = excludedChannels

    write_data(data)
    
    await ctx.send(f"Added {channel} to the excluded channels")

@client.command(hidden=True)
async def unexclude_channel(ctx,channel):

    if (not ctx.author.guild_permissions.administrator):
        await ctx.send("You do not have the permissions needed to use this command")
        return

    channel = int(channel)

    data = get_data()

    excludedChannels = data["servers"][str(ctx.guild.id)]["excludedChannels"]

    channels = [channel.id for channel in ctx.guild.channels]

    if (channel not in channels):
        await ctx.send("That is not a channel in this server")
        return
    
    if (channel not in excludedChannels):
        await ctx.send("The channel is not already exlcuded")
        return
    
    excludedChannels.remove(channel)

    data["servers"][str(ctx.guild.id)]["excludedChannels"] = excludedChannels

    write_data(data)
    
    await ctx.send(f"Removed {channel} from the excluded channels")


client.run(token)