import time
import random
import board
import neopixel

ORDER = neopixel.GRB
num_pixels = 144
pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False, pixel_order=ORDER, brightness=0.2)


# Static Color Mode
def static(color):
    pixels.fill(color)
    pixels.show()


# Breathing Lighting Mode
def breathe(color, wait):
    # Function to fill pixels for breathing lighting
    def fill_pixels():
        pixels.fill((round(color[0] * i / 255), round(color[1] * i / 255), round(color[2] * i / 255)))
        pixels.show()
        time.sleep(wait / 1000)

    # Increase Brightness
    for i in range(255):
        fill_pixels()

    # Decrease Brightness
    for i in range(255, 0, -1):
        fill_pixels()


# Rainbow Cycle Mode (All pixels are the same color at any given time)
def rainbow_cycle(wait):
    for i in range(255):
        pixels.fill(wheel(i))
        pixels.show()
        time.sleep(wait / 1000)


# Rainbow Wave Mode (All pixels are different colors at any given time)
def rainbow_wave(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait / 1000)


# Sets the Entire Strip to a Random Color
def random_color():
    pixels.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pixels.show()


# Sets Each Pixel to a Random Color (idk why you would use this option lol)
def random_pixel_colors():
    for i in range(num_pixels):
        pixels[i] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pixels.show()


# The Forbidden Mode
# def epilepsy_mode(wait):
#     print("why")

# Clear Lighting
def clear():
    pixels.fill((0, 0, 0))
    pixels.show()


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


class Options:
    mode = "static"
    set_color = (0, 0, 0)
    set_wait = 1


def set_mode(mode, color, wait):
    Options.mode = mode
    Options.set_color = color
    Options.set_wait = wait


def start():
    if Options.mode == "static":
        static(Options.set_color)
    elif Options.mode == "breathe":
        breathe(Options.set_color, Options.set_wait)
    elif Options.mode == "rainbow-cycle":
        rainbow_cycle(Options.set_wait)
    elif Options.mode == "rainbow-wave":
        rainbow_wave(Options.set_wait)
    elif Options.mode == "random-color":
        random_color()
    elif Options.mode == "random-pixel_colors":
        random_pixel_colors()
    elif Options.mode == "clear" or "off" or "none":
        clear()
