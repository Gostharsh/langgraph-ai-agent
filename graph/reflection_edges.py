MAX_RETRIES = 2

def reflection_decision(state):

    print("USING NEW REFLECTION_DECISION")

    print("\nREFLECTOR")
    print(state.retry_count)
    print(state.reflection)

    if (
        state.reflection.has_failures
        and state.retry_count < MAX_RETRIES
    ):
        return "replan"

    return "answer"