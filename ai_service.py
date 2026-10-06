import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

from models import ClinicalNote


load_dotenv()


MODELS = [
    "gemini-3.8-flash",
    "gemini-3.7-flash",
]


def structure_note(note):
    api_key = os.getenv("GEMINI_API_KEY")

    if api_key is None:
        raise ValueError(
            "GEMINI_API_KEY not found in environment variables."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
Extract structured clinical information from the clinical note below.

Rules:
- Extract only information explicitly stated about the patient.
- Do not infer or guess missing information.
- Do not assign family history information to the patient.
- Distinguish symptoms from diagnosed medical conditions.
- Do not include negated symptoms.
- Include all explicitly stated patient conditions.
- Include all explicitly stated patient medications.
- If the patient's name is not stated, return null.
- If the patient's age is not stated, return null.
- If no symptoms are stated, return an empty list.
- If no conditions are stated, return an empty list.
- If the note explicitly states that the patient takes no medications,
  return an empty list for medications.
- If medication information is not mentioned, return null.

Clinical note:
{note}
"""

    last_error = None

    for model in MODELS:
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=ClinicalNote,
                    temperature=0,
                ),
            )

            return ClinicalNote.model_validate_json(
                response.text
            )

        except ServerError as error:
            last_error = error

            if error.code == 503:
                continue

            raise

    raise RuntimeError(
        "Gemini is temporarily unavailable on all configured models."
    ) from last_error