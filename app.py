import streamlit as st

from ai_service import structure_note
from fhir_converter import to_fhir_bundle


st.set_page_config(
    page_title="Clinical Note Structurer",
    page_icon="🩺",
    layout="centered",
)

st.title("Clinical Note Structurer")

st.write(
    "Transform a synthetic clinical note into structured healthcare information."
)

note = st.text_area(
    "Clinical note",
    height=220,
    placeholder=(
        "Example: Anna Bianchi is a 64-year-old patient with hypertension "
        "and is currently taking Ramipril."
    ),
)

if st.button("Structure Note"):
    if not note.strip():
        st.warning("Please enter a clinical note.")
    else:
        try:
            with st.spinner("Structuring note..."):
                result = structure_note(note)

            data = result.model_dump()
            fhir_bundle = to_fhir_bundle(data)

            st.success("Clinical note structured successfully.")

            st.subheader("Structured Information")

            st.write(
                "**Name:**",
                data["name"] or "Not mentioned"
            )

            st.write(
                "**Age:**",
                data["age"] if data["age"] is not None else "Not mentioned"
            )

            st.write("**Symptoms:**")
            if data["symptoms"]:
                for symptom in data["symptoms"]:
                    st.write(f"- {symptom}")
            else:
                st.write("None")

            st.write("**Conditions:**")
            if data["conditions"]:
                for condition in data["conditions"]:
                    st.write(f"- {condition}")
            else:
                st.write("None")

            st.write("**Medications:**")
            if data["medications"] is None:
                st.write("Not mentioned")
            elif data["medications"]:
                for medication in data["medications"]:
                    st.write(f"- {medication}")
            else:
                st.write("None")

            with st.expander("View JSON"):
                st.json(data)

            with st.expander("View FHIR Bundle"):
                st.json(fhir_bundle)

        except Exception as error:
            st.error(f"Error: {error}")