from typing import Dict, Any, Optional
from typing_extensions import Annotated

from pydantic import BaseModel, validator,  BeforeValidator

OptionalBool = Annotated[
    Optional[bool],
    BeforeValidator(lambda v: None if v == "null" else v)
]


class Symptons(BaseModel):
    smoking: OptionalBool = None
    coughing: OptionalBool = None
    alcohol_use: OptionalBool = None
    swallowing_difficulty: OptionalBool = None
    snoring: OptionalBool = None
    anxiety: OptionalBool = None
    fatigue: OptionalBool = None
    wheezing: OptionalBool = None
    yellow_fingers: OptionalBool = None
    shortness_of_breath: OptionalBool = None
    allergy: OptionalBool = None
    chest_pain: OptionalBool = None
    chronic_lung_disease: OptionalBool = None
    coughing_of_blood: OptionalBool = None
    frequent_cold: OptionalBool = None
    genetic_risk: OptionalBool = None
    obesity: OptionalBool = None
    occupational_hazards: OptionalBool = None
    passive_smoker: OptionalBool = None
    peer_pressure: OptionalBool = None
    dust_allergy: OptionalBool = None
    dry_cough: OptionalBool = None


# FIXME(@lerax): seg 06 mai 2024 00:56:25
# inheritance here is just hacky and non-sense, fix this
class Patient(Symptons):
    patient_id: int
    name: str
    sex: str  # Male / Female
    age: int
    room: str
    hospitalized: bool = False
    has_lung_cancer: bool = False
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
            # Coercion: null -> false
            k: values.get(k)
            for k in Symptons.model_fields
        }
