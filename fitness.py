import discord
from discord.ext import commands
from datetime import datetime
import sys
import random
import config

client = commands.Bot(command_prefix="!")

token = sys.argv[1]

ODD = 50

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
    print(f"Bot started at {datetime.now()}")


@client.event
async def on_message(msg):

    if msg.author == client.user:
        return

    # can't have anyone making fun of my bot
    if (f"<@!{config.bot_id}>" in msg.content and "fuck you" in msg.content):
        await msg.channel.send(msg.author.mention + " fuck you too")


    num = random.randint(1,ODD)
    
    exercise = get_exercise()


    if (num==1):
        await msg.channel.send(msg.author.mention + f": you posted cringe, do {exercise[1]} {exercise[0]}")
    

    await client.process_commands(msg)

@client.command(hidden=True)
async def odds(ctx, newOdd):
    if (not ctx.author.guild_permissions.administrator):
        await ctx.send("You do not have the perms needed, you nerd")
        return

    global ODD

    ODD = int(newOdd)
    await ctx.send(f"New odds: 1 in {newOdd}")



client.run(token)