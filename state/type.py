from typing import TypedDict


class Route(TypedDict):

    type: str

    tool: str

    input: str

class Reflection(TypedDict):

    has_failures: bool

    failed_tasks: list

class Observation(TypedDict):

    tool: str

    input: str

    success: bool

    result: str