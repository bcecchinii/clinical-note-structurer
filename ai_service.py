import os

from dotenv import load_dotenv
from google import genai

from models import ClinicalNote


load_dotenv()


def structure_note(note):
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=f"""
        Extract structured clinical information from the clinical note below.

        Rules:
        - Extract only information explicitly stated about the patient.
        - Do not infer or guess missing information.
        - Do not assign family history information to the patient.
        - Distinguish symptoms from diagnosed medical conditions.
        - If the patient's name or age is not stated, return null.
        - If no symptoms, conditions, or medications are stated for the patient, return an empty list.

        Clinical note:
        {note}
        """,
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": ClinicalNote.model_json_schema()
        },
    )

    return ClinicalNote.model_validate_json(
        interaction.output_text
    )