from unittest.mock import MagicMock, patch

from ai_service import structure_note


def test_structure_note_with_mocked_gemini():
    fake_json = """
    {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": [],
        "conditions": ["Hypertension"],
        "medications": ["Ramipril"]
    }
    """

    fake_interaction = MagicMock()
    fake_interaction.output_text = fake_json

    with patch("ai_service.genai.Client") as mock_client:
        mock_client.return_value.interactions.create.return_value = fake_interaction

        result = structure_note(
            "Anna Bianchi is a 64-year-old patient with hypertension."
        )

    assert result.name == "Anna Bianchi"
    assert result.age == 64
    assert result.symptoms == []
    assert result.conditions == ["Hypertension"]
    assert result.medications == ["Ramipril"]