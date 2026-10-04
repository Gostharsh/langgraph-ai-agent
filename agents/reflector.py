from state.models import Reflection

def reflect(observations):

    failed_tasks = []

    FAIL_PATTERNS = [
        "couldn't find",
        "could not find",
        "not found",
        "no information",
        "no relevant information",
        "unknown",
        "error",
        "unfortunately",
        "isn't a direct answer",
        "not enough information",
        "cannot answer",
    ]

    for obs in observations:

        if not obs.success:

            failed_tasks.append({
                "tool": obs.tool,
                "input": obs.input,
                "reason": "execution_failed"
            })

            continue

        result = str(obs.result).lower()

        if any(
            pattern in result
            for pattern in FAIL_PATTERNS
        ):

            failed_tasks.append({
                "tool": obs.tool,
                "input": obs.input,
                "reason": "bad_answer"
            })

    return Reflection(
        has_failures=len(failed_tasks) > 0,
        failed_tasks=failed_tasks
    )