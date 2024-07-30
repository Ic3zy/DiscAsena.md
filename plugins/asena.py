from discord.ext import commands
class ExamplePlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def recognize(self, ctx):
        await ctx.send("send")
async def setup(bot):
    await bot.add_cog(ExamplePlugin(bot))
