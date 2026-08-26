import pytest
from model_evaluator.evaluation import (
    get_deployment_decision,
    get_performance_level,
    get_capability_match,
)


REQUIRED_CAPABILITIES = {
    "python",
    "sql",
    "pytorch",
    "docker",
}

@pytest.mark.parametrize(
    # NOTE 将所有参数名写在一个双引号内，用逗号隔开。参数名与后面的中括号之间加上逗号。
    "accuracy, expected_result",
    [(0.6, "Poor"),
     (0.75, "Acceptable"),
     (0.9, "Strong"), 
     ]
)
def test_get_performance_level(accuracy, expected_result):
    assert get_performance_level(accuracy) == expected_result


def test_get_capability_match():
    model_capabilities = [
        " Python ",
        "SQL",
        "python",
        "PyTorch",
        "GPU",
    ]

    result = get_capability_match(
        model_capabilities,
        REQUIRED_CAPABILITIES,
    )

    assert result["matched"] == {
        "python",
        "sql",
        "pytorch",
    }

    assert result["missing"] == {
        "docker",
    }

    assert result["extra"] == {
        "gpu",
    }


ready_model = {
    "model_name": "ready_model",
    "accuracy": 0.90,
    "latency_ms": 80,
    "memory_mb": 1200,
    "capabilities": [
        "python",
        "sql",
        "pytorch",
        "docker",
    ],
}

slow_model = {
    "model_name": "slow_model",
    "accuracy": 0.90,
    "latency_ms": 150,
    "memory_mb": 1200,
    "capabilities": [
        "python",
        "sql",
        "pytorch",
        "docker",
    ],
}

missing_capability_model = {
    "model_name": "missing_capability_model",
    "accuracy": 0.95,
    "latency_ms": 50,
    "memory_mb": 1200,
    "capabilities": [
        "python",
        "sql",
        "pytorch",
    ],
}

boundary_model = {
    "model_name": "boundary_model",
    "accuracy": 0.85,
    "latency_ms": 100,
    "memory_mb": 1200,
    "capabilities": [
        "python",
        "sql",
        "pytorch",
        "docker",
    ],
}

@pytest.mark.parametrize(
    "model_sample, expected_result",
    [
        (ready_model, "Recommend"),
        (slow_model, "Do Not Recommend"),
        (missing_capability_model, "Do Not Recommend"),
        (boundary_model, "Recommend")
    ]
)
def test_get_deployment_decision(model_sample, expected_result):
    assert(
        get_deployment_decision(model_sample, REQUIRED_CAPABILITIES) 
        == expected_result)





# NOTE 
# 在 model_run_evaluator 目录下 terminal 运行 pytest -v 出现 ModuleNotFoundError: No module named 'model_evaluator' 
# 原因 - > 是因为直接运行 pytest 时，Python 的寻找路径（sys.path）中没有包含你当前的工程根目录。

# 用 python -m pytest -v 可以解决该问题, 它会强制 Python 将你当前所在的终端目录（即 model_run_evaluator）添加到模块搜索路径中，这样它就能顺利找到 model_evaluator 文件夹了。

# 或者 export PYTHONPATH=.  再运行 pytest -v