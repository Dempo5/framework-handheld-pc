# Build Log 001 - First Physical Button Input

**Date:** October 30, 2026
**Stage:** Batch 1 - Controller Prototype
**Result:** Successful

## Objective

Connect a physical tactile button to an RP2040-Zero and detect button presses using MicroPython.

## Components

- Waveshare RP2040-Zero
- Breadboard
- 4-pin tactile pushbutton
- Jumper wires
- Digital multimeter
- USB-C data cable

## Software

- Thonny
- MicroPython

## What I Did

I started by learning how breadboard connections work using the continuity setting on my multimeter.

I then tested a tactile button to understand which pins were connected when pressed.

My first attempts at connecting the button to the RP2040 did not work correctly.

After troubleshooting the wiring, I discovered that the button's internal connections were causing the GPIO input to remain LOW.

I tested different breadboard positions until the multimeter only beeped when the button was pressed.

I then connected the button to GPIO0 and GND.

## MicroPython Code

```python
from machine import Pin
from time import sleep

button = Pin(0, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    sleep(0.5)
```

## Results

The RP2040 successfully detected the external button input.

- Button released: 1
- Button pressed: 0

The program displayed changing values in the Thonny shell.

## What I Learned

- How breadboard rows are connected
- How to use a multimeter for continuity testing
- How a tactile switch works internally
- How GPIO inputs work
- How internal pull-up resistors work
- How to troubleshoot incorrect electrical connections

## Next Steps

- Test joystick movement
- Connect additional buttons
- Learn analog inputs
- Continue developing the controller prototype

## Project Status

First external physical input working successfully.

The controller is not yet functioning as a USB gamepad.
