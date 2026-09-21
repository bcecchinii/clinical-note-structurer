import json

from ai_service import structure_note


def read_note(filename):
    with open(filename, "r") as file:
        return file.read()


def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data.model_dump(), file, indent=4)


def main():
    clinical_note = read_note("clinical_note.txt")
    result = structure_note(clinical_note)
    save_json(result, "structured_data.json")

    print(result)


if __name__ == "__main__":
    main()