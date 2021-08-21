from neopixels.neopixel_controller import NeopixelController

from discord.ext import commands


class Neopixels(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.npc = NeopixelController()

    @commands.command()
    @commands.guild_only()
    async def mode(self, ctx, mode, color, wait):
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

        if not isinstance(wait, int):
            await ctx.send("{} is not a valid wait time".format(wait))

        # Make all lowercase
        mode = mode.lower()

        # Set the Color Mode
        if mode == "static":
            self.npc.static(rgb)
        elif mode == "breathe":
            self.npc.breathe(rgb, wait)
        elif mode == "rainbow-cycle":
            self.npc.rainbow_cycle(wait)
        elif mode == "rainbow-wave":
            self.npc.rainbow_wave(wait)
        elif mode == "random-color":
            self.npc.random_color()
        elif mode == "random-pixel_colors":
            self.npc.random_pixel_colors()
        elif mode == "clear" or "off" or "none":
            self.npc.clear()
        else:
            await ctx.send("{} is not a valid mode - For a list of valid modes, use f!list-modes".format(mode))
            return

        await ctx.send("{} Mode Selected".format(mode.upper()))


def setup(bot):
    bot.add_cog(Neopixels(bot))
