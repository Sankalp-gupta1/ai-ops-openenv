from pydantic import BaseModel

class Observation(BaseModel):
    cpu: float
    memory: float
    errors: int
    anomaly: int
    logs: str

class Action(BaseModel):
    action: str  # scale / restart / ignore

class Reward(BaseModel):
    score: float