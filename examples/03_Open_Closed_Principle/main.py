"""Run the same measurement with two alignment rules."""

from alignment_rules import CircularRule, PerAxisRule
from ocp_inspection_evaluator import InspectionEvaluator


def main() -> None:
    for rule in (CircularRule(), PerAxisRule()):
        result = InspectionEvaluator(rule).evaluate(
            reference_x=200.0,
            reference_y=220.0,
            measured_x=216.0,
            measured_y=236.0,
            tolerance=20.0,
        )
        print(
            f"{result.rule_name}: offsets=({result.offset_x:.0f}, "
            f"{result.offset_y:.0f}), distance={result.distance:.2f} px, "
            f"tolerance={result.tolerance:.0f} px, {result.status}"
        )


if __name__ == "__main__":
    main()
