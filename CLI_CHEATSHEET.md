# 📖 CLI Cheat Sheet & Execution Guide

This reference guide provides a complete overview of the commands used to list, test, and run the various automation tasks on this platform.

---

## 🖥️ Central Runner Commands

### 1. List Available Tasks
Scans all modules under the `automations/` folder, registers active task decorators, and prints a formatted category table:
```bash
python scripts/run.py list
```

### 2. Verify Tasks Status (Run-All)
Runs all registered tasks sequentially to check which student teams have completed their assignments:
```bash
python scripts/run.py run-all
```

#### Expected Run-All Outputs:
*   **`❌ Not Implemented`**: The task was registered, but the code still raises `NotImplementedError` (default skeleton state).
*   **`✅ Implemented (Success)`**: The task executed successfully without errors.
*   **`✅ Implemented (Needs Parameters / Log Error)`**: The task logic was entered, but it failed due to missing credentials, connection issues, or missing files. *(This indicates the student has replaced the `NotImplementedError` with actual logic!)*

---

## 📁 Cheat Sheet: Individual Automations Commands

Run your specific team tasks by passing their required parameters in `key=value` format:

### 📂 Team 1 — File Systems (`files`)
```bash
# organizer.py (Organize directory files into folders based on file extensions)
python scripts/run.py run files organize directory_path=data/input

# backup.py (Compress folder contents into a timestamped ZIP archive)
python scripts/run.py run files backup source_dir=data/input dest_dir=data/output

# cleanup.py (Remove files in a folder older than X days)
python scripts/run.py run files cleanup directory_path=data/input days=7

# watcher.py (Monitor directory changes in real-time)
python scripts/run.py run files watch directory_path=data/input
```

### 🔌 Team 2 — HTTP API Integration (`api`)
```bash
# health.py (Check status code and ping latency of a target web URL)
python scripts/run.py run api health url=https://api.github.com

# fetch.py (Query a GET REST endpoint and serialize the JSON payload locally)
python scripts/run.py run api fetch endpoint=users output_filename=users.json

# upload.py (POST local JSON file data to a remote server endpoint)
python scripts/run.py run api upload file_path=data/output/users.json endpoint=upload
```

### 📊 Team 3 — Excel Processing (`excel`)
```bash
# reader.py (Parse Excel cells and display them as Python dictionaries)
python scripts/run.py run excel read file_path=data/samples/sales.xlsx sheet_name=Sheet1

# writer.py (Write a structured collection of dict rows to an Excel sheet)
python scripts/run.py run excel write file_path=data/output/output.xlsx data="[{'id': 101, 'item': 'Sample'}]"

# reports.py (Compile raw transaction sheets and aggregate pivots using Pandas)
python scripts/run.py run excel reports source_file=data/samples/sales.xlsx dest_file=data/output/summary.xlsx
```

### ✉️ Team 4 — Email Operations (`email`)
```bash
# sender.py (Send emails via local SMTP credentials with optional attachment paths)
python scripts/run.py run email send to_email=recipient@example.com subject="Job Alert" body="Task completed"
```

### 🐳 Team 5 — Docker Services (`docker`)
```bash
# build.py (Build a local Docker image from a path containing a Dockerfile)
python scripts/run.py run docker build path=. tag=web-service:latest

# run.py (Launch a detached container with ports and environment variables)
python scripts/run.py run docker run image_tag=web-service:latest container_name=web-app

# cleanup.py (Prune stopped containers, dangling images, and unused volumes)
python scripts/run.py run docker cleanup
```

### 🐙 Team 6 — Git Workflows (`git`)
```bash
# status.py (Inspect staged, modified, and untracked repository states)
python scripts/run.py run git status repo_path=.

# commit.py (Stage changes and commit them with a message)
python scripts/run.py run git commit repo_path=. message="refactor: clean codebase"

# push.py (Push local commits to your remote upstream git branch)
python scripts/run.py run git push repo_path=. remote=origin branch=main
```

### ☸️ Team 7 — Kubernetes Clusters (`kubernetes`)
```bash
# deploy.py (Apply YAML deployment/service manifests to cluster)
python scripts/run.py run kubernetes deploy manifest_path=data/samples/pod.yaml namespace=default

# pods.py (List running namespace pods and IPs)
python scripts/run.py run kubernetes pods namespace=default

# logs.py (Query logs of a running pod and write them to a log file)
python scripts/run.py run kubernetes logs pod_name=my-pod namespace=default output_file=logs/pod.log
```

### ⏰ Team 8 — Persisted Scheduling (`scheduler`)
```bash
# jobs.py (Run schedule heartbeat loop checks)
python scripts/run.py run scheduler run_jobs interval_seconds=10

# schedule.py (Schedules a task to run daily/weekly)
python scripts/run.py run scheduler schedule task_name=api:health interval=daily time_of_day=10:00
```

### 📈 Team 9 — Report Serialization (`reports`)
```bash
# csv.py (Aggregate unstructured JSON records to clean CSV formats)
python scripts/run.py run reports csv input_file=data/output/users.json output_file=data/output/report.csv

# pdf.py (Compile styled PDF documents with tables using ReportLab)
python scripts/run.py run reports pdf title="Analytics Summary" content_lines="['Line A', 'Line B']" output_file=data/output/report.pdf

# excel.py (Export spreadsheet analytics incorporating custom charts)
python scripts/run.py run reports excel data_source=data/output/users.json output_file=data/output/analytics.xlsx
```

### 🔔 Team 10 — Channels Alerting (`notifications`)
```bash
# slack.py (Webhook post message alerts to Slack)
python scripts/run.py run notifications slack message="Server alert!"

# discord.py (Webhook warning embeds to Discord channels)
python scripts/run.py run notifications discord message="Backup failed!"

# email.py (Forward SMTP alert notifications to administrator)
python scripts/run.py run notifications email subject="Disk Status" message="90% full"
```

---

## 🧪 Testing Specific Categories (Pytest)
Execute unit tests for a specific package to check your implementations:
```bash
# Test File System modules
pytest tests/test_files.py

# Test HTTP API integrations
pytest tests/test_api.py

# Test Core framework loaders
pytest tests/test_engine.py
```
