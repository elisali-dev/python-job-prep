# NOTE 用 python -m pytest -v command 去测试

# NOTE - 关于 from... import 
# 在 Python 工程开发中，from 语句从哪个层级开始写，取决于你的项目根目录（Project Root）被设置为了哪里，以及你如何运行这个测试脚本。
# 在 VS Code 或 PyCharm 等编辑器中，最标准、最不容易出错的方法是将最外层的项目根目录作为起点。
# 在写测试（Test Cases）时，为了不被 ModuleNotFoundError 折磨，工程上通常推荐以下两步：
    # 1. 配合 pytest 工具运行（最省心）在实际工程中，大家不会直接去运行测试脚本本身，而是使用 pytest。
            # NOTE 打开终端，切换到 model_run_evaluator 目录下，直接运行
            # pytest 会自动把当前运行的目录（model_run_evaluator）加入到 Python 的搜索路径（sys.path）中。此时，你在测试文件里写 from model_evaluator.validation import ... 就能百分之百完美识别。
    # 2. 检查 IDE 的项目根目录 (NOTE 这不是你terminal 里的当前所在文件夹目录)
            # 1. 窗口根目录（Project Root / Workspace）
                # 这是指你在 VS Code 或 PyCharm 中，通过 File -> Open Folder 最初打开的那个最顶层的文件夹。它的视觉特征：在你的编辑器左侧侧边栏（Explorer）中，排在最上面、最左边、无法再往上折叠的那个文件夹。它的工程作用：它决定了你的开发工具（IDE）如何去理解你的项目。你的代码自动补全、跳转（Go to Definition）、以及静态语法检查，都是以这个窗口根目录为基准线来寻找文件的。
            # 2. Terminal（终端）里的当前路径（Current Working Directory / CWD）这是指你当前在命令行终端里肉眼看到的那个路径（即闪烁的光标前面的那一串路径）。
                # 它的工程作用：它决定了当你输入指令（如 python main.py 或 pytest）并按下回车时，操作系统会在哪个文件夹里去执行这个命令。你可以随时通过 cd 命令去自由切换它。


import pytest 

from model_evaluator.validation import validate_model_run

model_run_1 = {
    "model_name": "image_classifier_v1",
    "accuracy": 0.87,
    "latency_ms": 75,
    "memory_mb": 1200,
}

model_run_2 = {
    "model_name": "image_classifier_v1",
    "accuracy": 1.5,
    "latency_ms": 75,
    "memory_mb": 1200,
}

# BUG 在编写基本的 pytest 测试时，标准的做法确实是 def test_...() 函数默认不传任何参数
# 但是我设了参数, 却没有在 function body 里面引用这个参数. 我本来就用了全局变量. 
# NOTE assert ... is True 就好 不用 == 
# def test_validate_model_run(model_run):
#     assert validate_model_run(model_run_1) == True
#     assert validate_model_run(model_run_2) == False

#BUG 这里如果model_run_1的 assert 失败了, 整个测试函数会立刻报错并退出, model_run_2 根本不会被执行 
# def test_validate_model_run():
#     assert validate_model_run(model_run_1) is True
#     assert validate_model_run(model_run_2) is False


@pytest.mark.parametrize(
    "sample_data, expected_result", 
    [
        (model_run_1, True),
        (model_run_2, False), 
    ],
)
def test_validate_model_run(sample_date, expected_result):
    assert validate_model_run(sample_date) == expected_result



# NOTE 关于 pytest 里测试 function 有 parameter 的情况, 如果没有 标记它是 parametrize , 那 pytest 会把它认为是一个 fixture 
# 它就会去“外面”找一个同名的、被特殊标记了 @pytest.fixture 的函数来喂给它

# 1. 这就是一个 Fixture。它的工作是“准备数据并返回”
@pytest.fixture
def model_run():
    # 比如从数据库读一条、或者生成一条合法的标准数据
    standard_data = {
        "model_name": "image_classifier_v1",
        "accuracy": 0.87,
        "latency_ms": 75,
        "memory_mb": 1200,
    }
    return standard_data  # 把数据返回出去


# 2. 你的测试函数通过“参数名”来向上面的 fixture 申请数据
def test_validate_model_run(model_run):
    # 注意！此时这里的 model_run 已经不是函数了，
    # 而是上面 fixture 返回回来的那个 standard_data 字典！
    assert model_run["accuracy"] == 0.87
    assert (
        validate_model_run(model_run) is True
    )  # 假装你有这个 validate_model_run 函数


# NOTE 关于用Fixture的好处 
# 1. 干净的隔离性（最重要）：全局变量是共享的。如果 test_A 拿到了 model_run_1 并把里面的 accuracy 改成了 0.0，那么紧接着运行的 test_B 拿到的全局变量就被污染了！而 Fixture 默认每执行一个测试函数，就会重新运行一次。它确保每个测试函数拿到的都是一份全新的、干净的数据，互不影响。
# 2. 不仅能生成数据，还能搞定“前后置操作”：比如在 AI 测试中，你需要在测试前连接 GPU 数据库，测试完后断开连接：
        # @pytest.fixture
        # def db_connection():
        #     db = connect_to_gpu_db()  # 1. 测试前：连接数据库
        #     yield db  # 2. 把连接“借给”测试函数使用
        #     db.close()  # 3. 测试完：自动断开连接（哪怕测试崩溃了也会执行）
# 3. 复用性极高：一个大型工程有 100 个测试文件都需要这个合法的 AI 模型数据，你只需要在一个叫 conftest.py 的公共文件里写一次这个 fixture，这 100 个文件就全都能直接在括号里调用它，无需重复复制粘贴。