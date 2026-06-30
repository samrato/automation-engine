#!/usr/bin/env python
import shutil
import sys
from pathlib import Path


def setup_project():
    """Sets up the initial project environment."""
    base_dir = Path(__file__).resolve().parent.parent

    print("=== Automation Engine Setup ===")

    # 1. Copy .env.example to .env
    env_example = base_dir / ".env.example"
    env_file = base_dir / ".env"

    if env_file.exists():
        print("[-] .env file already exists. Skipping copy.")
    else:
        if env_example.exists():
            shutil.copy(env_example, env_file)
            print("[+] Created .env file from .env.example")
        else:
            print("[!] Error: .env.example not found!", file=sys.stderr)
            sys.exit(1)

    # 2. Create required directories
    directories = ["data/input", "data/output", "data/samples", "logs"]

    for dir_name in directories:
        dir_path = base_dir / dir_name
        if not dir_path.exists():
            dir_path.mkdir(parents=True, exist_ok=True)
            # Create a .gitkeep if not existing
            gitkeep_path = dir_path / ".gitkeep"
            gitkeep_path.touch()
            print(f"[+] Created directory: {dir_name}")
        else:
            print(f"[-] Directory already exists: {dir_name}")

    print("\n[✓] Setup complete! You can now edit '.env' and run 'pip install -r requirements.txt'")


if __name__ == "__main__":
    setup_project()
