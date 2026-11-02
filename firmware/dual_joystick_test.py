"""Batch 1 bench test: dual joysticks read through an ADS1219 via I2C.

Wiring:
  ADS1219 3V3/GND -> RP2040 3V3/GND (shared 3.3 V supply)
  ADS1219 SDA/SCL -> RP2040 GP4/GP5
  ADS1219 REFP/REFN -> 3V3/GND (external voltage reference)
  ADS1219 AIN0/AIN1 -> left joystick VRx/VRy
  ADS1219 AIN2/AIN3 -> right joystick VRx/VRy
  Left/right joystick SW -> RP2040 GP0/GP1
  Joystick VCC/GND -> shared 3.3 V/GND, not 5 V

This is a slow MicroPython bench test, not USB gamepad firmware.
"""

from machine import Pin, I2C
from time import sleep_ms

# ADS1219 communication
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)
address = 0x40

# Joystick buttons (active-low)
left_button = Pin(0, Pin.IN, Pin.PULL_UP)
right_button = Pin(1, Pin.IN, Pin.PULL_UP)

# Reset ADS1219
i2c.writeto(address, bytes([0x06]))
sleep_ms(20)


def read_axis(config):
    # Configure selected input channel and use external 3.3 V reference.
    i2c.writeto(address, bytes([0x40, config | 0x01]))

    # Single-shot conversion
    i2c.writeto(address, bytes([0x08]))
    sleep_ms(120)

    # Read signed 24-bit result
    i2c.writeto(address, bytes([0x10]), False)
    data = i2c.readfrom(address, 3)

    raw = (data[0] << 16) | (data[1] << 8) | data[2]
    if raw & 0x800000:
        raw -= 1 << 24

    return round(raw * 3.3 / 8388608, 3)


while True:
    lx = read_axis(0x60)  # Left joystick X, AIN0
    ly = read_axis(0x80)  # Left joystick Y, AIN1
    rx = read_axis(0xA0)  # Right joystick X, AIN2
    ry = read_axis(0xC0)  # Right joystick Y, AIN3

    print("LEFT:", lx, ly, left_button.value())
    print("RIGHT:", rx, ry, right_button.value())
    print("-------------------------")

    sleep_ms(100)
