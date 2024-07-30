from discord.ext import commands
class TagAllMembers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def tagall(self, ctx, *, message: str = None):
        guild = ctx.guild
        members = [f'•{member.mention}' for member in guild.members if not member.bot]
        if not members:
            await ctx.send("Sunucuda etiketlenecek üye bulunamadı.")
            return
        if message:
            members.insert(0,message)
        message_parts = ["\n".join(members[i:i+1990]) for i in range(0, len(members), 1990)]
        for part in message_parts:
            await ctx.send(part)
async def setup(bot):
    await bot.add_cog(TagAllMembers(bot))
