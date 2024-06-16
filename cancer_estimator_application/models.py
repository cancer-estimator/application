from typing import Dict, Any, Optional
from pydantic import BaseModel, validator


class Symptons(BaseModel):
    smoking: bool = False
    coughing: bool = False
    alcohol_use: bool = False
    swallowing_difficulty: bool = False
    snoring: bool = False
    anxiety: bool = False
    fatigue: bool = False
    wheezing: bool = False
    yellow_fingers: bool = False
    shortness_of_breath: bool = False
    allergy: bool = False
    chest_pain: bool = False
    chronic_lung_disease: bool = False
    coughing_of_blood: bool = False
    frequent_cold: bool = False
    genetic_risk: bool = False
    obesity: bool = False
    occupational_hazards: bool = False
    passive_smoker: bool = False
    peer_pressure: bool = False
    dust_allergy: bool = False
    dry_cough: bool = False


# FIXME(@lerax): seg 06 mai 2024 00:56:25
# inheritance here is just hacky and non-sense, fix this
class Patient(Symptons):
    name: str
    sex: str  # Male / Female
    age: int
    room: str
    hospitalized: bool
    cancer_risk: bool = False
    cancer_risk_value: Optional[float] = None
    # read only
    symptons: Dict[str, bool] = dict()

    @validator("symptons", always=True)
    def fill_symptons(
        cls,
        symptons: Dict[str, bool],
        values: Dict[str, Any]
    ) -> Dict[str, Any]:
        """This should fill the symptons dictionary
        """
        return {
            k: values.get(k)
            for k in Symptons.model_fields
        }
