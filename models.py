from pydantic import BaseModel, Field


class ClinicalNote(BaseModel):
    name: str | None = Field(
        default=None,
        description=(
            "Full name of the patient, only if explicitly stated in the note. "
            "Do not infer a name. Do not use names of relatives or other people. "
            "Return null if the patient's name is not stated."
        )
    )

    age: int | None = Field(
        default=None,
        description=(
            "Age of the patient in years, only if explicitly stated in the note. "
            "For example, '64-year-old patient' means age 64. "
            "Return null if the patient's age is not stated."
        )
    )

    symptoms: list[str] = Field(
        default_factory=list,
        description=(
            "Symptoms currently reported or experienced by the patient, such as "
            "'headache', 'fatigue', 'shortness of breath', or 'nausea'. "
            "Do NOT include diagnosed diseases or chronic medical conditions such as "
            "'hypertension', 'diabetes', or 'asthma'. "
            "Do NOT include negated symptoms. "
            "Return an empty list if no patient symptoms are stated."
        )
    )

    conditions: list[str] = Field(
        default_factory=list,
        description=(
            "Diagnosed diseases or medical conditions explicitly stated as belonging "
            "to the patient, such as 'hypertension', 'type 2 diabetes', or 'asthma'. "
            "Include conditions introduced with phrases such as 'has', "
            "'with', or 'history of'. "
            "Do NOT include symptoms. "
            "Do NOT include conditions that belong only to family members. "
            "Return an empty list if no patient conditions are stated."
        )
    )

    medications: list[str] | None = Field(
        default=None,
        description=(
            "Medications that the patient is explicitly stated to be taking or using, "
            "such as 'Ramipril', 'Metformin', or 'Salbutamol'. "
            "Include all explicitly stated patient medications. "
            "Do NOT include medications belonging to another person. "
            "Return an empty list if the note explicitly states that the patient "
            "takes no medications. "
            "Return null if medication information is not mentioned at all."
        )
    )


    