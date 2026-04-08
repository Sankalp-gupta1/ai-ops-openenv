class Memory:
    def __init__(self):
        self.history = []

    def add(self, obs, action):
        self.history.append((obs, action))

    def last(self):
        return self.history[-1] if self.history else None