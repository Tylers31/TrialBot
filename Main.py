
import asyncio
import discord
from discord.ext import commands

token = "TOKEN HERE"
prefix = "!"

client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

#bot console
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Walhx Fail Trials'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    await asyncio.sleep(1)
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')
 
###########
#Alert CMD
###########
@client.command()
async def ping(ctx):
    await ctx.send("||@here|| **Get on we running trials!**")
    await asyncio.sleep(0.5)
    await ctx.send("||@here|| **Get on we running trials!**")
    await asyncio.sleep(0.5)
    await ctx.send("||@here|| **Get on we running trials!**")
    await asyncio.sleep(0.5)
    await ctx.send("||@here|| **Get on we running trials!**")
    await asyncio.sleep(0.5)
    await ctx.send("||@here|| **Get on we running trials!**")
  
###########
#Mental Asylum Map CMD
###########
@client.command()
async def mental(ctx):
  await ctx.send('**Mental Asylum Trial Map**', file=discord.File('mental.png'))
  await asyncio.sleep(1)
  await ctx.message.delete()
  
###########
#Haze and Seek Map CMD
###########
@client.command()
async def haze(ctx):
  await ctx.send('**Haze and Seek Trial Map**', file=discord.File('Haze.png'))
  await asyncio.sleep(1)
  await ctx.message.delete()  

###########
#Fire Colony Map CMD
###########
@client.command()
async def fire(ctx):
  await ctx.send('**Fire Colony Trial Map**', file=discord.File('fire.png'))
  await asyncio.sleep(1)
  await ctx.message.delete() 
  
###########
#Help CMD
###########
@client.command()
async def help(ctx):
  embed=discord.Embed(title="Trial Bot Commands", url="https://cosmicpvp.com/", description="*Made by tyler.#2578* \n Prefix = !\n \n> **1:** **Ping** *- Pings everyone to get on*\n > **2:** **Help** *- Displays this menu* \n > **3:** **Mental** *- Displays a map of Mental Asylum* \n > **4:** **Haze** *- Displays a map of Hase and Seek* \n > **5:** **Fire** *- Displays a map of Fire Colony*", color=0xFF5733)
  await ctx.send(embed=embed)

###########
#Client Token Execution
###########
client.run(token)
