import json
import os

from dotenv import load_dotenv
from google import genai

from models import ClinicalNote


load_dotenv()


def read_note(filename):
    with open(filename, "r") as file:
        return file.read()


def structure_note(note):
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=note,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ClinicalNote.model_json_schema()
        },
    )

    structured_note = ClinicalNote.model_validate_json(
        interaction.output_text
    )

    return structured_note


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