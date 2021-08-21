import time
import board
import neopixel

class NeopixelController:

    ORDER = neopixel.GRB
    num_pixels = 144
    pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False, pixel_order=ORDER, brightness = 0.2)
    
    # Color Wheel for Rainbow Color Modes
    def wheel(self, pos):
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

        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    # Static Color Mode
    def static(self, color):
        self.pixels.fill(color)
        self.pixels.show()
        
    # Breathing Lighting Mode
    def breathe(self, color, wait):

        # Increase Brightness
        for i in range(255):
            self.pixels.fill((round(color[0] * i / 255), round(color[1] * i / 255), round(color[2] * i / 255)))
            self.pixels.show()
            time.sleep(wait / 1000)

        # Decrease Brightness
        for i in range(255, 0, -1):
            self.pixels.fill((round(color[0] * i / 255), round(color[1] * i / 255), round(color[2] * i / 255)))
            self.pixels.show()
            time.sleep(wait / 1000)

    # Rainbow Cycle Mode (All pixels are the same color at any given time)
    def rainbow_cycle(self, wait):
        for i in range(255):
            self.pixels.fill(self.wheel(i))
            self.pixels.show()
            time.sleep(wait / 1000)

    # Rainbow Wave Mode (All pixels are different colors at any given time)
    def rainbow_wave(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait / 1000)


    
    # Clear Lighting
    def clear(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()


