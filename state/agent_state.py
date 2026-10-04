
from pydantic import BaseModel, Field
from state.models import (
    Route,
    Observation,
    Reflection,
    PlanStep
)


class AgentState(BaseModel):

    retry_count: int = 0

    question: str

    rewritten_question: str = ""

    route: Route = Field(default_factory=Route)

    plan: list[PlanStep] = Field(default_factory=list)

    new_plan: list[PlanStep] = Field(default_factory=list)

    observations: list[Observation] = Field(default_factory=list)

    reflection: Reflection = Field(default_factory=Reflection)

    answer: str = ""

    history: list = Field(default_factory=list)