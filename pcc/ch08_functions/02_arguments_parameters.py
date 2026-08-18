# NOTE 👇- Parameter vs Argument
# name
# → parameter
# → function 定义时使用的 variable
# 
# "Alex"
# → argument
# → call function 时实际传进去的 value

def greet(name):
    print(f"Hello, {name}!")

greet("Alex")




# NOTE 👇 Positional Aruments
# 这里默认按照 position 对应：
# "Alex" → name
# 3      → years
# 这叫 positional arguments。顺序错了, Python 不一定报错，但语义就错了。

def describe_candidate(name, years):
    print(f"{name}: {years} years experience")

describe_candidate("Alex", 3)



# NOTE 👇 Keyword Arguments 
describe_candidate(name="Alex", years=3)
describe_candidate(years=3, name="Alex")
# 带上 keyword 之后, 顺序可以打乱, Python 不再靠 position 猜，而是根据 parameter name 匹配。

# NOTE 👇 default parameter 
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alex") # 默认参数是可选参数. ‼️ 
greet("Alex", "Welcome")

# NOTE syntax rule ✅ required parameter 先放。
# 不要：def greet(greeting="Hello", name): ❌ 会 SyntaxError。

# ================ Exercise 1 - parameter vs argument ==================== 
print(f"\n{'=' * 20} Exercise 1 {'=' * 20}")

def show_candidate(name):
    print(f"Candidate: {name}")

show_candidate("Alex")
show_candidate("Emma")
show_candidate("Sam")

# ================ Exercise 2 - multiple parameters ==================== 
print(f"\n{'=' * 20} Exercise 2 {'=' * 20}")

def show_candidate_summary(name, years_experience, technical_score):
    print(
        f"Candidate: {name}\n"
        f"Experience: {years_experience}\n"
        f"Technical score: {technical_score}"
    )

# ================ Exercise 3 - positional vs keyword arguments ==================== 
print(f"\n{'=' * 20} Exercise 3 {'=' * 20}")

show_candidate_summary("Alex", 3, 82)

# NOTE 普通 assignment 两边留空格, 但
# Python style 推荐 keyword argument 的 = 两边不留空格：
show_candidate_summary(name="Emma", years_experience=6, technical_score=92)

# NOTE show_candidate_summary(3, 82, "Alex") this works but positional arguments order matters, you have to watch yourself


# ================ Exercise 4 - default parameter ==================== 
print(f"\n{'=' * 20} Exercise 4 {'=' * 20}")

def show_model(model_name, device = "cpu"):
    print(f"Model: {model_name}")
    print(f"Device: {device}")

show_model("resnet18")
show_model("transformer", "cuda")

# ================ Experiment ==================== 
print(f"\n{'=' * 20} Experiment {'=' * 20}")

def test(a, b=10):
    print(a, b)

test(5)
test(5, 20)
test(a=5, b=30)
test(b=30, a=5)

## BUG SyntaxError: parameter without a default follows parameter with a default
# def test(a=10, b): 
#    pass # NOTE 空操作占位符，用来保证代码结构的完整性，它什么都不做


# ================ Closed book drill ==================== 
print(f"\n{'=' * 20} closed book drill {'=' * 20}")

def evaluate_candidate(name, years_experience, technical_score):
    if years_experience >= 2 and technical_score >= 75:
        print(f"{name}: Pass")
    else:
        print(f"{name}: Reject")

evaluate_candidate("Emma", 3, 90)
evaluate_candidate(years_experience=5,technical_score=70,name="Sam")

