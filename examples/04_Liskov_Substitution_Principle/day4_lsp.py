"""
File Name: day4_lsp.py
Created Date: 2026-09-28
Author: Alex
Description:
    Demonstrates the Liskov Substitution Principle by replacing
    evaluation policies and checking whether each policy follows
    the expected PASS or FAIL result contract.
"""

from abc import ABC, abstractmethod


class EvaluationPolicy(ABC):
    """Returns PASS or FAIL for a score from 0 to 100."""

    @abstractmethod
    def evaluate(self, score: int) -> str:
        pass


class BasicPolicy(EvaluationPolicy):
    def evaluate(self, score: int) -> str:
        return "PASS" if score >= 60 else "FAIL"


class StrictPolicy(EvaluationPolicy):
    def evaluate(self, score: int) -> str:
        return "PASS" if score >= 80 else "FAIL"

'''
class SpecialPolicy(EvaluationPolicy):
    def evaluate(self, score: int) -> str:
        return "EXCELLENT" if score >= 95 else "NORMAL"
'''

class SpecialPolicy(EvaluationPolicy):
    def evaluate(self, score: int) -> str:
        return "PASS" if score >= 95 else "FAIL"

def print_result(policy: EvaluationPolicy, score: int) -> None:
    result = policy.evaluate(score)

    if result == "PASS":
        print(f"{score} points: Pass")
    elif result == "FAIL":
        print(f"{score} points: Fail")
    else:
        print(f"{score} points: Unexpected result → {result}")

'''
for policy in (BasicPolicy(), StrictPolicy(), SpecialPolicy()):
    print(type(policy).__name__)
    print_result(policy, 95)
'''

'''
for policy in (BasicPolicy(), StrictPolicy(), SpecialPolicy()):
    print(type(policy).__name__)

    for score in (94, 95):
        print_result(policy, score)
'''

policies = (
    BasicPolicy(),
    StrictPolicy(),
    SpecialPolicy(),
)

for policy in policies:
    for score in (0, 59, 60, 79, 80, 94, 95, 100):
        result = policy.evaluate(score)

        assert result in ("PASS", "FAIL"), (
            f"{type(policy).__name__}: Unexpected result {result!r} for a score of {score}"
        )

    print(f"{type(policy).__name__}: Return value contract verified")

assert SpecialPolicy().evaluate(94) == "FAIL"
assert SpecialPolicy().evaluate(95) == "PASS"

print("All checks passed")
