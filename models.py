from pydantic import BaseModel


class ClinicalNote(BaseModel):
    name: str
    age: int
    conditions: list[str]
    medications: list[str]