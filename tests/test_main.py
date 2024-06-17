import pytest
from fastapi.testclient import TestClient

from cancer_estimator_application import main


@pytest.fixture
def client():
    return TestClient(main.app)


@pytest.fixture
def default_response():
    return {
        "age": 42,
        "room": "20-B",
        "name": "Lorena",
        "sex": "Female",
        "hospitalized": True,
        "allergy": False,
        "anxiety": False,
        "cancer_risk": False,
        "has_lung_cancer": False,
        "chest_pain": False,
        "coughing": False,
        "fatigue": False,
        "peer_pressure": False,
        "shortness_of_breath": False,
        "smoking": False,
        "alcohol_use": False,
        "cancer_risk_value": None,
        "chronic_lung_disease": False,
        "coughing_of_blood": False,
        "dry_cough": False,
        "dust_allergy": False,
        "frequent_cold": False,
        "genetic_risk": False,
        "obesity": False,
        "occupational_hazards": False,
        "passive_smoker": False,
        "snoring": False,
        "swallowing_difficulty": False,
        "wheezing": False,
        "yellow_fingers": False,
        "symptons": {
            "allergy": False,
            "anxiety": False,
            "chest_pain": False,
            "coughing": False,
            "fatigue": False,
            "peer_pressure": False,
            "shortness_of_breath": False,
            "smoking": False,
            "alcohol_use": False,
            "chronic_lung_disease": False,
            "coughing_of_blood": False,
            "dry_cough": False,
            "dust_allergy": False,
            "frequent_cold": False,
            "genetic_risk": False,
            "obesity": False,
            "occupational_hazards": False,
            "passive_smoker": False,
            "snoring": False,
            "swallowing_difficulty": False,
            "wheezing": False,
            "yellow_fingers": False,
        },
    }


def test_main_get_api_profile(client, default_response):
    response = client.get("/api/profile")
    assert response.status_code == 200
    assert response.json() == default_response


def test_main_post_api_profile(client, default_response):
    for sympton in default_response["symptons"]:
        default_response[sympton] = True
    del default_response["symptons"]
    response = client.post("/api/profile", json=default_response)
    assert response.status_code == 200
    assert response.json()["cancer_risk"] is True
