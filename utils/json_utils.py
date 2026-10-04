import json
import re

def extract_json(text):

    match = re.search(
        r"\[\s*{.*}\s*\]",
        text,
        re.DOTALL
    )

    if not match:
        return []

    try:
        return json.loads(match.group())
    except Exception:
        return []