from typing import Tuple

from functools import lru_cache

from cancer_estimator_model import models, io
from cancer_estimator_application.models import Patient


@lru_cache
def get_model():
    return models.load()


def _proper_type_coercion(feature, value):
    if feature.upper() in models.cat_features + models.artificial_variables:
        return int(value)
    return float(value)


def _generate_features(patient: Patient) -> dict:
    features: dict[str, str | float] = {
        k: _proper_type_coercion(k, v)
        for k, v in patient.symptons.items()
    }
    features["age"] = patient.age
    features["gender"] = patient.sex
    return features


def estimate_cancer(patient: Patient) -> Tuple[float, bool]:
    features = _generate_features(patient)
    model = get_model()
    df = io.dict_to_pandas(features)
    X = models.generate_artificial_variables(df)[models.feature_selection]
    # FIXES:
    X["COLD_SYMPTOMNS"] = X["COLD_SYMPTOMNS"].astype(int)
    X["RESPIRATORY_SYMPTOMNS"] = X["COLD_SYMPTOMNS"].astype(int)
    #
    risk_of_cancer, risk_flag = models.predict_with_threshold(model, X)
    return risk_of_cancer[0], risk_flag[0]
