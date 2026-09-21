import pytest

from pydantic import ValidationError

from models import ClinicalNote


def test_clinical_note_with_complete_data():
    note = ClinicalNote(
        name="Anna Bianchi",
        age=64,
        symptoms=["headache"],
        conditions=["Hypertension"],
        medications=["Ramipril"]
    )

    assert note.name == "Anna Bianchi"
    assert note.age == 64
    assert note.symptoms == ["headache"]
    assert note.conditions == ["Hypertension"]
    assert note.medications == ["Ramipril"]


def test_clinical_note_with_missing_data():
    note = ClinicalNote()

    assert note.name is None
    assert note.age is None
    assert note.symptoms == []
    assert note.conditions == []
    assert note.medications == []


def test_invalid_age():
    with pytest.raises(ValidationError):
        ClinicalNote(
            name="Anna Bianchi",
            age="sessantaquattro"
        )