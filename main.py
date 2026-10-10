

from agents.query_rewriter import rewrite_query
from agents.planner import create_plan
from agents.validator import validate_plan
from agents.executor import execute_plan
from agents.reflector import reflect
from agents.replanner import replan
from agents.answer_generator import generate_final_answer
from agents.router import route_question
from agents.direct_executor import execute_direct                           
from nodes.rewrite_node import rewrite_node
from nodes.router_node import router_node
from nodes.planner_node import planner_node
from nodes.executor_node import executor_node
from nodes.reflector_node import (
    reflector_node
)
from nodes.replanner_node import (
    replanner_node
)
from nodes.answer_node import (
    answer_node
)

MAX_RETRIES = 1
DEBUG = True


def main():

    while True:

        question = input("\nAsk: ").strip()

        if not question:
            continue

        if question.lower() == "exit":
            print("Goodbye.")
            break

        # state = create_state(question)

        # memory.add_user(question)

        state = rewrite_node(state)

        print("\n===== REWRITTEN QUESTION =====")
        print(state.rewritten_question)


        #Temporary state debug

        print("\n===== STATE =====")

        for key, value in state.model_dump().items():
            print(f"{key}: {value}")

        state = router_node(state)

        print("\n===== ROUTER =====")
        print(state.route)

        if state.route.type == "direct":

            print("\n===== DIRECT EXECUTION =====")


            state = executor_node(state)

            state.answer = generate_final_answer(
                state.question,
                state.observations
            )

            # memory.add_assistant(state.answer)

            print("\n===== FINAL ANSWER =====")
            print(state.answer)

            continue

        # ==========================
        # PLANNING
        # ==========================

        print("\n===== PLANNING =====")

        state = planner_node(state)

        print("\n===== PLAN =====")

        for step in state.plan:
            print(step)

        if not state.plan:    

            state = answer_node(state)

            print("\n===== FINAL ANSWER =====")
            print(state.answer)

            continue

        for step in state.plan:
            print(step)


        # ==========================
        # EXECUTION
        # ==========================

        print("\n===== EXECUTING =====")

        state = executor_node(state)

        # ==========================
        # REFLECTION + REPLAN
        # ==========================

        retries = 0

        while retries < MAX_RETRIES:

            state = reflector_node(state)

            print("\n===== REFLECTION =====")

            reflection = state.reflection

            if reflection.has_failures:

                for task in reflection.failed_tasks:
                    print(task)

            else:

                print("No failures detected.")
                break

            print("\n===== REPLANNING =====")

            state = replanner_node(state)

            if not state.new_plan:

                print("No replacement plan generated.")
                break

            print("\nNEW PLAN:")

            for step in state.new_plan:
                print(step)

            retries += 1

        # ==========================
        # OBSERVATIONS
        # ==========================

        print("\n===== OBSERVATIONS =====")

        for obs in state.observations:
            print(obs)

        # ==========================
        # FINAL ANSWER
        # ==========================

        state = answer_node(state)

        print("\n===== FINAL ANSWER =====")
        print(state.answer)

        # ==========================
        # DEBUG MEMORY
        # ==========================

        if DEBUG:

            print("\n===== MEMORY =====")

            for msg in state.history:
                print(
                    f"{msg['role']}: {msg['content']}"
                )


if __name__ == "__main__":
    main()
