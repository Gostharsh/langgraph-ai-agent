
from pydantic import BaseModel, Field
from pydantic import BaseModel
from typing import Literal

class Route(BaseModel):

    type: str = ""

    tool: str = ""

    input: str = ""


class Observation(BaseModel):

    tool: str

    input: str

    success: bool

    result: str

class Reflection(BaseModel):

    has_failures: bool = False

    failed_tasks: list = Field(default_factory=list)




class PlanStep(BaseModel):

    tool: Literal[
        "pdf_search",
        "calculator",
        "get_time"
    ]
    input: str = ""

class PlanOutput(BaseModel):
    steps: list[PlanStep]