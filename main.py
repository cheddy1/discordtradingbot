import discord
import asyncio
from discord.ext import commands
import sys, traceback
token = ''
intents = discord.Intents.all()
intents.members = True

startup_extensions = ['cogs.value','cogs.general','cogs.modmail','cogs.template','cogs.pricecheck','cogs.screenshot']

bot = commands.Bot(command_prefix ='!', intents=intents)
bot.remove_command('help')
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            pass
@bot.event
async def on_ready(): #Runs when the bot connects.
    print("Ready")
    while True:
        await bot.change_presence(activity=discord.Game(name='!help | v1.0.3',type=1))
        await asyncio.sleep(120)
        await bot.change_presence(activity=discord.Activity(name='!dm for support', type=3))
        await asyncio.sleep(60)
        #await bot.change_presence(activity=discord.Activity(name='cheddydev.com', type=3))
        #await client.change_presence(activity=discord.Streaming(name="FOLLOW MY TWITCH", url="https://twitch.tv/cheddyGG", type=1))
        #await asyncio.sleep(30)

@bot.event
async def on_member_update(before, after):
    if (before.pending) == True:
      if (after.pending) == False:
        role = discord.utils.get(after.guild.roles, name="Trader")
        role2 = discord.utils.get(after.guild.roles, name="↥─────《 Server Rank 》────↥")
        role3 = discord.utils.get(after.guild.roles, name="↥────《 Inventory Value 》───↥")
        role4 = discord.utils.get(after.guild.roles, name="↥──────《 Self Role 》──────↥")
        await after.add_roles(role)
        await after.add_roles(role2)
        await after.add_roles(role3)
        await after.add_roles(role4)
bot.run(token)


