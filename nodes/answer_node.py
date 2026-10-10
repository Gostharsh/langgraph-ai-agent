# from agents.answer_generator import generate_final_answer


# def answer_node(state):

#     state.answer = generate_final_answer(
#         state.question,
#         state.observations
#     )

#     state.history.append(
#         {
#             "user": state.question,
#             "assistant": state.answer
#         }
#     )

#     return state



# from memory.memory import memory

# def answer_node(state):

#     state.answer = generate_final_answer(
#         state.question,
#         state.observations
#     )

#     memory.add_user(state.question)

#     memory.add_assistant(state.answer)

#     return state

from agents.answer_generator import generate_final_answer

def answer_node(state):

    state.answer = generate_final_answer(
        state.question,
        state.observations
    )

    state.history.append(
        {
            "role": "user",
            "content": state.question
        }
    )

    state.history.append(
        {
            "role": "assistant",
            "content": state.answer
        }
    )

    return state