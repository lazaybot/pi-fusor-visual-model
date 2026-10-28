# Low-voltage wiring

Power off the system before changing wires.

1. Connect Raspberry Pi GPIO18 to a 74AHCT125 input.
2. Power the 74AHCT125 from the regulated 5 V rail and connect its ground.
3. Connect the level-shifter output through a 330–470 Ω resistor to LED `DIN`.
4. Connect the LED ring to the external regulated 5 V supply.
5. Connect the Raspberry Pi, level shifter, LED ring, and supply grounds.
6. Place the 1000 µF capacitor across LED 5 V and ground with correct polarity.

Do not power a large LED ring from the Pi 3.3 V pin. Limit brightness in software
and size the supply for the selected pixel count. Cover all exposed conductors.

## Explicitly absent connections

There are no high-voltage, vacuum-pump, gas-valve, chamber, radiation-detector,
or electrode connections. If a proposed change adds one, it is outside this
project's safety boundary.
