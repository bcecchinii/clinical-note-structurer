from evaluate import normalize_data


def test_normalize_data():
    data = {
        "name": "  Anna Bianchi ",
        "age": 64,
        "symptoms": ["Headache"],
        "conditions": ["Hypertension", "TYPE 2 DIABETES"],
        "medications": ["Ramipril"]
    }

    normalized = normalize_data(data)

    assert normalized == {
        "name": "anna bianchi",
        "age": 64,
        "symptoms": ["headache"],
        "conditions": ["hypertension", "type 2 diabetes"],
        "medications": ["ramipril"]
    }



def test_normalize_data_with_missing_name():
    data = {
        "name": None,
        "age": None,
        "symptoms": [],
        "conditions": [],
        "medications": []
    }

    normalized = normalize_data(data)

    assert normalized["name"] is None
    assert normalized["age"] is None