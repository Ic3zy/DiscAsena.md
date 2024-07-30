from discord.ext import commands
class Komut(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')
async def setup(bot):
    await bot.add_cog(Komut(bot))
