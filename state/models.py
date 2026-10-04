
from pydantic import BaseModel, Field


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


from pydantic import BaseModel


class PlanStep(BaseModel):

    tool: str

    input: str = ""

