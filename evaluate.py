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

    normalized["symptoms"] = sorted(
        normalize_text(item) for item in normalized["symptoms"]
    )

    normalized["conditions"] = sorted(
        normalize_text(item) for item in normalized["conditions"]
    )

    if normalized["medications"] is not None:
        normalized["medications"] = sorted(
            normalize_text(item) for item in normalized["medications"]
        )

    return normalized


def compare_fields(actual, expected):
    fields = ["name", "age", "symptoms", "conditions", "medications"]

    normalized_actual = normalize_data(actual)
    normalized_expected = normalize_data(expected)

    results = {}

    for field in fields:
        results[field] = (
            normalized_actual[field] == normalized_expected[field]
        )

    return results




def main():
    cases = load_cases("evaluation/cases.json")

    if len(sys.argv) > 1:
        case_id = sys.argv[1]
        cases = [case for case in cases if case["id"] == case_id]

        if not cases:
            print(f"Case '{case_id}' not found.")
            return

    passed_cases = 0
    total_correct_fields = 0
    total_fields = 0

    for case in cases:
        print(f"\nEvaluating: {case['id']}")

        try:
            result = structure_note(case["note"])
        except Exception as error:
            print(f"ERROR: {error}")
            continue

        actual = result.model_dump()
        expected = case["expected"]

        comparison = compare_fields(actual, expected)

        correct_fields = 0

        for field, is_correct in comparison.items():
            total_fields += 1

            if is_correct:
                print(f"{field}: PASS")
                correct_fields += 1
                total_correct_fields += 1
            else:
                print(f"{field}: FAIL")
                print(f"  Expected: {expected[field]}")
                print(f"  Actual:   {actual[field]}")

        if correct_fields == len(comparison):
            print("Case result: PASS")
            passed_cases += 1
        else:
            print(
                f"Case result: "
                f"{correct_fields}/{len(comparison)} fields correct"
            )

    total_cases = len(cases)

    print(f"\nCases passed: {passed_cases}/{total_cases}")

    if total_fields > 0:
        accuracy = total_correct_fields / total_fields * 100

        print(
            f"Field accuracy: "
            f"{total_correct_fields}/{total_fields} "
            f"({accuracy:.1f}%)"
        )

    


if __name__ == "__main__":
    main()