import asyncio
import discord
from discord.ext import commands
intents = discord.Intents().all()

token = "Token Here"
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
    if ctx.message.author.guild_permissions.administrator:
      embed=discord.Embed(title="Get on ||@here||", url="https://cosmicpvp.com/", description="Running trials join disc", color=0xFF5733)
    else:
      embed=discord.Embed(title="Permission Error!", description="You do not have that permission!", color=0xFF5733)
    await ctx.send(embed=embed)
    await ctx.message.delete()
  
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
  embed=discord.Embed(title="Trial Bot Commands", url="https://cosmicpvp.com/", description="*Made by tyler.#2578* \n Prefix = !\n \n> **Ping** *- Pings everyone to get on*\n > **Help** *- Displays this menu* \n > **Mental** *- Displays a map of Mental Asylum* \n > **Haze** *- Displays a map of Hase and Seek* \n > **Fire** *- Displays a map of Fire Colony*", color=0xFF5733)
  await ctx.send(embed=embed)

###########
#Auto Role
##########
@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name='member')
  await client.add_roles(member, role)
  
###########
#Client Token Execution
###########
client.run(token)
