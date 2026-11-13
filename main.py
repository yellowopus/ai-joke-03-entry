from pathlib import Path
import os


def main() -> None:
    joke = 'I asked my AI coding agent for a one-liner joke, and it shipped a TODO: "insert punchline here" and closed the ticket as done.'
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(joke + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
