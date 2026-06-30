# 🚀 Modular Automation Engine

A clean, extensible, and professional Python automation platform designed for educational curriculum training and real-world scripting.

This repository serves as a learning hub. Instead of creating a dozen tiny isolated scripts, students work inside this single, shared codebase. As they learn new topics—such as File System manipulations, Web APIs, Excel processing, Scheduling, DevOps, and Docker/Kubernetes—they implement respective modules and build onto this unified engine. This mimics a professional engineering environment where codebases grow incrementally over time.

---

## 📁 Repository Structure

```
automation-engine/
│
├── README.md               # Main instructions and course overview
├── LICENSE                 # MIT License details
├── .gitignore              # Ignores local setups, envs, logs and output files
├── requirements.txt        # Package dependencies
├── pyproject.toml          # Package metadata, Ruff and Pytest configuration
├── .env.example            # Sample environment configurations template
│
├── main.py                 # Application entry point (CLI dispatcher)
├── config.py               # Settings manager (loads env, creates folders)
├── engine.py               # Core task discovery and execution engine
├── cli.py                  # CLI framework using Typer and Rich console
│
├── automations/            # Student Task Implementations
│   ├── __init__.py
│   ├── files/              # File and directory manipulation tasks
│   ├── api/                # HTTP API requests, clients and health checks
│   ├── excel/              # Excel reading, writing, and custom worksheets
│   ├── email/              # SMTP mail sending and HTML templating
│   ├── docker/             # Container builds, execution, and cleanup
│   ├── git/                # Staging, committing, pushing automation
│   ├── kubernetes/         # Applying manifests, list pods, fetch logs
│   ├── scheduler/          # Cron-like job loop runners
│   ├── reports/            # Exporting data summaries to Excel/PDF/CSV
│   └── notifications/      # Webhook dispatches to Slack and Discord
│
├── core/                   # Shared System Utilities
│   ├── logger.py           # Pre-configured Rich stdout & rotating file logger
│   ├── utils.py            # Execution duration decorator, formatting helpers
│   ├── constants.py        # Global constants and domain namespaces
│   ├── exceptions.py       # Custom structured exceptions
│   └── helpers.py          # Domain-specific helpers
│
├── tests/                  # Pytest Unit Test Suite
│   ├── test_files.py
│   ├── test_api.py
│   └── test_engine.py
│
├── data/                   # Git-ignored folders for file testing
│   ├── input/              # Source directory for task files
│   ├── output/             # Destination directory for generated files
│   └── samples/            # Static sample files
│
├── logs/                   # Log output directory (app.log)
├── docs/                   # Additional documentation
│   ├── architecture.md     # System design walkthrough
│   ├── api.md              # Task template decorator reference
│   └── contributing.md     # Code style, testing, and PR submission guide
│
└── scripts/                # Helper setup and maintenance scripts
    ├── setup.py            # Pre-flight environment configuration
    ├── install.py          # Interactive pip dependency installer
    └── run.py              # Short-hand script to execute main.py
```

---

## 🛠️ Getting Started

Follow the guide below depending on your operating system to set up your virtual environment and install the dependencies.

### 🐧 Linux & macOS Setup Guide

1. **Create and Activate Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Initialize Configurations**:
   Runs the setup script to copy `.env.example` to `.env` and create missing workspace folders:
   ```bash
   python scripts/setup.py
   ```

3. **Install Dependencies**:
   Installs core requirements and hooks the project in editable mode for testing:
   ```bash
   python scripts/install.py
   ```

4. **Verify Installation**:
   Check if the CLI successfully loads the modules:
   ```bash
   python scripts/run.py list
   ```

---

### 🪟 Windows Setup Guide

1. **Create and Activate Virtual Environment**:
   *   **Using PowerShell**:
       ```powershell
       python -m venv .venv
       .venv\Scripts\Activate.ps1
       ```
   *   **Using Command Prompt (cmd)**:
       ```cmd
       python -m venv .venv
       .venv\Scripts\activate.bat
       ```

2. **Initialize Configurations**:
   ```cmd
   python scripts/setup.py
   ```

3. **Install Dependencies**:
   ```cmd
   python scripts/install.py
   ```

4. **Verify Installation**:
   ```cmd
   python scripts/run.py list
   ```

*(You will see a structured grid showing all the registered categories and skeleton tasks!)*

⚙️ Modular Dependency Options (For Low-Resource Environments)

Installing heavy packages like `kubernetes` or `pandas` is **NOT mandatory** for all students. The platform is designed to run dynamically, skipping modules with missing packages instead of crashing. 

Students can choose between two installation approaches:

#### Option A: Full Installation (For high-resource systems)
Installs every module dependency (including Kubernetes, Docker, and Pandas) to run the full suite:
```bash
python scripts/install.py
```

#### Option B: Modular/Core Installation (For low-resource or slow internet environments)
Students only install the lightweight core CLI requirements, and then install **only** their assigned team's dependencies:

1.  **Install Core Engine**:
    ```bash
    pip install -r requirements-core.txt
    ```
2.  **Install specific team extras (with developer testing tools)**:
    *   **Team 1 (Files)**: `pip install -e .[files,dev]`
    *   **Team 2 (API)**: `pip install -e .[api,dev]`
    *   **Team 3 (Excel)**: `pip install -e .[excel,dev]`
    *   **Team 4 (Email)**: `pip install -e .[dev]` (No extra packages needed)
    *   **Team 5 (Docker)**: `pip install -e .[docker,dev]`
    *   **Team 6 (Git)**: `pip install -e .[git,dev]`
    *   **Team 7 (Kubernetes)**: `pip install -e .[kubernetes,dev]` (Only Team 7 downloads the `kubernetes` package!)
    *   **Team 8 (Scheduler)**: `pip install -e .[dev]`
    *   **Team 9 (Reports)**: `pip install -e .[pdf,excel,dev]`
    *   **Team 10 (Alerts)**: `pip install -e .[slack,dev]`

*(If a student has not installed Kubernetes, the engine will safely print a warning during discovery and continue running all other tasks normally!)*

---

## 👥 Team Assignments

Each student team is assigned to a specific folder under this repository. Each team is only responsible for their folder's automation scripts, unit tests, and design guidelines. The repository owner (instructor) has set up the core scaffolding and base configuration; teams should write their code inside their designated directories.

| Team    | Target Folder                  | Automation Scope |
| ------- | ------------------------------ | ---------------- |
| **Team 1**  | `automations/files/`           | File organization, compression backups, temp cleanup, file watchers |
| **Team 2**  | `automations/api/`             | Standard HTTP API integrations, request client base, status checks |
| **Team 3**  | `automations/excel/`           | Reading worksheets, formatting data, exporting reports using pandas |
| **Team 4**  | `automations/email/`           | Dispatching email attachments, drafting HTML templating engine |
| **Team 5**  | `automations/docker/`          | Container lifecycle build operations, starting processes, pruning resources |
| **Team 6**  | `automations/git/`             | Git actions, automatic commits, push scripts, workspace checking |
| **Team 7**  | `automations/kubernetes/`      | Resource manifest validation, service deployment, fetching cluster pod logs |
| **Team 8**  | `automations/scheduler/`       | Loop scheduling configuration (daily, weekly, hourly jobs runner) |
| **Team 9**  | `automations/reports/`         | Generating exports and formatting charts inside PDF, CSV, and Excel |
| **Team 10** | `automations/notifications/`   | Real-time alerts using Slack Webhooks and Discord server webhooks |
| **Team 11** | `core/`                        | Shared configurations, loggers, timing decorators, and base exceptions |
| **Team 12** | `tests/`                       | Integration mock suites, testing coverage runner scripts |

---

## 📚 Course Modules & Student Assignments

Each subfolder inside `automations/` represents a learning unit. Students will implement the code within these files based on the docstring instructions.

### 1. 📂 File Automations (`automations/files/`)
Focuses on local OS operations, file system paths, compression, and event watching.
*   **`organizer.py`**: Sort raw files in a directory into structured subfolders (e.g., `.pdf` goes to `Documents/`, `.zip` goes to `Archives/`).
*   **`backup.py`**: Compress a folder into a timestamped zip archive and verify its output size.
*   **`cleanup.py`**: Find and delete temporary files or logs older than $X$ days.
*   **`watcher.py`**: Use `python-watchdog` to monitor a directory in real-time and alert on new creations.

### 2. 🔌 API Integration (`automations/api/`)
Teaches web protocols, REST API design, headers, query parameters, authentication, and HTTP clients.
*   **`client.py`**: Write a reusable HTTP Client using `requests` or `httpx` with request/response logging and retry logic.
*   **`health.py`**: Probe status endpoints of an API, validating latency and status code.
*   **`fetch.py`**: Extract payloads from a public API (e.g., weather or user data) and serialize it locally.
*   **`upload.py`**: Read a local CSV/JSON file and POST it as a JSON payload to a remote server.

### 3. 📊 Excel Processing (`automations/excel/`)
Introduces data manipulation, tabular logic, and reporting.
*   **`reader.py`**: Read raw worksheets and dump them as Python lists of dictionaries.
*   **`writer.py`**: Export dynamic database records into standard columns and auto-fit column sizes.
*   **`reports.py`**: Use Pandas to create aggregated pivot-style metrics out of raw lists.

### 4. ✉️ Email Operations (`automations/email/`)
Builds automated communication flows.
*   **`sender.py`**: Open secure SMTP sockets to forward messages, handling both rich HTML templates and document attachments.
*   **`templates.py`**: Implement a simple string template compiler to render variables inside static templates.

### 5. 🐳 Container Operations (`automations/docker/`)
Bridge standard scripting and modern DevOps practices using the Docker SDK.
*   **`build.py`**: Build a docker image by streaming logs from a target Dockerfile path.
*   **`run.py`**: Launch containers programmatically, configuring env variables and local port bindings.
*   **`cleanup.py`**: Prune unused networks, stopped containers, and dangling images.

### 6. 🐙 Git Integration (`automations/git/`)
Automates routine code management using `GitPython`.
*   **`status.py`**: Check if the working tree has uncommitted adjustments.
*   **`commit.py`**: Stage changes and execute commits with standardized message structures.
*   **`push.py`**: Publish local changes to remote repository branches.

### 7. ☸️ Kubernetes (`automations/kubernetes/`)
Introduces Cloud Native orchestration through python-kubernetes.
*   **`deploy.py`**: Apply YAML deployments and services to a namespace.
*   **`pods.py`**: Query current state and statuses of pods.
*   **`logs.py`**: Fetch, filter, and store diagnostic logs from running pods.

### 8. ⏰ Task Scheduling (`automations/scheduler/`)
Teaches persistent system processes and loop execution.
*   **`jobs.py`**: Standard scheduler loop runner that calls scheduled tasks.
*   **`schedule.py`**: Configure periodic rules (e.g. daily, weekly, or specific weekdays) dynamically.

### 9. 📈 Report Export (`automations/reports/`)
Focuses on serialization and document compilation.
*   **`csv.py`**: Convert raw API logs into clean CSV worksheets.
*   **`pdf.py`**: Build stylized PDF invoices or summaries utilizing ReportLab.
*   **`excel.py`**: Compile transaction sheets with charts.

### 10. 🔔 Alerting (`automations/notifications/`)
Webhooks integration for real-time notifications.
*   **`slack.py`**: Push structured block layouts to Slack webhooks.
*   **`discord.py`**: Dispatch formatted webhook embeds to Discord channels.
*   **`email.py`**: Route high-level server alerts to standard administrators.

---

## 🖥️ Running Automations Guide

The core execution engine dynamically discovers, registers, and routes tasks. Below is the comprehensive guide on listing, invoking, and parameterizing your automation routines.

### 1. Listing Available Automations
The engine dynamically scans the `automations/` package, executes the registration decorators, and prints a structured grid of all active commands:
```bash
python scripts/run.py list
```

### 2. Testing All Tasks (Task Verification Run-All)
Instructors and students can run all registered tasks at once to audit implementation coverage. The engine will inspect signatures, pass placeholder credentials, and return a summary of which tasks are implemented vs not implemented:
```bash
python scripts/run.py run-all
```

### 3. CLI Command Mapping Guide (Using Git Commit Example)

If you are not sure how the CLI syntax routes to your Python code, here is a step-by-step breakdown using the **Git Commit** automation task.

#### Step 1: Inspect the Python task function in the code:
Open `automations/git/commit.py` and look at the registration decorator and function definition:
```python
@register_task(
    name="commit",
    category="git",
    description="Stages changes and commits them..."
)
def git_commit(repo_path: str, message: str):
    ...
```

#### Step 2: Extract the CLI terms from the code:
*   **Category Name**: Comes from the decorator's `category="git"` property $\rightarrow$ **`git`**
*   **Task Name**: Comes from the decorator's `name="commit"` property $\rightarrow$ **`commit`**
*   **Parameters**: The function parameters (`repo_path` and `message`) must be provided as `key=value` pairs:
    *   `repo_path=.` (sets the path to the current directory)
    *   `message="initial skeleton"` (sets the commit message)

#### Step 3: Construct the final command:
Run the script passing your parameters:
```bash
python scripts/run.py run git commit repo_path=. message="initial skeleton"
```

---

### 3. Dynamic Parameter Parsing & Casting
Arguments passed via the command line are dynamically parsed by the engine and cast to Python types matching the target function's parameter expectations:
*   **Booleans**: `verify=true` or `verify=false` are automatically parsed into Python `True` or `False`.
*   **Integers**: `days=10` is automatically cast to a Python `int`.
*   **Floats**: `threshold=1.5` is cast to a Python `float`.
*   **Strings**: Anything else (e.g. `path=data/input`) is parsed as a standard Python `str`.

---

### 4. Complete CLI Execution Cheat Sheet

Once your team has written the module code, run and test your specific tasks using the exact CLI patterns below:

#### 📂 Team 1 — File Systems (`files`)
```bash
# organizer.py (Organize directory files into type subfolders)
python scripts/run.py run files organize directory_path=data/input

# backup.py (ZIP compress folder contents to target destination)
python scripts/run.py run files backup source_dir=data/input dest_dir=data/output

# cleanup.py (Clear old temporary log files)
python scripts/run.py run files cleanup directory_path=data/input days=7

# watcher.py (Monitor file creations in real time)
python scripts/run.py run files watch directory_path=data/input
```

#### 🔌 Team 2 — HTTP API Integration (`api`)
```bash
# health.py (Status ping endpoint check)
python scripts/run.py run api health url=https://api.github.com

# fetch.py (Fetch API data and export to JSON)
python scripts/run.py run api fetch endpoint=users output_filename=users.json

# upload.py (Post JSON payload to API endpoint)
python scripts/run.py run api upload file_path=data/output/users.json endpoint=upload
```

#### 📊 Team 3 — Excel Processing (`excel`)
```bash
# reader.py (Load worksheets into dict lists)
python scripts/run.py run excel read file_path=data/samples/sales.xlsx sheet_name=Sheet1

# writer.py (Save datasets to excel columns)
python scripts/run.py run excel write file_path=data/output/output.xlsx data="[{'a': 1}]"

# reports.py (Aggregate pivot summaries)
python scripts/run.py run excel reports source_file=data/samples/sales.xlsx dest_file=data/output/summary.xlsx
```

#### ✉️ Team 4 — Email Operations (`email`)
```bash
# sender.py (Send email via SMTP server configuration)
python scripts/run.py run email send to_email=recipient@example.com subject="Platform Alert" body="Test message"
```

#### 🐳 Team 5 — Docker Services (`docker`)
```bash
# build.py (Build docker image from Dockerfile context)
python scripts/run.py run docker build path=. tag=test-image:latest

# run.py (Launch port-bound container instance)
python scripts/run.py run docker run image_tag=test-image:latest container_name=test-container

# cleanup.py (Prune stopped nodes and unused volumes)
python scripts/run.py run docker cleanup
```

#### 🐙 Team 6 — Git Workflows (`git`)
```bash
# status.py (Get local git workspace status)
python scripts/run.py run git status repo_path=.

# commit.py (Stage changes and commit them)
python scripts/run.py run git commit repo_path=. message="chore: update workflows"

# push.py (Push branches upstream to remote origin)
python scripts/run.py run git push repo_path=. remote=origin branch=main
```

#### ☸️ Team 7 — Kubernetes Clusters (`kubernetes`)
```bash
# deploy.py (Apply YAML deployment/service manifests)
python scripts/run.py run kubernetes deploy manifest_path=data/samples/pod.yaml namespace=default

# pods.py (List running namespace pods)
python scripts/run.py run kubernetes pods namespace=default

# logs.py (Collect logs of running pod)
python scripts/run.py run kubernetes logs pod_name=my-pod namespace=default output_file=logs/pod.log
```

#### ⏰ Team 8 — Persisted Scheduling (`scheduler`)
```bash
# jobs.py (Run main loop schedule heartbeat checks)
python scripts/run.py run scheduler run_jobs interval_seconds=10

# schedule.py (Schedules a task to run daily/weekly)
python scripts/run.py run scheduler schedule task_name=api:health interval=daily time_of_day=10:00
```

#### 📈 Team 9 — Report Serialization (`reports`)
```bash
# csv.py (Convert JSON records to CSV)
python scripts/run.py run reports csv input_file=data/output/users.json output_file=data/output/report.csv

# pdf.py (Generate styled ReportLab PDF sheets)
python scripts/run.py run reports pdf title="System Report" content_lines="['Line A', 'Line B']" output_file=data/output/report.pdf

# excel.py (Save sheets with custom charts)
python scripts/run.py run reports excel data_source=data/output/users.json output_file=data/output/analytics.xlsx
```

#### 🔔 Team 10 — Channels Alerting (`notifications`)
```bash
# slack.py (Webhook post alerts to Slack)
python scripts/run.py run notifications slack message="Server overload detected!"

# discord.py (Webhook warning embeds to Discord)
python scripts/run.py run notifications discord message="Backup failed!"

# email.py (Forward SMTP alert notifications to administrator)
python scripts/run.py run notifications email subject="Disk Status" message="90% full"
```

---

### 5. Reading Output Logs & Execution Audits
The engine automatically intercepts all executions to measure performance, enforce errors, and log results.
*   **Timing Audits**: Every run logs execution time to the millisecond (e.g., `Task organize completed in 0.0037s`).
*   **Log Storage**: Detailed output logs (including tracebacks in case of failures) are persistently archived inside `logs/app.log`. Look there to debug exceptions!

---

## 🧪 Testing & Code Quality

Professional codebases maintain strict validation routines. Before pushing code or creating pull requests, make sure tests pass and formatting is correct.

### Running Lint Checks (Ruff)
Ruff verifies code formatting and flags patterns:
```bash
# Run styling audit
ruff check .

# Automatically fix format warnings
ruff format .
```

### Running Unit Tests (Pytest)
Pytest executes assertions against helper routines and student modules:
```bash
# Run all project tests:
pytest

# Run tests for specific modules (Team 12):
pytest tests/test_files.py     # Check Files category
pytest tests/test_api.py       # Check API category
pytest tests/test_engine.py    # Check Engine framework loader
```

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
