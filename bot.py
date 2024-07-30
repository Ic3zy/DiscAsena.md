import discord
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content = True
intents.members = True 
intents.messages = True
async def load_extensions():
    await bot.load_extension("cogs.getusername")
    await bot.load_extension("cogs.helpcommand")
    await bot.load_extension("cogs.ban")
    await bot.load_extension("cogs.unban")
bot = commands.Bot(command_prefix='.', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game(name="Hayatlarla"))
    for filename in os.listdir('./plugins'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'plugins.{filename[:-3]}')
                print(f'Loaded extension: {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f'An error occurred: {str(error)}')
bot.run('MTI2Nzc5Mjc0NDYyNjEzMDk4NA.GSYfii.SKb0bW99UBLFM8sH8Qn715ywlDvM3788439-10') 
