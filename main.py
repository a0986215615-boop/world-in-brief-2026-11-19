"""Emit the finished World in Brief image to the contest output directory."""

from os import environ
from pathlib import Path
from shutil import copyfile


def main():
    artwork = Path(__file__).resolve().with_name("entry.png")
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    target = output / "entry.png"
    staging = target.with_suffix(".tmp")
    try:
        copyfile(artwork, staging)
        staging.replace(target)
    finally:
        staging.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
