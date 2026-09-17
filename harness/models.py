"""Data transfer objects and schemas for benchmark evaluation results."""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class TestCaseResult:
    node_id: str
    name: str
    outcome: str  # 'passed', 'failed', 'error', 'skipped'
    duration: float
    is_edge_case: bool
    error_message: Optional[str] = None

@dataclass
class ChallengeEvaluation:
    challenge_id: str
    title: str
    passed: bool
    total_tests: int
    passed_tests: int
    edge_cases_total: int
    edge_cases_passed: int
    execution_time: float
    tests: List[TestCaseResult] = field(default_factory=list)
    raw_output: str = ""
    error_summary: Optional[str] = None

    @property
    def pass_rate(self) -> float:
        return (self.passed_tests / self.total_tests * 100.0) if self.total_tests > 0 else 0.0

    @property
    def edge_case_pass_rate(self) -> float:
        return (self.edge_cases_passed / self.edge_cases_total * 100.0) if self.edge_cases_total > 0 else 0.0
