# Python Bug-Fix Benchmark & Automated Grading Harness

# [![Benchmark CI](https://github.com/your-username/python-bugfix-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/python-bugfix-benchmark)
[![Benchmark CI](https://github.com/your-username/python-bugfix-benchmark/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/python-bugfix-benchmark/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Docker Ready](https://img.shields.io/badge/docker-ready-2496ED.svg)](https://www.docker.com/)
[![Modeled on Datacurve Workflow](https://img.shields.io/badge/pipeline-Datacurve%2FShipd-orange.svg)](https://datacurve.ai)

An enterprise-grade Python coding challenge benchmark and sandboxed evaluation harness designed to assess hand-written and AI-generated code patches. Directly modeled after production code evaluation platforms featuring automated pytest grading, standard vs. edge-case breakdown, sandboxed isolation, and automated human reviewer sign-off reports.

---

## 🏛 Architecture & Evaluation Pipeline

```
      +-------------------------------------------------------------+
      |               AI Coding Agent / Candidate Patch             |
      +-------------------------------------------------------------+
                                     |
                                     v
      +-------------------------------------------------------------+
      |              Sandboxed Isolated Subprocess Runner           |
      |   - Dynamic Workspace Generation                            |
      |   - 10-Second Execution Timeout Guardian                    |
      +-------------------------------------------------------------+
                                     |
                                     v
      +-------------------------------------------------------------+
      |                       Pytest Harness                        |
      |   - Standard Regression Suites                              |
      |   - Edge-Case Invariant Validation (@pytest.mark.edge_case) |
      +-------------------------------------------------------------+
                                     |
                                     v
      +-------------------------------------------------------------+
      |                Grading & Reporting Engine                   |
      |   ├── Rich Terminal Summary Table                           |
      |   ├── JSON Machine-Readable Results (CI/CD Artifacts)       |
      |   └── Human Reviewer Sign-Off Audit Markdown Checklist      |
      +-------------------------------------------------------------+
```

---

## 📦 Challenge Taxonomy

| ID | Title | Category | Difficulty | Key Edge Cases Tested |
|---|---|---|---|---|
| `ch_01` | **LRU Cache** | Data Structures | Medium | Recency refresh on read, capacity overflow eviction |
| `ch_02` | **Sliding Window Limiter** | Systems & Concurrency | Medium | Sub-second timestamps, exact boundary eviction |
| `ch_03` | **JSON Path Extractor** | Parsing & Utilities | Easy | Falsy value preservation (`0`, `False`, `""`), missing nodes |
| `ch_04` | **Interval Merger** | Algorithms | Medium | Touching intervals `[1, 4]` & `[4, 5]`, unsorted ranges |
| `ch_05` | **Deep Dictionary Diff** | Data Processing | Hard | Type transitions (dict to string), added/removed keys |
| `ch_06` | **Topological Sort** | Algorithms & Graphs | Hard | Dependency cycles (`CycleDetectedError`), disjoint trees |
| `ch_07` | **Exponential Backoff** | Metaprogramming | Medium | Decorator metadata `@wraps`, unhandled exception pass-through |
| `ch_08` | **Decimal Financial Allocator** | FinTech | Easy | Banker's rounding, penny preservation invariant |
| `ch_09` | **Markdown Table Parser** | Compilers / Parsers | Medium | Escaped pipe `\|` symbols, mismatched cell counts |
| `ch_10` | **JWT Validator** | Security & Auth | Medium | Base64URL padding auto-recovery, exact second expiry |

---

## 🚀 Quick Start

For detailed setup, debugging, and GitHub deployment instructions, see [INSTRUCTIONS.md](INSTRUCTIONS.md).

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the automated benchmark harness (reference solutions: 100% pass)
python -m harness.runner --mode fixed

# 3. Test buggy candidate implementations (inspect failure traces)
python -m harness.runner --mode buggy
```
