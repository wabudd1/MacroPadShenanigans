# MacroPadShenanigans
Playing with AdaFruit MacroPad Circuit Python code.

# Some notes
[AdaFruit MacroPad repo](https://github.com/adafruit/Adafruit_CircuitPython_MacroPad) where much of this code is borrowed from.

[Media (consumer) control codes enum:](https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/consumer_control_code.py)

[Standard Keyboard codes enum](https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keycode.py)

Keyboard class supports send(*keycodes) that automatically presses and released
Press(*keycodes) and release(*keycodes) also supported
See: https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/adafruit_hid/keyboard.py
