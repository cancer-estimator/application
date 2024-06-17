from cancer_estimator_application import models


def get_patients():
    names = ["Lorena", "João", "Verri"]
    return [
        models.Patient(
            patient_id=idx,
            name=name,
            age=42,
            sex="Female" if name == "Lorena" else "Male",
            room="20-B",
            hospitalized=True
        )
        for (idx, name) in enumerate(names)
    ]
