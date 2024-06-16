from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fasthx import Jinja

from cancer_estimator_application import models
from cancer_estimator_application import debug
from cancer_estimator_application import predict

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Create a FastAPI Jinja2Templates instance and use it to create a
# FastHX Jinja instance that will serve as your decorator.
jinja = Jinja(Jinja2Templates("templates"))
debug.register_exception(app)


@app.get("/")
@jinja.page("patient-profile.html")
def index() -> None:
    ...


@app.get("/api/profile")
@jinja.hx("patient-profile-data.html")
def patient_profile() -> models.Patient:
    m = models.Patient(
        name="Lorena",
        age=42,
        sex="Female",
        room="20-B",
        hospitalized=True
    )
    # print(m.dict())
    return m


@app.post("/api/profile")
@jinja.hx("patient-profile-data.html")
def update_profile(patient: models.Patient):
    print(patient)
    cancer_risk, cancer_flag = predict.estimate_cancer(patient)
    if cancer_flag:
        patient.cancer_risk = True
        patient.cancer_risk_value = round(cancer_risk, ndigits=4)
    return patient
