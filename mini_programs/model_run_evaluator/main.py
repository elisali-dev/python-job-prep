from model_evaluator.validation import validate_model_run 
from model_evaluator.evaluation import (
    get_performance_level, 
    get_deployment_decision, 
)

def main():
    model_run = {
    "model_name": "image_classifier_v1",
    "accuracy": 0.87,
    "latency_ms": 75,
    "memory_mb": 1200,
}
    if validate_model_run(model_run):
        print(f"Model: {model_run["model_name"]}")
        print(f"Performance: {get_performance_level(model_run["accuracy"])}")
        print(f"Deployment Decision: {get_deployment_decision(model_run)}")
    # NOTE 补上 else, workflow 更完整
    else:
        print("Invalid model run data.")



if __name__ == "__main__":
    main()

    