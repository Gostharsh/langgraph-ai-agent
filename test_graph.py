from graph.build_graph import graph


config = {
    "configurable": {
        "thread_id": "user_1"
    }
}


# =========================
# FIRST QUESTION
# =========================

result = graph.invoke(
    {
        "question": "What is investing?"
    },
    config=config
)

print("\nFIRST RUN")
print(result["answer"])


snapshot = graph.get_state(config)
history = snapshot.values.get("history", [])

print("\nHISTORY AFTER FIRST RUN")
print(snapshot.values["history"])


# =========================
# SECOND QUESTION
# =========================

result = graph.invoke(
    {
        "question": "Explain it simply"
    },
    config=config
)

print("\nSECOND RUN")
print(result["answer"])


snapshot = graph.get_state(config)
history = snapshot.values.get("history", [])

print("\nHISTORY AFTER SECOND RUN")
print(snapshot.values["history"])