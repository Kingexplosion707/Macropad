# main.py — 7-Key Macropad Firmware
# Hardware: Seeed XIAO RP2040
# Firmware: CircuitPython 9.x
# -----------------------------------------------
# Pin mapping (edit to match your PCB routing):
#
#   ROW pins : GP1, GP2, GP3   (outputs)
#   COL pins : GP4, GP5, GP6   (inputs with pull-up)
#
#   Switch matrix layout:
#   [ K0 ] [ K1 ] [ K2 ]
#   [ K3 ] [ K4 ] [ K5 ]
#             [ K6 ]
#
# Dependencies (copy to /lib on CIRCUITPY):
#   - adafruit_hid  (from Adafruit CircuitPython bundle)
# -----------------------------------------------

import board
import busio
import digitalio
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# ── Matrix pin definitions ──────────────────────
ROW_PINS = [board.GP1, board.GP2, board.GP3]
COL_PINS = [board.GP4, board.GP5, board.GP6]

# ── Build row outputs ───────────────────────────
rows = []
for pin in ROW_PINS:
    r = digitalio.DigitalInOut(pin)
    r.direction = digitalio.Direction.OUTPUT
    r.value = True
    rows.append(r)

# ── Build col inputs with pull-up ───────────────
cols = []
for pin in COL_PINS:
    c = digitalio.DigitalInOut(pin)
    c.direction = digitalio.Direction.INPUT
    c.pull = digitalio.Pull.UP
    cols.append(c)

# ── HID setup ───────────────────────────────────
kbd = Keyboard(usb_hid.devices)

# ── Keymap ──────────────────────────────────────
# Matrix position → key action (list of Keycodes)
# Customise these to suit your workflow.
KEYMAP = [
    # Row 0
    [Keycode.F13],                          # K0
    [Keycode.F14],                          # K1
    [Keycode.F15],                          # K2
    # Row 1
    [Keycode.CONTROL, Keycode.Z],           # K3 — Undo
    [Keycode.CONTROL, Keycode.C],           # K4 — Copy
    [Keycode.CONTROL, Keycode.V],           # K5 — Paste
    # Row 2 (col 1 only for K6)
    [Keycode.CONTROL, Keycode.SHIFT, Keycode.S],  # K6 — Save As
]

# ── Debounce state ──────────────────────────────
DEBOUNCE_MS = 20
last_state = [False] * 7
last_change = [0] * 7

# ── Main loop ───────────────────────────────────
def scan():
    """Return list of 7 booleans — True if key is pressed."""
    pressed = []
    for row_idx, row in enumerate(rows):
        row.value = False                   # Drive row LOW
        time.sleep(0.001)                   # Settle
        for col_idx, col in enumerate(cols):
            # Only 7 keys: skip row2 col0 and row2 col2
            if row_idx == 2 and col_idx != 1:
                continue
            pressed.append(not col.value)  # Active-low
        row.value = True                    # Release row
    return pressed

print("7-Key Macropad ready.")

while True:
    now = time.monotonic_ns() // 1_000_000  # ms
    raw = scan()

    for idx, is_pressed in enumerate(raw):
        if is_pressed != last_state[idx]:
            if (now - last_change[idx]) >= DEBOUNCE_MS:
                last_state[idx] = is_pressed
                last_change[idx] = now
                keys = KEYMAP[idx]
                if is_pressed:
                    kbd.press(*keys)
                else:
                    kbd.release(*keys)

    time.sleep(0.001)
