from pathlib import Path
import os


JOKE = (
    "My AI coding agent finally passed its performance review: "
    "it closed every ticket by rewriting the requirements to match its output."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
