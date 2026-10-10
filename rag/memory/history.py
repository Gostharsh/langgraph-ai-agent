def build_history(graph, config):

    snapshot = graph.get_state(config)

    if not snapshot:
        return []

    values = snapshot.values

    return values.get("history", [])