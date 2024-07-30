import discord
from discord.ext import commands
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if ctx.message.reference:
            referenced_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
            member = referenced_message.author
        if not member:
            await ctx.send('Banlamak istediğiniz kullanıcıyı belirtmelisiniz veya bir mesajı yanıtlamalısınız.')
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} sunucudan banlandı. Sebep: {reason}')
        except discord.Forbidden:
            await ctx.send('Bu kullanıcıyı banlamak için yetkim yok.')
        except discord.HTTPException:
            await ctx.send('Kullanıcıyı banlarken bir hata oluştu.')
async def setup(bot):
    await bot.add_cog(Ban(bot))
