class ConversationMemory:

    def __init__(self, max_messages=6):
        self.max_messages = max_messages
        self.history = []

    def add_user(self, message):
        self.history.append(("User", message))
        self.trim()

    def add_bot(self, message):
        self.history.append(("AgriBot", message))
        self.trim()

    def trim(self):
        if len(self.history) > self.max_messages:
            self.history = self.history[-self.max_messages:]

    def get_history(self):
        return "\n".join(
            f"{role}: {msg}" for role, msg in self.history
        )


memory = ConversationMemory()