from typing import Optional
from pydantic import BaseModel


class Symptons(BaseModel):
    allergy: Optional[bool] = False
    fatigue: Optional[bool] = False
    chronic_disease: Optional[bool] = False
    coughing: Optional[bool] = False
    alcohol_consuming: Optional[bool] = False
    swallowing_difficulty: Optional[bool] = False
    peer_pressure: Optional[bool] = False
    anxiety: Optional[bool] = False
    wheezing: Optional[bool] = False
    yellow_fingers: Optional[bool] = False
    smoking: Optional[bool] = False
    shortness_of_breath: Optional[bool] = False
    chest_pain: Optional[bool] = False


# FIXME(@lerax): seg 06 mai 2024 00:56:25
# inheritance here is just hacky and non-sense, fix this
class Patient(Symptons):
    name: str
    sex: str
    age: int
    room: str
    hospitalized: bool
