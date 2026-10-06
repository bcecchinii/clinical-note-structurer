def to_fhir_bundle(data):
    entries = []

    patient_resource = {
        "resourceType": "Patient",
        "name": [
            {
                "text": data["name"]
            }
        ] if data["name"] else [],
    }

    if data["age"] is not None:
        patient_resource["extension"] = [
            {
                "url": "http://example.org/fhir/StructureDefinition/age",
                "valueInteger": data["age"]
            }
        ]

    entries.append({
        "resource": patient_resource
    })

    for condition in data["conditions"]:
        entries.append({
            "resource": {
                "resourceType": "Condition",
                "subject": {
                    "reference": "Patient/1"
                },
                "code": {
                    "text": condition
                }
            }
        })

    if data["medications"] is not None:
        for medication in data["medications"]:
            entries.append({
                "resource": {
                    "resourceType": "MedicationStatement",
                    "subject": {
                        "reference": "Patient/1"
                    },
                    "medicationCodeableConcept": {
                        "text": medication
                    }
                }
            })

    bundle = {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": entries
    }

    return bundle