import json
import sys

from ai_service import structure_note


def load_cases(filename):
    with open(filename, "r") as file:
        return json.load(file)


def main():
    cases = load_cases("evaluation/cases.json")

    if len(sys.argv) > 1:
        case_id = sys.argv[1]
        cases = [case for case in cases if case["id"] == case_id]

        if not cases:
            print(f"Case '{case_id}' not found.")
            return

    passed = 0

    for case in cases:
        print(f"\nEvaluating: {case['id']}")

        try:
            result = structure_note(case["note"])
        except Exception as error:
            print(f"ERROR: {error}")
            continue

        actual = result.model_dump()
        expected = case["expected"]

        if actual == expected:
            print("PASS")
            passed += 1
        else:
            print("FAIL")
            print(f"Expected: {expected}")
            print(f"Actual:   {actual}")

    total = len(cases)

    print(f"\nResults: {passed}/{total} cases passed")


if __name__ == "__main__":
    main()