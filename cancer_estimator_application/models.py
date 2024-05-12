from typing import Optional, Dict, Any
from pydantic import BaseModel, validator


class Symptons(BaseModel):
    allergy: bool = False
    fatigue: bool = False
    chronic_disease: bool = False
    coughing: bool = False
    alcohol_consuming: bool = False
    swallowing_difficulty: bool = False
    peer_pressure: bool = False
    anxiety: bool = False
    wheezing: bool = False
    yellow_fingers: bool = False
    smoking: bool = False
    shortness_of_breath: bool = False
    chest_pain: bool = False


# FIXME(@lerax): seg 06 mai 2024 00:56:25
# inheritance here is just hacky and non-sense, fix this
class Patient(Symptons):
    name: str
    sex: str
    age: int
    room: str
    hospitalized: bool
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
