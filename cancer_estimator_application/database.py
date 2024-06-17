from typing import List
import os
from contextlib import contextmanager

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float
from sqlalchemy.orm import DeclarativeBase  # type: ignore
from sqlalchemy.orm import sessionmaker

from cancer_estimator_application import models


# Database file path
db_path = os.path.join(os.getcwd(),  "patients.db")

# Create the database engine
engine = create_engine(f"sqlite:///{db_path}", echo=False)

# expire_on_commit prevent sqlalchemy error when returning the object on a
# function. Without that it's not possible to return a models.Job to the caller
# More info here: https://stackoverflow.com/a/3040164
SessionLocal = sessionmaker(bind=engine,
                            autoflush=False,
                            expire_on_commit=False)


class Base(DeclarativeBase):
    pass


# Define the Patient class
class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer, nullable=False)
    room = Column(String, nullable=False)
    name = Column(String, nullable=False)
    sex = Column(String, nullable=False)
    hospitalized = Column(Boolean, nullable=False, default=False)
    cancer_risk = Column(Boolean, nullable=False, default=False)
    has_lung_cancer = Column(Boolean, nullable=False, default=False)
    cancer_risk_value = Column(Float, nullable=True)

    # Symptons
    allergy = Column(Boolean, nullable=True)
    anxiety = Column(Boolean, nullable=True)
    chest_pain = Column(Boolean, nullable=True)
    coughing = Column(Boolean, nullable=True)
    fatigue = Column(Boolean, nullable=True)
    peer_pressure = Column(Boolean, nullable=True)
    shortness_of_breath = Column(Boolean, nullable=True)
    smoking = Column(Boolean, nullable=True)
    alcohol_use = Column(Boolean, nullable=True)
    chronic_lung_disease = Column(Boolean, nullable=True)
    coughing_of_blood = Column(Boolean, nullable=True)
    dry_cough = Column(Boolean, nullable=True)
    dust_allergy = Column(Boolean, nullable=True)
    frequent_cold = Column(Boolean, nullable=True)
    genetic_risk = Column(Boolean, nullable=True)
    obesity = Column(Boolean, nullable=True)
    occupational_hazards = Column(Boolean, nullable=True)
    passive_smoker = Column(Boolean, nullable=True)
    snoring = Column(Boolean, nullable=True)
    swallowing_difficulty = Column(Boolean, nullable=True)
    wheezing = Column(Boolean, nullable=True)
    yellow_fingers = Column(Boolean, nullable=True)


@contextmanager
def get_db():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()


def create_database_if_dont_exists(recreate=False):
    # Create the table if the database file does not exist

    # hack for testing, create a better approach
    if recreate is True and os.path.exists(db_path):
        os.remove(db_path)

    if not os.path.exists(db_path):
        Base.metadata.create_all(engine)

        with get_db() as db:
            # Add a sample record
            names = ["Lorena", "João", "Verri"]
            initial_patients = [
                Patient(
                    patient_id=idx + 1,
                    name=name,
                    age=42,
                    sex="Female" if name == "Lorena" else "Male",
                    room="20-B",
                    hospitalized=True
                )
                for (idx, name) in enumerate(names)
            ]

            for p in initial_patients:
                db.add(p)

            db.commit()

            # Query the database
            patients = db.query(Patient).all()
            for p in patients:
                print(f"[database] patient: patient_id={p.patient_id}, name={p.name}")
    else:
        print("Database exists. Skipping table creation and data insertion.")


def get_patients() -> List[models.Patient]:
    with get_db() as db:
        # Query the database
        patients = db.query(Patient).all()
        return [
            models.Patient.model_validate(p)
            for p in patients
        ]


def get_patient(patient_id: int) -> models.Patient:
    with get_db() as db:
        patient = db.query(Patient).filter(Patient.patient_id == patient_id).first()
        if not patient:
            raise ValueError("not found")
        return models.Patient.model_validate(patient)


def update_patient(patient: models.Patient) -> models.Patient:
    """
    Using a new update method seen in FastAPI https://github.com/tiangolo/fastapi/pull/2665
    Simple, does not need each attribute to be updated individually
    Uses python in built functionality... preferred to the pydintic related method
    """
    with get_db() as db:
        # get the existing data
        db_patient = db.query(Patient).filter(Patient.patient_id == patient.patient_id).one_or_none()
        if db_patient is None:
            raise ValueError("not found")

        for key, value in patient.dict().items():
            if key == "symptons":
                continue
            setattr(db_patient, key, value)

        db.commit()
        db.refresh(db_patient)
        return models.Patient.model_validate(db_patient)
