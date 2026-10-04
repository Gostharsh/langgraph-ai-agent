# memory/memory.py

class ConversationMemory:

    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        self.messages.append({
            "role": role,
            "content": content
        })

    def add_user(self, content):
        self.add_message(
            "user",
            content
        )

    def add_assistant(self, content):
        self.add_message(
            "assistant",
            content
        )

    def get_history(self):
        return self.messages

    def last_user_message(self):

        users = [
            m
            for m in self.messages
            if m["role"] == "user"
        ]

        if len(users) < 2:
            return ""

        return users[-2]["content"]


# Global memory instance
memory = ConversationMemory()


# Helper functions
def add_message(role, content):
    memory.add_message(role, content)


def get_history():
    return memory.get_history()


def last_user_message():
    return memory.last_user_message()