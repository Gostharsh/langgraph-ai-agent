from pydantic import BaseModel
from llm.generate import generate


def structured_generate(
    prompt: str,
    schema: type[BaseModel]
):
    response = generate(prompt)

    return schema.model_validate_json(
        response
    )