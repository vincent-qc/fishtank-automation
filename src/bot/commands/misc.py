from discord.ext import commands


class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        """
        Ping
        """

        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Misc(bot))
