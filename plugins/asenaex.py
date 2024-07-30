from discord.ext import commands
import discord
class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def asena(self, ctx):
        embed = discord.Embed(
            title="●▬▬▬ *DiscAsena Public* ▬▬▬●",
        )

        embed.add_field(
            name="🛠 : .soru [@kullanıcı]",
            value="💬 : Belirtilen kullanıcıya rastgele bir soru sorar.",
            inline=False
        )
        embed.add_field(
            name="🛠 : .zorsoru [@kullanıcı]",
            value="💬 : Belirtilen kullanıcıya rastgele zor bir soru sorar. ",
            inline=False
        )
        embed.add_field(
        name="🛠 : .alive",
        value="💬 : Botun aktif olup olmadığını sorar.",
        inline=False
        )
        embed.add_field(
        name="🛠 : .tagall",
        value="💬 : Sunucudaki herkesi etiketlemek için kullanılır.",
        inline=False
        )
        embed.add_field(
        name="🛠 : .asena",
        value="💬 : Botun tüm komutlarına erişmek için kullanılır.",
        inline=False
        )
        embed.add_field(
        name="🛠 : .ban",
        value="💬 : Yanıtladığınız/Etiketlediğiniz kişiyi gruptan banlar.",
        inline=False
        )
        embed.add_field(
        name="🛠 : .unban",
        value="💬 : Sunucudan Banladığınız Kişinin banını açar ve sunucuya davet eder.",
        inline=False
        )
        """embed.add_field(
        name="🛠 : ",
        value="💬 : ",
        inline=False
        )"""
        await ctx.send(embed=embed)
async def setup(bot):
    await bot.add_cog(HelpCommand(bot))
