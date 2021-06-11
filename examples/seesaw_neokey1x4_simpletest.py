# SPDX-FileCopyrightText: 2021 John Furcean
# SPDX-License-Identifier: MIT

"""NeoKey 1x4 QT I2C simple example."""

import board
import time
from adafruit_seesaw import seesaw, neopixel, digitalio


# For use with the STEMMA connector on QT Py RP2040
# import busio
# i2c = busio.I2C(board.SCL1, board.SDA1)
# seesaw = seesaw.Seesaw(i2c, 0x30)

seesaw = seesaw.Seesaw(board.I2C(), 0x30)

# intialize each button using pins 4,5,6,7
buttons = []
for i in range(4, 8):
    seesaw.pin_mode(i, seesaw.INPUT_PULLUP)
    button = digitalio.DigitalIO(seesaw, i)
    buttons.append(button)

pixels = neopixel.NeoPixel(seesaw, 3, 4)
pixels.brightness = 0.3

# pulse all the LEDs on to show they're working
for i in range(4):
    pixels[i] = (128, 128, 128)
    time.sleep(0.05)

for i in range(4):
    pixels[i] = 0x000000
    time.sleep(0.05)

while True:
    for i, button in enumerate(buttons):
        if not button.value:
            if i == 0:
                print("Button A")
                pixels[i] = (255, 0, 0)
            elif i == 1:
                print("Button B")
                pixels[i] = (255, 255, 0)
            elif i == 2:
                print("Button C")
                pixels[i] = (0, 255, 0)
            elif i == 3:
                print("Button D")
                pixels[i] = (0, 0, 255)
        else:
            pixels[i] = (0, 0, 0)

    # don't print too fast
    time.sleep(0.01)
