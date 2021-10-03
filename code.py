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

lastEncoderPosition = 0

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
                macropad.keyboard_layout.write("NOTEPAD\n")
                time.sleep(0.5)
                macropad.keyboard.send(macropad.Keycode.CONTROL, macropad.Keycode.V)
            if key_event.key_number is 2:
                time.sleep(0.01)
            if key_event.key_number is 3:
                time.sleep(0.01)
            if key_event.key_number is 4:
                time.sleep(0.01)
            if key_event.key_number is 5:
                time.sleep(0.01)
            if key_event.key_number is 6:
                time.sleep(0.01)
            if key_event.key_number is 7:
                time.sleep(0.01)
            if key_event.key_number is 8:
                time.sleep(0.01)
            if key_event.key_number is 9:
                macropad.consumer_control.send(macropad.ConsumerControlCode.SCAN_PREVIOUS_TRACK)
            if key_event.key_number is 10:
                macropad.consumer_control.send(macropad.ConsumerControlCode.PLAY_PAUSE)
            if key_event.key_number is 11:
                macropad.consumer_control.send(macropad.ConsumerControlCode.SCAN_NEXT_TRACK)
            text_lines[0].text = f"Key pressed: {key_event.key_number}"
        else: # Keyup
            macropad.pixels[key_event.key_number] = colorwheel((key_event.key_number / 12 * 256))
    # End key if block
    macropad.encoder_switch_debounced.update()

    if macropad.encoder > lastEncoderPosition:
        # increase volume
        macropad.consumer_control.send(macropad.ConsumerControlCode.VOLUME_INCREMENT)
    if macropad.encoder < lastEncoderPosition:
        # decrease volume
        macropad.consumer_control.send(macropad.ConsumerControlCode.VOLUME_DECREMENT)
    lastEncoderPosition = macropad.encoder

    if macropad.encoder_switch_debounced.pressed:
        # mute/unmute
        macropad.consumer_control.send(macropad.ConsumerControlCode.MUTE)

    text_lines[1].text = f"Encoder: {macropad.encoder}"
    text_lines[2].text = f"Encoder switch: {macropad.encoder_switch}"
    text_lines.show()
