# Build Log 003 - Dual Joystick ADS1219 Prototype

**Date:** November 1, 2026  
**Stage:** Batch 1 - Controller Electronics  
**Status:** Four axes and both stick clicks tested successfully in MicroPython (bench prototype)

## Goal

Read two analog joysticks through one external ADS1219 ADC, using I2C to send the readings to an RP2040-Zero. Read both joystick click switches through separate digital GPIO inputs.

## Parts and tools

- Waveshare RP2040-Zero running MicroPython
- SparkFun Qwiic ADS1219 breakout with soldered male headers
- Two temporary analog joystick modules
- Breadboard and jumper wires
- Multimeter, soldering iron, solder
- Thonny

## Wiring

| Source | Destination |
|---|---|
| RP2040 3V3 | ADS1219 3V3, both joystick VCC pins (shared 3.3 V rail) |
| RP2040 GND | ADS1219 GND, both joystick GND pins (shared ground rail) |
| RP2040 GP4 | ADS1219 SDA |
| RP2040 GP5 | ADS1219 SCL |
| ADS1219 REFP | 3V3 supply |
| ADS1219 REFN | GND |
| ADS1219 AIN0 | Left joystick VRx |
| ADS1219 AIN1 | Left joystick VRy |
| ADS1219 AIN2 | Right joystick VRx |
| ADS1219 AIN3 | Right joystick VRy |
| RP2040 GP0 | Left joystick SW (active-low) |
| RP2040 GP1 | Right joystick SW (active-low) |

The joystick modules were supplied at **3.3 V**, despite their '+5V' labeling, to keep signal levels in range. The external ADC was at I2C address **0x40** for this MicroPython test.

## What happened

1. Soldered two 6-pin male headers to the ADS1219 breakout. Used continuity mode to check for a power-to-ground short before powering it.
2. Connected the ADS1219 to the RP2040 over I2C. The first scan found no device because the RP2040 was not fully seated; reseating it produced `['0x40']` reliably.
3. Tested the first joystick on AIN0/AIN1. An awkward breadboard placement made the signal wiring difficult; switched to direct female jumper connections on the soldered header pins.
4. Added the second joystick on AIN2/AIN3 and confirmed all four axes responded.
5. Both stick switches were verified: released = `1`, pressed = `0`.
6. Initial internal 2.048 V reference clipped joystick outputs at 2.048 V. Connected REFP to 3V3 and REFN to ground, then selected the external reference in the ADC configuration.
7. Confirmed both sticks' X axes reached approximately 0 V and 3.3 V, and both Y axes reached the full range during the movement tests.

Sample centered readings (approximately):

| Axis | Voltage |
|---|---:|
| Left X | 1.692 V |
| Left Y | 1.662 V |
| Right X | 1.655 V |
| Right Y | 1.697 V |

## Code

See [`firmware/dual_joystick_test.py`](../firmware/dual_joystick_test.py).

## Lessons learned

- Physical seating and wiring can cause seemingly software-related I2C errors.
- Power rails distribute 3.3 V and ground but are not automatically connected to signal rows.
- An ADC's voltage reference must match the voltage range of the sensor being measured.
- One I2C ADC can measure four joystick axes sequentially.

## Next steps

- Keep this MicroPython experiment as a reference, not the final gamepad firmware.
- Configure the ADS1219 address and external reference in the planned GP2040-CE integration. The build plan calls for a compatible address and firmware changes.
- Integrate ABXY/D-pad/shoulder buttons, analog triggers and rumble.
- Verify all inputs in a PC USB gamepad tester before moving beyond Batch 1.

The **handheld PC is not assembled** and the controller **does not yet operate as a USB gamepad**.
