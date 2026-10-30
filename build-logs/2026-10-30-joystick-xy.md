# Build Log 002 - First Analog Joystick

**Date:** October 30, 2026
**Stage:** Batch 1 - Controller Prototype
**Result:** Successful

## Objective

Connect an analog joystick to the RP2040-Zero and read horizontal and vertical movement using MicroPython.

## Components

- Waveshare RP2040-Zero
- Two-axis analog joystick module
- Female-to-female jumper wires
- USB-C cable

## Wiring

| Joystick | RP2040 |
|---|---|
| GND | GND |
| VCC | 3V3 |
| VRx | GP26 |
| VRy | GP27 |

## MicroPython Code

```python
from machine import ADC, Pin
from time import sleep

joystick_x = ADC(Pin(26))
joystick_y = ADC(Pin(27))

while True:
    x = joystick_x.read_u16()
    y = joystick_y.read_u16()

    print("X:", x, "Y:", y)
    sleep(0.2)
```

## Results

Both joystick axes successfully reported movement.

Initial X-axis observations:
- Center: approximately 33,750
- Full left: approximately 224-272
- Full right: near the upper end of the ADC range

The joystick returned values toward the middle when released.

The RP2040 successfully read X and Y simultaneously.

## What I Learned

- How analog inputs differ from digital inputs
- How an ADC converts voltage into digital readings
- How to read two analog inputs using MicroPython
- Why real-world joystick readings may not reach exact minimum or maximum values

## Next Steps

- Test the joystick's built-in pushbutton
- Test a second joystick
- Eventually integrate controller firmware
