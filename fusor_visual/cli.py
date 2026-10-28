from __future__ import annotations

import argparse
import json
from pathlib import Path
from time import monotonic, sleep

from .animation import generate_frame
from .render import save_preview


def main() -> None:
    parser = argparse.ArgumentParser(description="Safe Raspberry Pi fusor visual imitation")
    parser.add_argument("--hardware", action="store_true", help="drive an LED ring on GPIO18")
    parser.add_argument("--duration", type=float, default=30.0)
    parser.add_argument("--fps", type=float, default=20.0)
    parser.add_argument("--pixels", type=int, default=24)
    parser.add_argument("--preview", type=Path, help="save a still preview PNG")
    args = parser.parse_args()
    if args.duration <= 0 or args.fps <= 0:
        raise SystemExit("duration and fps must be positive")
    if args.preview:
        save_preview(args.preview, 34.0, args.pixels)
    output = None
    if args.hardware:
        from .hardware import NeoPixelOutput
        output = NeoPixelOutput(args.pixels)
    start = monotonic()
    frames = 0
    last = generate_frame(0, args.pixels)
    try:
        while monotonic() - start < args.duration:
            now = monotonic() - start
            last = generate_frame(now, args.pixels)
            if output:
                output.show(last)
            frames += 1
            sleep(1 / args.fps)
    finally:
        if output:
            output.clear()
    print(json.dumps({
        "mode": "LED hardware" if args.hardware else "simulation",
        "frames": frames,
        "final_pressure_normalized": last.pressure_normalized,
        "final_glow_normalized": last.glow_normalized,
        "hazardous_outputs": False,
    }, indent=2))


if __name__ == "__main__":
    main()
