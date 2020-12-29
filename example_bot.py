import discord
import discord
from discord.ext import commands
from random import random
import time
import json

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '*', intents = intents)


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    print(f"{member} がきました.")

@bot.event
async def on_member_remove(member):
    print(f"{member} が行きました.")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちわ！")
'''
@bot.command(aliases=['D', 'Dice', 'Roll'])
async def r1(ctx, * , num):
    await ctx.send(f"Rolling a D{num}!")
    await ctx.send(int(random()*int(num)) + 1)
'''
@bot.command(aliases=['D','Dice', 'Roll'])
async def rx(ctx, num, times = 1):
    i = 0
    times = int(times)
    total = 0
    string = ""
    await ctx.send(f"Rolling a D{num} {times} times!")
    for i in range(times):
        inst = int(random()*int(num)) + 1
        string += (str(inst) + "  ")
        total += inst
    await ctx.send(f"Sequence: {string}")
    await ctx.send(f"Total: {total}!")
    time.sleep(5)
    await ctx.channel.purge(limit = 4)

on_messagelist = ["sign up", "Sign Up", "SignUp", "signup", "su"]
@bot.event
async def on_message(message):
    user = message.author
    List = ''
    print(message.id)
    if "@!7904125296367370" in message.content:
        string = message.content[23:]
        if string in on_messagelist:
            print("Found sign up request")
            with open("signup.json", 'r') as f:
                List = json.load(f)
                List[message.id] = 'yes'
            with open("signup.json", 'w') as f:
                json.dump(List, f, indent=4)

    await message.add_reaction('\U0001F44D')

bot.run('NzkwNDEyNTI5NjM2NzM3MDY2.X-APCA.WlvOZFgugVayUiUTvjTQPGpX5uI')