import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import DiodeMatrixScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.macros import Macros
from kmk.extensions.rgb import RGB
from kmk.extensions.pegoled import PegOledDisplay

# Main keyboard instance
keyboard = KMKKeyboard()

# Layers and macros
layers = Layers()
macros = Macros()
keyboard.modules.append(layers)
keyboard.modules.append(macros)

# SK6812 MINI-E RGB LEDs on pin D6
led = RGB(
    pixel_pin=board.D6,
    num_pixels=16,
    brightness=0.2,
)
keyboard.extensions.append(led)

# I2C for 0.91" OLED
i2c = busio.I2C(board.SCL, board.SDA)
oled = PegOledDisplay(i2c, width=128, height=32)
keyboard.extensions.append(oled)

# 4×4 key matrix with diodes
keyboard.matrix = DiodeMatrixScanner(
    col_pins=[board.D0, board.D1, board.D2, board.D3],  # columns
    row_pins=[board.D7, board.D8, board.D9, board.D10],  # rows
    diode_orientation=DiodeOrientation.COL2ROW,
)

# 4×4 keymap
keyboard.keymap = [
    [KC.Q, KC.W, KC.E, KC.R],
    [KC.A, KC.S, KC.D, KC.F],
    [KC.Z, KC.X, KC.C, KC.V],
    [KC.KC_1, KC.KC_2, KC.KC_3, KC.KC_4],
]

if __name__ == '__main__':
    keyboard.go()
