import unittest

from fusor_visual.animation import Pixel, generate_frame, simulated_pressure


class VisualTests(unittest.TestCase):
    def test_pressure_falls_toward_display_floor(self):
        self.assertGreater(simulated_pressure(0), simulated_pressure(30))
        self.assertGreaterEqual(simulated_pressure(1000), 0.08)

    def test_frame_is_deterministic(self):
        self.assertEqual(generate_frame(12.5), generate_frame(12.5))

    def test_frame_respects_pixel_count_and_brightness_limit(self):
        frame = generate_frame(24, 16)
        self.assertEqual(len(frame.ring), 16)
        self.assertTrue(all(max(pixel.red, pixel.green, pixel.blue) <= 96 for pixel in frame.ring))

    def test_pixel_limiter_preserves_color_ratio(self):
        limited = Pixel(200, 100, 50).limited(100)
        self.assertEqual(limited, Pixel(100, 50, 25))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            generate_frame(0, 0)
        with self.assertRaises(ValueError):
            simulated_pressure(-1)


if __name__ == "__main__":
    unittest.main()
