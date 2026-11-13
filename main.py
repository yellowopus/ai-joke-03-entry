"""Joke generator poking fun at an AI coding agent that costs more than it accomplishes."""

from pathlib import Path
import os


def main() -> None:
    joke = "Bought a $200/mo AI coding agent; it burned $500 in tokens centering a div, then asked for a raise."
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
