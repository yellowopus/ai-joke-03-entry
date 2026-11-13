"""A satirical dig at AI coding agents that burn compute on trivial bugs, then scope-creep into needless refactors."""

from pathlib import Path
import os


def main() -> None:
    joke = "My AI coding agent burned $42 in tokens to fix a bug that cost $0.03, then suggested we refactor the whole codebase as a side quest."
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
