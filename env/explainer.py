def explain(obs, action):
    if action == "scale":
        return "CPU high, scaling system"
    elif action == "restart":
        return "Memory high, restarting service"
    else:
        return "System normal, ignoring"