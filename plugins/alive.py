from discord.ext import commands

class Alive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def alive(self, ctx):
        await ctx.send("""Tanrı Türk'ü Korusun. 🐺 Asena Hizmetinde!
                       
Version:0,26 Public
Branch:Master
Telegram Group: ttps://t.me/AsenaSupport
Telegram Channel: ttps://t.me/asenaremaster
Plugin Channel:ttps://t.me/asenaplugin""")

async def setup(bot):
    await bot.add_cog(Alive(bot)) 