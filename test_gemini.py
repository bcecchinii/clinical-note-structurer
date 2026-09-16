import os

from dotenv import load_dotenv
from google import genai

from models import ClinicalNote


load_dotenv()


def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    clinical_text = """
    Anna Bianchi is a 64-year-old patient with a history of hypertension
    and type 2 diabetes. She is currently taking Ramipril, Metformin and Aspirin.
    """

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=clinical_text,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ClinicalNote.model_json_schema()
        },
    )

    structured_note = ClinicalNote.model_validate_json(
        interaction.output_text
    )

    print(structured_note)


if __name__ == "__main__":
    main()