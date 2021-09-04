# SPDX-FileCopyrightText: Copyright (c) 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Simpletest demo for MacroPad. Prints the key pressed, the relative position of the rotary
encoder, and the state of the rotary encoder switch to the serial console.
"""
import time
from rainbowio import colorwheel
from adafruit_macropad import MacroPad

macropad = MacroPad()

# Cannot be updated after initialization
# Uses Simple Text Display library
text_lines = macropad.display_text(title="MacroPad Info") 
# macropad.display_image("blinka.bmp")
#audio_files = ["macropad_mp3/slow.mp3", "macropad_mp3/happy.mp3", "macropad_mp3/beats.mp3", "macropad_mp3/upbeats.mp3"]

# tones are integers in Hz
tones = [196, 220, 246, 262, 294, 330, 349, 392, 440, 494, 523, 587]
while True:
    key_event = macropad.keys.events.get()
    if key_event:
        if key_event.pressed:
            if key_event.key_number is 0:
                macropad.keyboard.send(macropad.Keycode.A)
                macropad.pixels[key_event.key_number] = colorwheel(
                    int(255 / 12) * key_event.key_number
                )
            # macropad.start_tone(tones[key_event.key_number])
            text_lines[0].text = f"Key pressed: {key_event.key_number}"

            # if key_event.key_number < len(audio_files):
            #     macropad.play_file(audio_files[key_event.key_number])
        else:
            macropad.pixels.fill((0, 0, 0))
            # macropad.stop_tone()
    text_lines[1].text = f"Encoder: {macropad.encoder}"
    text_lines[2].text = f"Encoder switch: {macropad.encoder_switch}"
    text_lines.show()
