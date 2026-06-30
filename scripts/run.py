#!/usr/bin/env python
import subprocess
import sys
from pathlib import Path


def run_cli():
    """Helper script to run the automation CLI."""
    base_dir = Path(__file__).resolve().parent.parent
    main_path = base_dir / "main.py"

    # Forward all arguments to main.py
    cmd = [sys.executable, str(main_path)] + sys.argv[1:]

    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[-] Interrupted by user.")
        sys.exit(0)


if __name__ == "__main__":
    run_cli()
