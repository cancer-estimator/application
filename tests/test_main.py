import pytest
from fastapi.testclient import TestClient

from cancer_estimator_application import main


@pytest.fixture
def client():
    return TestClient(main.app)


def test_main_api_profile(client):
    response = client.get("/api/profile")
    assert response.status_code == 200
    assert response.json() == {
        "age": 42,
        "alcohol_consuming": False,
        "allergy": False,
        "anxiety": False,
        "cancer_risk": False,
        "chest_pain": False,
        "chronic_disease": False,
        "coughing": False,
        "fatigue": False,
        "hospitalized": True,
        "name": "Lorena",
        "peer_pressure": False,
        "room": "20-B",
        "sex": "Female",
        "shortness_of_breath": False,
        "smoking": False,
        "swallowing_difficulty": False,
        "symptons": {"alcohol_consuming": False,
                     "allergy": False,
                     "anxiety": False,
                     "chest_pain": False,
                     "chronic_disease": False,
                     "coughing": False,
                     "fatigue": False,
                     "peer_pressure": False,
                     "shortness_of_breath": False,
                     "smoking": False,
                     "swallowing_difficulty": False,
                     "wheezing": False,
                     "yellow_fingers": False},
        "wheezing": False,
        "yellow_fingers": False
    }
