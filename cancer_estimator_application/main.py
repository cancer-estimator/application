from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fasthx import Jinja

from cancer_estimator_application import models
from cancer_estimator_application import debug
from cancer_estimator_application import predict
from cancer_estimator_application import database

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create a FastAPI Jinja2Templates instance and use it to create a
# FastHX Jinja instance that will serve as your decorator.
jinja = Jinja(Jinja2Templates("templates"))
debug.register_exception(app)


@app.get("/")
@jinja.page("search.html")
def index() -> None:
    ...


@app.get("/profile/{patient_id}")
@jinja.page("patient-profile.html")
def patient_profile_page(patient_id: int):
    return {
        "patient_id": 1
    }


@app.get("/api/search")
@jinja.hx("search-data.html")
def filter_search(search: str = "") -> List[models.Patient]:
    query = search.lower()
    matches = [
        patient
        for patient in database.get_patients()
        if query in patient.name.lower()
    ]
    return matches


@app.get("/api/profile/{patient_id}")
@jinja.hx("patient-profile-data.html")
def patient_profile_data(patient_id: int) -> models.Patient:
    return database.get_patients()[patient_id]


@app.put("/api/profile/{patient_id}")
@jinja.hx("patient-profile-data.html")
def update_profile(patient: models.Patient, patient_id: int) -> models.Patient:
    print(patient)
    cancer_risk, cancer_flag = predict.estimate_cancer(patient)
    if cancer_flag:
        patient.cancer_risk = True
        patient.cancer_risk_value = cancer_risk
    return patient
