from __future__ import annotations

from pathlib import Path

from .animation import generate_frame


def save_preview(path: Path, time_s: float = 24.0, pixels: int = 24) -> None:
    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise RuntimeError("Install preview support with: pip install -e '.[plot]'") from exc
    frame = generate_frame(time_s, pixels)
    figure, (chamber, telemetry) = plt.subplots(1, 2, figsize=(10, 5), facecolor="#060812")
    for axis in (chamber, telemetry):
        axis.set_facecolor("#060812")
    angles = [2 * 3.141592653589793 * index / pixels for index in range(pixels)]
    xs = [0.9 * __import__("math").cos(angle) for angle in angles]
    ys = [0.9 * __import__("math").sin(angle) for angle in angles]
    colors = [(p.red / 255, p.green / 255, p.blue / 255) for p in frame.ring]
    chamber.scatter(xs, ys, s=250, c=colors)
    chamber.scatter([0], [0], s=900, c=[(0.40, 0.08, 0.85)], alpha=0.55)
    for spoke in range(4):
        angle = spoke * 3.141592653589793 / 4
        chamber.plot([-0.7 * __import__("math").cos(angle), 0.7 * __import__("math").cos(angle)],
                     [-0.7 * __import__("math").sin(angle), 0.7 * __import__("math").sin(angle)],
                     color="#a95cff", linewidth=4, alpha=0.55)
    chamber.add_patch(plt.Circle((0, 0), 1.05, fill=False, color="#a9c7ff", linewidth=2))
    chamber.set_aspect("equal")
    chamber.axis("off")
    chamber.set_title("LED chamber imitation", color="white")
    times = list(range(0, 61))
    pressures = [generate_frame(float(t), pixels).pressure_normalized for t in times]
    glows = [generate_frame(float(t), pixels).glow_normalized for t in times]
    telemetry.plot(times, pressures, label="synthetic pressure", color="#52d8ff")
    telemetry.plot(times, glows, label="visual glow", color="#b862ff")
    telemetry.axvline(time_s, color="white", linestyle="--", alpha=0.6)
    telemetry.set_xlabel("simulation time (s)", color="white")
    telemetry.set_ylabel("normalized value", color="white")
    telemetry.tick_params(colors="white")
    telemetry.legend(facecolor="#10162b", labelcolor="white")
    telemetry.grid(alpha=0.15)
    figure.suptitle("Pi Fusor Visual Model — no plasma or ionizing radiation", color="white", fontsize=15)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, dpi=160, bbox_inches="tight", facecolor=figure.get_facecolor())
    plt.close(figure)
