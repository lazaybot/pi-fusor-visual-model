# Pi Fusor Visual Model

A safe Raspberry Pi exhibit that imitates the appearance and instrument display
of a Farnsworth–Hirsch fusor using a low-voltage addressable LED ring and
synthetic telemetry. It creates no plasma, fusion reaction, neutron source,
X-ray source, vacuum, or hazardous high voltage.

Any visible display necessarily emits ordinary visible photons. In this project
they come from LEDs or a screen—not plasma or ionizing radiation.

## What it demonstrates

- A deterministic visual “plasma” animation with four moving spokes
- A synthetic pumpdown-style curve in normalized, non-operational units
- A screen preview and optional WS2812 LED-ring output
- Strict brightness limiting and automatic LED clearing on exit
- Software simulation that runs without Raspberry Pi hardware
- Unit tests for repeatability, input checks, and output limits

The animation is an artistic science exhibit, not a plasma-physics simulation
and not evidence that a real fusor was constructed or operated.

## Run the simulator

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,plot]'
fusor-visual --duration 2 --preview outputs/preview.png
python -m unittest discover -s tests -v
```

## Run the LED model on Raspberry Pi

Complete [PARTS.md](PARTS.md), [WIRING.md](WIRING.md), and
[ASSEMBLY.md](ASSEMBLY.md) first, then:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[hardware]'
sudo .venv/bin/fusor-visual --hardware --duration 60
```

## Architecture

```text
Raspberry Pi animation ──> 3.3 V logic ──> 74AHCT125 level shifter
                                            │
5 V regulated supply ─────────────────> WS2812 LED ring

Raspberry Pi HDMI ─────────────────────> optional telemetry screen
```

There is no connection for a vacuum pump, gas supply, electrode, transformer,
high-voltage supply, radiation detector, or physical fusor.

## Safety boundary

This repository intentionally contains no real-fusor construction, operating,
or high-voltage instructions. A physical fusor can involve lethal voltage,
vacuum implosion, X-rays, and potentially neutrons. Do not modify this exhibit
into an energized vacuum apparatus.

## License

BSD-3-Clause.
