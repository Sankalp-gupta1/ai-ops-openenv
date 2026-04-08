class CPUAgent:
    def act(self, obs):
        if obs.cpu > 80:
            return "scale"
        return None

class MemoryAgent:
    def act(self, obs):
        if obs.memory > 80:
            return "restart"
        return None

class MasterAgent:
    def __init__(self):
        self.cpu_agent = CPUAgent()
        self.mem_agent = MemoryAgent()

    def decide(self, obs):
        a1 = self.cpu_agent.act(obs)
        a2 = self.mem_agent.act(obs)

        return a1 or a2 or "ignore"