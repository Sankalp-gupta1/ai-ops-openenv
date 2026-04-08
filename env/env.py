from env.models import Observation
from env.memory import Memory
from env.anomaly import AnomalyDetector
from env.simulator import generate_log, generate_metrics

class AIOpsEnv:
    def __init__(self):
        self.memory = Memory()
        self.detector = AnomalyDetector()
        self.task = None
        self.step_count = 0

    def reset(self, level="easy"):
        cpu, memory, errors = generate_metrics(level)
        log = generate_log()
        anomaly = self.detector.detect(cpu, memory, errors)

        self.state_data = {
            "cpu": cpu,
            "memory": memory,
            "errors": errors,
            "logs": log,
            "anomaly": anomaly
        }

        self.task = level
        self.step_count = 0

        return Observation(**self.state_data)

    def step(self, action):
        act = action["action"]
        self.step_count += 1

        reward = 0.0
        done = False
        explanation = ""

        # 🎯 TASK LOGIC
        if self.task == "easy":
            if act == "scale":
                reward = 1.0
                explanation = "CPU spike handled by scaling"
            else:
                reward = -0.3
                explanation = "Wrong action for CPU spike"

        elif self.task == "medium":
            if act == "restart":
                reward = 1.0
                explanation = "Memory leak fixed by restart"
            else:
                reward = -0.3
                explanation = "Wrong action for memory issue"

        elif self.task == "hard":
            if act in ["scale", "restart"]:
                reward = 0.6
                explanation = "Partial fix for multi-issue system"
            else:
                reward = -0.5
                explanation = "Ignored critical failure"

        # ⏳ DELAYED REWARD (IMPORTANT)
        if act == "restart":
            reward += 0.4  # future stability bonus

        # ❌ LOOP PENALTY
        if self.step_count > 2:
            reward -= 0.2

        self.memory.add(self.state_data, act)

        done = True

        return Observation(**self.state_data), reward, done, {
            "explanation": explanation
        }

    def state(self):
        return self.state_data