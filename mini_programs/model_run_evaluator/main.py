from model_evaluator.validation import validate_model_run 
from model_evaluator.evaluation import (
    get_performance_level, 
    get_deployment_decision, 
    get_capability_match
)

def main():
    model_run = {
    "model_name": "image_classifier_v2",
    "accuracy": 0.89,
    "latency_ms": 80,
    "memory_mb": 1200,
    "capabilities": [
        " Python ",
        "SQL",
        "PyTorch",
        "GPU",
        "python",
    ],
}
    required_capabilities = {
    "python",
    "sql",
    "pytorch",
    "docker",
}


    
    if validate_model_run(model_run):
        print(f"Model: {model_run["model_name"]}")
        print(f"Performance: {get_performance_level(model_run["accuracy"])}")
        capability_result = get_capability_match(model_run["capabilities"], required_capabilities)
        print(f"Matched Capabilities: {capability_result["matched"]}")
        print(f"Missing Capabilities: {capability_result["missing"]}")
        print(f"Extra Capabilities: {capability_result["extra"]}")

        print(f"Deployment Decision: {get_deployment_decision(model_run, required_capabilities)}")
    else:
        print("Invalid model run data.")

    
if __name__ == "__main__":
    main()

    