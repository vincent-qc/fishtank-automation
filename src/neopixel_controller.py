import time
import board
import neopixel

class Neopixel_Controller:

    ORDER = neopixel.GRB
    num_pixels = 144
    pixels = neopixel.NeoPixel(board.NEOPIXEL, num_pixels, auto_write=False, pixel_order=ORDER)
    
    # Color Wheel for Rainbow Color Modes
    def wheel(pos):
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)

        return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    # Breathing Lighting Mode
    def breathe(color, time):

        # Increase Brightness
        for i in range(100):
            pixels.fill((color[0] * i / 100, color[1] * i / 100, color[2] * i / 100))
            pixels.show()
            time.sleep(time)

        # Decrease Brightness
        for i in range(100, 0, -1):
            pixels.fill((color[0] * i / 100, color[1] * i / 100, color[2] * i / 100))
            pixels.show()
            time.sleep(time)

    # Rainbow Cycle Mode (All pixels are the same color at any given time)
    def rainbow_cycle(wait):
        for i in range(255):
            pixels.fill(wheel(i))
            pixels.show()
            time.sleep(wait)

    # Rainbow Wave Mode (All pixels are different colors at any given time)
    def rainbow_wave(wait):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)

    # Static Color Mode
    def static(color):
        pixels.fill(color)
        pixels.show()
    
    # Clear Lighting
    def clear():
        pixels.fill((0, 0, 0))


