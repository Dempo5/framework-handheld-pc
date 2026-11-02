# Framework Handheld Gaming PC

A custom handheld gaming PC built around a Framework 13 mainboard, custom controller electronics, and a custom-designed enclosure.

## Project Goals

- 7-inch 1080p 120Hz display
- Framework mainboard
- Custom RP2040-based controller PCB
- Analog joysticks and Hall-effect triggers
- Rumble motors and back buttons
- Retail-quality enclosure
- Target size: 290 x 121 mm
- Target weight: 740g or less

## Development Roadmap

1. Controller electronics and firmware
2. Enclosure design and size testing
3. Framework mainboard integration
4. Display integration
5. Battery and audio integration
6. Final PCB and enclosure assembly

## Current Progress

**Batch 1 - Controller Prototype**

- [x] Program RP2040-Zero using MicroPython
- [x] Test onboard LED
- [x] Learn breadboard connections
- [x] Test tactile button with multimeter
- [x] Read button presses using GPIO0
- [x] Read analog joystick inputs with ADS1219 (both sticks, four axes)
- [x] Test both joystick click switches (GP0 and GP1)
- [ ] Test multiple buttons
- [ ] Test analog triggers
- [ ] Test rumble motors
- [ ] Test complete controller on PC

## Build Logs

- [October 30, 2026 - First Button Input](build-logs/2026-10-30-first-button-input.md)
- [October 30, 2026 - First Analog Joystick](build-logs/2026-10-30-joystick-xy.md)
- [November 1, 2026 - Dual Joystick ADS1219 Prototype](build-logs/2026-11-01-dual-joystick-ads1219.md)

## Tools

MicroPython, Thonny, Fusion 360, KiCad, Git, and GitHub.

## Status

Early electronics prototyping. The full handheld has not been assembled yet.
