from agents.reflector import reflect


def reflector_node(state):

    state.reflection = reflect(
        state.observations
    )

    print("\nREFLECTOR")
    print(state.retry_count)
    print(state.reflection)


    return state
