training_runs = [
    {
        "model": "resnet18",
        "config": {
            "epochs": 10,
            "device": "cpu",
        },
        "metrics": {
            "accuracy": 0.82,
            "loss": 0.41,
        },
    },
    {
        "model": "transformer",
        "config": {
            "epochs": 20,
            "device": "cuda",
        },
        "metrics": {
            "accuracy": 0.93,
            "loss": 0.18,
        },
    },
]

for run in training_runs:
        print(f"Model: {run["model"]}")
        print(f"Device: {run["config"]["device"]}")
        print(f"Accuracy: {run["metrics"]["accuracy"]}")
        if run["metrics"]["accuracy"] >= 0.90:
            print("High accuracy model")