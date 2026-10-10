class ConversationMemory:

    def __init__(self):
        self.last_question = ""

    def get_last_question(self):
        return self.last_question

    def save_question(self, question):
        self.last_question = question