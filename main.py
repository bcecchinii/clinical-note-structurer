import json

def read_note(filename):
    with open(filename, "r") as file:
        return file.read()


def structure_note(note):
    structured_data = {
        "name": "Anna Bianchi",
        "age": 64,
        "conditions": ["Hypertension", "Type 2 Diabetes"],
        "medications": ["Ramipril", "Metformin", "Aspirin"]
    }
    return structured_data


def save_json(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    clinical_note = read_note("clinical_note.txt")
    result = structure_note(clinical_note)
    save_json(result, "structured_data.json")
    print(f"clinical note: {clinical_note}")


if __name__ == "__main__":
    main()
