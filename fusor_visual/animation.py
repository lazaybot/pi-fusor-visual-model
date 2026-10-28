from __future__ import annotations

from dataclasses import dataclass
from math import exp, pi, sin
from random import Random


@dataclass(frozen=True)
class Pixel:
    red: int
    green: int
    blue: int

    def limited(self, maximum: int = 96) -> "Pixel":
        peak = max(self.red, self.green, self.blue, 1)
        scale = min(1.0, maximum / peak)
        return Pixel(int(self.red * scale), int(self.green * scale), int(self.blue * scale))


@dataclass(frozen=True)
class VisualFrame:
    time_s: float
    pressure_normalized: float
    glow_normalized: float
    ring: tuple[Pixel, ...]


def simulated_pressure(time_s: float, floor: float = 0.08) -> float:
    if time_s < 0:
        raise ValueError("time cannot be negative")
    return floor + (1.0 - floor) * exp(-time_s / 18.0)


def generate_frame(time_s: float, pixels: int = 24, seed: int = 7) -> VisualFrame:
    if pixels <= 0:
        raise ValueError("pixels must be positive")
    pressure = simulated_pressure(time_s)
    # Brightness rises only in a middle display band. This is artistic, not physics.
    glow = max(0.0, 1.0 - abs(pressure - 0.22) / 0.22)
    random = Random(seed + int(time_s * 20))
    values: list[Pixel] = []
    for index in range(pixels):
        angle = 2 * pi * index / pixels
        spoke = 0.55 + 0.45 * max(0.0, sin(4 * angle + time_s * 2.5))
        flicker = 0.85 + 0.15 * random.random()
        intensity = glow * spoke * flicker
        values.append(Pixel(int(150 * intensity), int(45 * intensity), int(255 * intensity)).limited())
    return VisualFrame(time_s, pressure, glow, tuple(values))
