def route_decision(state):

    if state.route.type == "direct":
        return "direct"

    return "planner"