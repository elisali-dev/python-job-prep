
def validate_model_run(model_run):
    if (model_run["model_name"].strip() 
        and 0 <= model_run["accuracy"] <= 1 
        and model_run["latency_ms"] > 0 
        and model_run["memory_mb"] > 0 
        ):
            return True 
    return False
    
