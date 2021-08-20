from neopixel_controller import NeopixelController


npc = NeopixelController()

npc.clear()

while True:
    npc.rainbow_wave(0.0001)