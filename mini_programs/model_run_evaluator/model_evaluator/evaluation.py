def get_performance_level(accuracy):
    if accuracy < 0.7:
        return "Poor"
    elif 0.7 <= accuracy < 0.85:
        return "Acceptable"
    return "Strong"

def get_deployment_decision(model_run):
    if model_run["accuracy"] >= 0.85 and model_run["latency_ms"] <= 100:
        return "Recommend"
    return "Do Not Recommend"

# Engineering best practice- no print statement in evaluation function. so they are easy to test 