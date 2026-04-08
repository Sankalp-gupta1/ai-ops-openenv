from env.env import AIOpsEnv
import json

env = AIOpsEnv()
tasks = json.load(open("tasks/tasks.json"))

score = 0

def simple_agent(obs):
    # basic logic (no API)
    if obs.cpu > 80:
        return "scale"
    elif obs.memory > 80:
        return "restart"
    else:
        return "ignore"

for t in tasks:
    obs = env.reset(t["level"])

    action = simple_agent(obs)

    _, r, _, _ = env.step({"action": action})

    score += r

print("Final Score:", score/len(tasks))