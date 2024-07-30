import discord
from discord.ext import commands
class Unban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='unban')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, *, reason=None):
        """Bir kullanıcının banını kaldırır ve ona davet linki gönderir."""
        try:
            async for ban_entry in ctx.guild.bans():
                if ban_entry.user.id == user.id:
                    await ctx.guild.unban(user, reason=reason)
                    await ctx.send(f'{user.mention} banı kaldırıldı. Sebep: {reason}')
                    invite = await ctx.channel.create_invite(max_uses=1, unique=True)
                    try:
                        await user.send(f'Merhaba {user.name}, banınız kaldırıldı. İşte davet linkiniz: {invite.url}')
                    except discord.Forbidden:
                        await ctx.send(f'{user.mention} kullanıcısına davet linki gönderilemedi.')
                    return
            await ctx.send(f'{user.mention} kullanıcı sunucuda banlı değil.')
        except discord.Forbidden:
            await ctx.send('Bu kullanıcının banını kaldırmak için yetkim yok.')
        except discord.HTTPException:
            await ctx.send('Kullanıcının banını kaldırırken bir hata oluştu.')
async def setup(bot):
    await bot.add_cog(Unban(bot))
