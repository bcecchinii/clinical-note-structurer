from pydantic import BaseModel, Field


class ClinicalNote(BaseModel):
    name: str | None = Field(
        default=None,
        description="Patient name explicitly stated in the clinical note."
    )

    age: int | None = Field(
        default=None,
        description="Patient age explicitly stated in the clinical note."
    )

    symptoms: list[str] = Field(
        default_factory=list,
        description="Symptoms explicitly reported in the clinical note."
    )

    conditions: list[str] = Field(
        default_factory=list,
        description="Diagnosed medical conditions explicitly stated in the clinical note. Do not include symptoms."
    )

    medications: list[str] | None = Field(
        default=None,
        description=(
            "Medications explicitly stated in the clinical note. "
            "Return an empty list if the note explicitly states that the patient "
            "takes no medications. Return null if medication information is not mentioned."
        )
    )