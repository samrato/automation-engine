#!/usr/bin/env python
import subprocess
import sys


def install_dependencies():
    """Installs pip dependencies and package in editable mode."""
    print("=== Installing Dependencies ===")

    try:
        # Install requirements.txt
        print("[+] Installing packages from requirements.txt...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
            check=True,
        )

        # Install development package
        print("[+] Installing package in editable mode with dev dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-e", ".[dev]"], check=True)

        print("\n[✓] All dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\n[!] Error during installation: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    install_dependencies()
