from neopixels.neopixel_controller import *

from discord.ext import commands


class Neopixels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.modes = ["static", "breathe", "rainbow-cycle", "rainbow-wave", "random-color", "random-pixel-colors"]

    @commands.command()
    @commands.guild_only()
    async def mode(self, ctx, mode, color="#FFFFFF", wait=1):
        """
        Change the Neopixels Lighting Mode
        """

        rgb = (255, 255, 255)

        # Convert HEX into RGB
        try:
            c = color.lstrip('#')
            rgb = tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))
        except:
            await ctx.send("{} is not a valid color (Must be in HEX format)".format(color))
            return

        if not isinstance(int(wait), int):
            await ctx.send("{} is not a valid wait time".format(wait))
            return

        # Make all lowercase
        mode = mode.lower()

        # TODO: fix async send problem

        if mode in self.modes:
            set_mode(mode, rgb, wait)

            await ctx.send("{} Mode Selected".format(mode.upper()))
        else:
            await ctx.send("{} is not a valid mode".format(mode))


def setup(bot):
    bot.add_cog(Neopixels(bot))
