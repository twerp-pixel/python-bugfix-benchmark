"""Sandboxed Pytest benchmark execution engine."""
import sys
import time
import argparse
import subprocess
import tempfile
from pathlib import Path
from typing import List

from harness.models import TestCaseResult, ChallengeEvaluation
from harness.reporter import BenchmarkReporter

CHALLENGE_REGISTRY = [
    ("ch_01_lru_cache", "LRU Cache Recency & Eviction Order"),
    ("ch_02_rate_limiter", "Sliding Window Rate Limiter"),
    ("ch_03_json_path_extractor", "Nested JSON Path Safe Extractor"),
    ("ch_04_merge_intervals", "Meeting & Range Interval Consolidation"),
    ("ch_05_deep_dict_diff", "Recursive Deep Dictionary Diff Engine"),
    ("ch_06_topological_sort", "Dependency Graph Topological Resolver"),
    ("ch_07_retry_decorator", "Exponential Backoff Retry Decorator"),
    ("ch_08_financial_allocator", "High-Precision Financial Portfolio Allocator"),
    ("ch_09_markdown_table_parser", "Markdown Table Robust Parser"),
    ("ch_10_jwt_validator", "Lightweight JWT Signature & Expiry Validator"),
]

def run_single_challenge(cid: str, title: str, code_path: Path, test_path: Path, timeout: int = 10) -> ChallengeEvaluation:
    with tempfile.TemporaryDirectory() as tmpdir:
        tmppath = Path(tmpdir)
        runner_test_file = tmppath / test_path.name
        
        # Copy test file
        test_content = test_path.read_text(encoding="utf-8")
        runner_test_file.write_text(test_content, encoding="utf-8")

        # Discover edge case test names
        edge_case_tests = set()
        for line in test_content.splitlines():
            if "def test_edge_" in line:
                name = line.split("def ")[1].split("(")[0].strip()
                edge_case_tests.add(name)

        cmd = [
            sys.executable,
            "-m",
            "pytest",
            str(runner_test_file),
            "-v",
            "--tb=short"
        ]

        env = {
            "PYTHONPATH": str(code_path.parent.resolve())
        }

        start_time = time.time()
        try:
            proc = subprocess.run(
                cmd,
                cwd=tmpdir,
                capture_output=True,
                text=True,
                env={**env, "PATH": subprocess.os.environ.get("PATH", "")},
                timeout=timeout
            )
            duration = time.time() - start_time
            raw_out = proc.stdout + "\n" + proc.stderr

            test_results = []
            total = 0
            passed = 0
            edge_total = 0
            edge_passed = 0

            for line in raw_out.splitlines():
                if "::test_" in line:
                    parts = line.split("::")
                    if len(parts) >= 2:
                        right = parts[1].split()
                        test_name = right[0]
                        status_part = right[1] if len(right) > 1 else ""
                        
                        is_edge = test_name in edge_case_tests or "edge" in test_name.lower()
                        total += 1
                        if is_edge:
                            edge_total += 1

                        if "PASSED" in status_part:
                            outcome = "passed"
                            passed += 1
                            if is_edge:
                                edge_passed += 1
                        elif "FAILED" in status_part:
                            outcome = "failed"
                        else:
                            outcome = "error"

                        test_results.append(TestCaseResult(
                            node_id=f"{test_path.name}::{test_name}",
                            name=test_name,
                            outcome=outcome,
                            duration=0.0,
                            is_edge_case=is_edge
                        ))

            all_passed = (total > 0) and (passed == total)
            return ChallengeEvaluation(
                challenge_id=cid,
                title=title,
                passed=all_passed,
                total_tests=total,
                passed_tests=passed,
                edge_cases_total=edge_total,
                edge_cases_passed=edge_passed,
                execution_time=duration,
                tests=test_results,
                raw_output=raw_out
            )

        except subprocess.TimeoutExpired:
            return ChallengeEvaluation(
                challenge_id=cid,
                title=title,
                passed=False,
                total_tests=0,
                passed_tests=0,
                edge_cases_total=0,
                edge_cases_passed=0,
                execution_time=float(timeout),
                raw_output="Timeout: Candidate code exceeded execution limit (> 10s)",
                error_summary="Execution Timeout"
            )


def main():
    parser = argparse.ArgumentParser(description="Python Benchmark & Grading Harness")
    parser.add_argument("--mode", choices=["fixed", "buggy"], default="fixed",
                        help="Run against 'fixed' reference solutions or 'buggy' candidate code")
    parser.add_argument("--json-out", default="benchmark_results.json", help="Path for JSON metrics output")
    parser.add_argument("--signoff-out", default="REVIEWER_SIGNOFF.md", help="Path for Reviewer Sign-Off sheet")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent
    code_dir = repo_root / ("solutions" if args.mode == "fixed" else "challenges")
    tests_dir = repo_root / "tests"

    print(f"\n[BENCHMARK HARNESS] Running in '{args.mode.upper()}' mode")
    print(f"\nAutomated Pytest Evaluation\n")

    results: List[ChallengeEvaluation] = []
    for cid, title in CHALLENGE_REGISTRY:
        code_file = code_dir / f"{cid}.py"
        test_file = tests_dir / f"test_{cid}.py"
        print(f"Evaluating {cid:<26} ... ", end="", flush=True)

        res = run_single_challenge(cid, title, code_file, test_file)
        results.append(res)

        status_badge = "✅ PASS" if res.passed else "❌ FAIL"
        print(f"{status_badge} ({res.passed_tests}/{res.total_tests} tests, {res.edge_cases_passed}/{res.edge_cases_total} edge-cases)")

    BenchmarkReporter.print_cli_summary(results)
    BenchmarkReporter.export_json(results, Path(args.json_out))
    BenchmarkReporter.export_reviewer_signoff(results, Path(args.signoff_out))

if __name__ == "__main__":
    main()
