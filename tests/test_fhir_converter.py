from fhir_converter import to_fhir_bundle


def test_fhir_bundle_with_complete_patient():
    data = {
        "name": "Anna Bianchi",
        "age": 64,
        "symptoms": [],
        "conditions": [
            "hypertension",
            "type 2 diabetes"
        ],
        "medications": [
            "Ramipril",
            "Metformin"
        ]
    }

    bundle = to_fhir_bundle(data)

    assert bundle["resourceType"] == "Bundle"
    assert bundle["type"] == "collection"

    resources = [
        entry["resource"]
        for entry in bundle["entry"]
    ]

    assert resources[0]["resourceType"] == "Patient"
    assert resources[0]["name"][0]["text"] == "Anna Bianchi"

    conditions = [
        resource
        for resource in resources
        if resource["resourceType"] == "Condition"
    ]

    assert len(conditions) == 2

    medications = [
        resource
        for resource in resources
        if resource["resourceType"] == "MedicationStatement"
    ]

    assert len(medications) == 2


def test_fhir_bundle_without_medications():
    data = {
        "name": "Paolo Conti",
        "age": 41,
        "symptoms": [
            "nausea",
            "fatigue"
        ],
        "conditions": [],
        "medications": None
    }

    bundle = to_fhir_bundle(data)

    resources = [
        entry["resource"]
        for entry in bundle["entry"]
    ]

    medications = [
        resource
        for resource in resources
        if resource["resourceType"] == "MedicationStatement"
    ]

    assert medications == []