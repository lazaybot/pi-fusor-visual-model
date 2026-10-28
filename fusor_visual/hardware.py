from __future__ import annotations

from .animation import VisualFrame


class NeoPixelOutput:
    """Optional output for a WS2812 ring. It never controls hazardous equipment."""

    def __init__(self, count: int = 24, gpio_pin: int = 18, brightness: int = 96) -> None:
        try:
            from rpi_ws281x import PixelStrip
        except ImportError as exc:
            raise RuntimeError("Install hardware support with: pip install -e '.[hardware]'") from exc
        self._brightness = max(0, min(255, brightness))
        self._strip = PixelStrip(count, gpio_pin, brightness=self._brightness)
        self._strip.begin()

    def show(self, frame: VisualFrame) -> None:
        from rpi_ws281x import Color

        for index, pixel in enumerate(frame.ring[: self._strip.numPixels()]):
            self._strip.setPixelColor(index, Color(pixel.red, pixel.green, pixel.blue))
        self._strip.show()

    def clear(self) -> None:
        from rpi_ws281x import Color

        for index in range(self._strip.numPixels()):
            self._strip.setPixelColor(index, Color(0, 0, 0))
        self._strip.show()
