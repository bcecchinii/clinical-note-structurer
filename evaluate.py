import json
import sys

from ai_service import structure_note


def load_cases(filename):
    with open(filename, "r") as file:
        return json.load(file)


def normalize_text(value):
    return value.strip().lower()


def normalize_data(data):
    normalized = data.copy()

    if normalized["name"] is not None:
        normalized["name"] = normalize_text(normalized["name"])

    normalized["symptoms"] = [
        normalize_text(item) for item in normalized["symptoms"]
    ]

    normalized["conditions"] = [
        normalize_text(item) for item in normalized["conditions"]
    ]

    normalized["medications"] = [
        normalize_text(item) for item in normalized["medications"]
    ]

    return normalized

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

        normalized_actual = normalize_data(actual)
        normalized_expected = normalize_data(expected)

        if normalized_actual == normalized_expected:
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