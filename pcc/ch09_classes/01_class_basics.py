# ================ Exercise 1  First Candidate Class ==================== 
print(f"\n{'=' * 20} Exercise 1 First Candidate Class {'=' * 20}")


# 即使 __init__ 没有定义参数（或者你根本没写 __init__），你依然可以在创建对象后，随时动态地为它添加属性。例如在 instantiation 后 打 code candidate.name = "Alice"
# NOTE 虽然 Python 支持这种动态添加属性的做法，但在实际开发中，更推荐把所有属性都在 __init__ 里初始化（哪怕先赋值为 None），这样代码更具可读性。

class Candidate:
    def __init__(self, name, years_experience, technical_score):
        #BUG
        # self.name = "name"
        # name 是paramter, "name" 就是表面的字符串, self.name 是attribute 
        self.name = name
        self.years_experience = years_experience
        self.technical_score = technical_score


# 实例化一个类不需要 new 关键字。你只需要像调用函数一样，在类名后面加上括号 () 即可。
# Python 的一个类只能有一个 __init__ 方法。一旦你定义了带参数的 __init__(self, name, age)，Python 就不再允许你通过不传参数的方式 MyClass() 来实例化对象了
# 一个 class 最终只能有一个名字叫 __init__ 的 method
# Python 没有 Java 那种 method overloading。
# 以后 Python 通常用：def __init__(self, name, score=0): default parameters，或者其他方式来实现不同创建方式，而不是 Java 那种 constructor overloading。

candidate = Candidate("Alex", 3, 82)

print(f"Candidate: {candidate.name}")
print(f"Experience: {candidate.years_experience}")
print(f"Score: {candidate.technical_score}")


# ================ Exercise 2 Multiple instances ==================== 
print(f"\n{'=' * 20} Exercise 2 Multiple instances {'=' * 20}")

candidate_B = Candidate("Emma", 6, 92)
candidate_C = Candidate("Sam", 1, 90)

print(candidate_B.name)
print(candidate_B.technical_score)
print(candidate_C.name)
print(candidate_C.technical_score)


# ================ Exercise 3 ==================== 
print(f"\n{'=' * 20} Exercise 3 Modify attribute {'=' * 20}")

alex = Candidate("Alex", 3, 82)
print(f"Before: {alex.technical_score}")
# object attribute 默认也是可以修改的
#BUG alex.score = 90 # python 没报错,输出 score 还是 82. 因为它又加了一个 attribute score 
# 动态性方便，但也意味着 typo 风险更高

alex.technical_score = 90
print(f"After: {alex.technical_score}")


# ============= Experiment =============== # 
print(f"\n{'=' * 20} Experiement {'=' * 20}")

class Candidate:

    def __init__(self, name):
        self.name = name


alex = Candidate("Alex")
emma = Candidate("Emma")

print(id(alex))
print(id(emma))

alex.name = "Alexander"

print(alex.name)
print(emma.name)