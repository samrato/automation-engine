# Contributing Guidelines for Students

Welcome! As a student, you will be implementing and extending modules in this repository. To keep the repository professional and clean, please follow these guidelines.

## Development Setup

1. **Clone the Repository**:
   ```bash
   git clone <your-fork-or-repo-url>
   cd automation-engine
   ```

2. **Initialize Environment**:
   Run the setup script to copy environment configurations and establish required folders:
   ```bash
   python scripts/setup.py
   ```

3. **Install Dependencies**:
   Install the required libraries and register this module locally in editable mode:
   ```bash
   python scripts/install.py
   ```

## Workflow Checklist

### 1. Formatting and Style
We use **Ruff** for checking lint issues and formatting files. Before pushing your changes:
```bash
# Check code style errors
ruff check .

# Automatically apply formatting fixes
ruff format .
```

### 2. Testing Your Task
Every automation should have a corresponding test under the `tests/` directory. Use **pytest** to verify your tasks:
```bash
# Run all tests
pytest

# Run tests with output logs
pytest -s
```

### 3. Submitting Pull Requests
- Keep your changes limited to your assigned file (e.g., `automations/files/organizer.py`).
- Do not commit your personal `.env` files to git.
- Write a clear, concise commit message.
- Verify that the GitHub Actions continuous integration (CI) tests pass successfully on your PR.
