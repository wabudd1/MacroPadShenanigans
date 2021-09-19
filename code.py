# SPDX-FileCopyrightText: Copyright (c) 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
import time
from rainbowio import colorwheel
from adafruit_macropad import MacroPad

macropad = MacroPad()

# Cannot be updated after initialization
# Uses Simple Text Display library
text_lines = macropad.display_text(title="Swiggity Swooty") 
# macropad.display_image("blinka.bmp")

# Set default key colors
for pixel in range(12):
    macropad.pixels[pixel] = colorwheel((pixel / 12 * 256))

# Main scan loop
while True:
    key_event = macropad.keys.events.get()
    if key_event: # Some type of key event
        if key_event.pressed: # a.k.a. Keydown
            macropad.pixels[key_event.key_number] = (100, 100, 100)
            if key_event.key_number is 0:
                macropad.keyboard.send(macropad.Keycode.WINDOWS, macropad.Keycode.L)
            if key_event.key_number is 1:
                macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.C)
                macropad.keyboard.send(macropad.Keycode.WINDOWS, macropad.Keycode.R)
                time.sleep(0.5)
                macropad.keyboard.send(macropad.Keycode.N)
                macropad.keyboard.send(macropad.Keycode.O)
                macropad.keyboard.send(macropad.Keycode.T)
                macropad.keyboard.send(macropad.Keycode.E)
                macropad.keyboard.send(macropad.Keycode.P)
                macropad.keyboard.send(macropad.Keycode.A)
                macropad.keyboard.send(macropad.Keycode.D)
                macropad.keyboard.send(macropad.Keycode.ENTER)
                time.sleep(0.5)
                macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.V)
            if key_event.key_number is 2:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 3:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 4:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 5:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 6:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 7:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 8:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 9:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 10:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 11:
                macropad.keyboard.send(macropad.Keycode.A)
            if key_event.key_number is 12:
                macropad.keyboard.send(macropad.Keycode.A)
            text_lines[0].text = f"Key pressed: {key_event.key_number}"
        else: # Keyup
            macropad.pixels[key_event.key_number] = colorwheel((key_event.key_number / 12 * 256))
        
    text_lines[1].text = f"Encoder: {macropad.encoder}"
    text_lines[2].text = f"Encoder switch: {macropad.encoder_switch}"
    text_lines.show()
