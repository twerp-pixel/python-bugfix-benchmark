# 📖 Operational Instructions & GitHub Deployment Guide

This guide walks you through setting up, testing, and deploying the **Python Bug-Fix Benchmark & Automated Grading Harness** to your GitHub account on EndeavourOS / Linux.

---

## 1. System Requirements & Setup on EndeavourOS

This project was built to run efficiently on an **Intel i3 with 8 GB RAM**:
- Minimal memory footprint (<150 MB RAM during evaluation)
- Subprocess timeouts prevent runaway processes or CPU lockups

### Install Dependencies:
```bash
# Ensure Python and git are installed
sudo pacman -S python git

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

---

## 2. Running the Harness

### A. Run Reference Solutions (100% Pass)
Runs the test suite against the reference implementations in `solutions/`:
```bash
python -m harness.runner --mode fixed
```
*Outputs:*
- Terminal summary table
- `benchmark_results.json` (Machine-readable test metrics)
- `REVIEWER_SIGNOFF.md` (Datacurve-style auditor sign-off)

### B. Run Buggy Candidates (Simulating AI / Candidate Failure Traces)
Runs the test suite against the raw buggy code in `challenges/`:
```bash
python -m harness.runner --mode buggy
```

### C. Direct Pytest Execution
You can also run pytest directly across all test suites:
```bash
pytest tests/ -v
```
To run only edge-case tests:
```bash
pytest tests/ -m edge_case -v
```

---

## 3. Running with Docker

```bash
# Build and run with Docker Compose
docker compose up --build
```

---

## 4. Pushing to GitHub (Step-by-Step)

Create a new repository on [GitHub](https://github.com/new) named `python-bugfix-benchmark`.

In your project directory on EndeavourOS, run:
```bash
# 1. Initialize git
git init

# 2. Stage all repository files
git add .

# 3. Create your initial commit
git commit -m "feat: complete python bug-fix benchmark & grading harness (Datacurve model)"

# 4. Set default branch to main
git branch -M main

# 5. Link to your GitHub remote (replace with your URL)
git remote add origin git@github.com:<YOUR-USERNAME>/python-bugfix-benchmark.git

# 6. Push to GitHub
git push -u origin main
```

Once pushed, check the **Actions** tab on GitHub. The CI workflow (`.github/workflows/ci.yml`) will run the test suites on Ubuntu CI and upload the evaluation artifacts automatically.

---

## 5. Resume & Interview Talking Points

When discussing this project with recruiters or in interviews:

- **What problem does this solve?**
  "Modern AI coding benchmarks require reproducible, automated verification beyond basic assertion checking. I built a harness modeled after Datacurve's evaluation pipeline that grades standard tests, isolates boundary invariants, and outputs automated sign-off checklists."
- **How is it tested?**
  "Each challenge has a dedicated pytest suite with standard assertions and marked `@pytest.mark.edge_case` decorators. The harness runs each challenge in isolated subshells with a 10-second timeout to prevent deadlocks or infinite loops."
- **Why is it Dockerized?**
  "To ensure full environment determinism and prevent host pollution when evaluating untrusted or AI-generated patches."
