from agents.answer_generator import generate_final_answer


def answer_node(state):

    state.answer = generate_final_answer(
        state.question,
        state.observations
    )

    return state