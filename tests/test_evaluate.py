from evaluate import compare_fields, normalize_data


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


def test_compare_fields_all_correct():
    actual = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": [],
        "conditions": ["Hypertension"],
        "medications": ["Ramipril"]
    }

    expected = {
        "name": "anna bianchi",
        "age": 64,
        "symptoms": [],
        "conditions": ["hypertension"],
        "medications": ["ramipril"]
    }

    result = compare_fields(actual, expected)

    assert result == {
        "name": True,
        "age": True,
        "symptoms": True,
        "conditions": True,
        "medications": True
    }


def test_compare_fields_with_error():
    actual = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": ["headache"],
        "conditions": ["Hypertension"],
        "medications": ["Ramipril"]
    }

    expected = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": [],
        "conditions": ["Hypertension"],
        "medications": ["Ramipril"]
    }

    result = compare_fields(actual, expected)

    assert result["name"] is True
    assert result["age"] is True
    assert result["symptoms"] is False
    assert result["conditions"] is True
    assert result["medications"] is True


def test_compare_fields_ignores_list_order():
    actual = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": ["fatigue", "headache"],
        "conditions": ["diabetes", "hypertension"],
        "medications": ["Metformin", "Ramipril"]
    }

    expected = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": ["headache", "fatigue"],
        "conditions": ["hypertension", "diabetes"],
        "medications": ["Ramipril", "Metformin"]
    }

    result = compare_fields(actual, expected)

    assert all(result.values())