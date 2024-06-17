import pytest
from fastapi.testclient import TestClient

from cancer_estimator_application import main


@pytest.fixture
def client():
    return TestClient(main.app)


@pytest.fixture
def default_response():
    return {
        "patient_id": 0,
        "age": 42,
        "room": "20-B",
        "name": "Lorena",
        "sex": "Female",
        "hospitalized": True,
        "allergy": None,
        "anxiety": None,
        "cancer_risk": False,
        "cancer_risk_value": None,
        "has_lung_cancer": False,
        "chest_pain": None,
        "coughing": None,
        "fatigue": None,
        "peer_pressure": None,
        "shortness_of_breath": None,
        "smoking": None,
        "alcohol_use": None,
        "chronic_lung_disease": None,
        "coughing_of_blood": None,
        "dry_cough": None,
        "dust_allergy": None,
        "frequent_cold": None,
        "genetic_risk": None,
        "obesity": None,
        "occupational_hazards": None,
        "passive_smoker": None,
        "snoring": None,
        "swallowing_difficulty": None,
        "wheezing": None,
        "yellow_fingers": None,
        "symptons": {
            "allergy": None,
            "anxiety": None,
            "chest_pain": None,
            "coughing": None,
            "fatigue": None,
            "peer_pressure": None,
            "shortness_of_breath": None,
            "smoking": None,
            "alcohol_use": None,
            "chronic_lung_disease": None,
            "coughing_of_blood": None,
            "dry_cough": None,
            "dust_allergy": None,
            "frequent_cold": None,
            "genetic_risk": None,
            "obesity": None,
            "occupational_hazards": None,
            "passive_smoker": None,
            "snoring": None,
            "swallowing_difficulty": None,
            "wheezing": None,
            "yellow_fingers": None,
        },
    }


def test_main_get_api_profile(client, default_response):
    response = client.get("/api/profile/0")
    assert response.status_code == 200
    assert response.json() == default_response


def test_main_post_api_profile(client, default_response):
    for sympton in default_response["symptons"]:
        default_response[sympton] = True
    del default_response["symptons"]
    response = client.put("/api/profile/0", json=default_response)
    assert response.status_code == 200
    assert response.json()["cancer_risk"] is True
