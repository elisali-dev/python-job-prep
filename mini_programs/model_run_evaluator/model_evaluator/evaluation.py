def get_performance_level(accuracy):
    if accuracy < 0.7:
        return "Poor"
    elif 0.7 <= accuracy < 0.85:
        return "Acceptable"
    return "Strong"

def get_deployment_decision(model_run, required_capabilities):
    if (model_run["accuracy"] >= 0.85 
        and model_run["latency_ms"] <= 100
        #Iteration 2
        and not get_capability_match(model_run["capabilities"],required_capabilities)["missing"]
        ):
            return "Recommend"
    return "Do Not Recommend"

# Engineering best practice- no print statement in evaluation function. so they are easy to test 



### Normalize Model capabilities ###
def get_capability_match(
    model_capabilities,
    required_capabilities,
):
    # # LEARNING NOTE: Normalize each string before converting to a set.
    model_capabilities_dedup = {capability.strip().lower() for capability in model_capabilities}
   

    matched_capabilities = model_capabilities_dedup & required_capabilities
    missing_capabilities = required_capabilities - model_capabilities_dedup
    extra_capabilities = model_capabilities_dedup - required_capabilities

    return {
        "matched": matched_capabilities,
        "missing": missing_capabilities,
        "extra": extra_capabilities,
    }
    


 # NOTE 其他生成 set 的写法
        #直接用花括号 {} 就能生成去重后的集合
            # model_capabilities_dedup = {capability.strip().lower() for capability in model_capabilities}
        # 使用 set.update()（如果你必须先声明空集合）
            # model_capabilities_dedup = set()
            # model_capabilities_dedup.update(capability.strip().lower() for capability in model_capabilities)
        # NOTE set.add(element)：只能添加一个元素。set.update(iterable)：可以添加多个元素（把一个可迭代对象里的东西拆开加进去）。
