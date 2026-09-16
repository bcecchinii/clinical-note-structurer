import json
with open("patient.json", "r") as file:
    patient = json.load(file)

'''
print(f"Patient Name: {patient['name']}")
print(f"Patient Age: {patient['age']}")

for condition in patient["conditions"]:
    print(f"Condition: {condition}")

for medication in patient["medications"]:
    print(f"Medication: {medication}")
'''

with open("clinical_note.txt", "r") as clinical:
    clinical_note = clinical.read()

print(f"Clinical Note: {clinical_note}")
