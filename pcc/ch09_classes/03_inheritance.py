# ============================================================
# Ch09 - 03 Inheritance
# Knowledge Notes
# ============================================================


# ------------------------------------------------------------
# 1. Inheritance = create a more specific class from another class
# 2. Basic inheritance
# 3. Child class can have its own __init__()
# 4. super()  
            #  super() gives access to the parent class behavior.
            # In:
            # super().__init__(name, years_experience, technical_score)
            # we are saying:
            # "Let Candidate.__init__ initialize the Candidate part of this object."
#  
# 5. Child class can add new methods
# 6. Method overriding       
# 7. Inherited methods use the child object's state
# 8. is-a relationship
# 9. Inheritance is NOT just for code reuse. Otherwise, composition might be better fit. 
# ------------------------------------------------------------


class Candidate:
    def __init__(self, name, years_experience, technical_score):
        self.name = name
        self.years_experience = years_experience
        self.technical_score = technical_score

    def get_experience_level(self):
        if self.years_experience >= 5:
            return "Senior"
        elif self.years_experience >= 2:
            return "Mid"
        else:
            return "Entry"

    def get_decision(self):
        if self.technical_score >= 75:
            return "General Interview"
        return "Reject"



#======= Exer 1 - Basic Inheritance ============
class MLCandidate_1(Candidate):
    # # 所以 child init 方法不能直接 pass super as method paramter 直接继承所有 attribute? 所有attribute 还得在 child 这 init list 一遍? 
    # def __init__(self, name, years_experience, technical_score):
    #     #BUG 不是 super.__init__(), super 后边缺了括号
    #     super().__init__(name, years_experience, technical_score)
    # super()是一个特殊 helper，让你从当前 class 的继承关系中访问 parent behavior。
    pass 
# NOTE - 上边可以直接写 pass 我的 overriding init 纯属多余 
# Child 如果不需要新的初始化逻辑 → 不要写 __init__  
# 因为 MLCandidate 自己没有 __init__()，Python 就会去 parent Candidate 找： Candidate.__init__() -> Candidate("Alex", 3, 82) 的初始化逻辑直接复用 


print("="*10 + "Exer 1" + "="*10)

alex = MLCandidate_1("Alex", 3, 82)
print(alex.name)
print(alex.technical_score)
print(alex.get_experience_level())

#======= Exer 2 - super() + child-specific state =========
print("="*10 + "Exer 2" + "="*10)

class MLCandidate_2(Candidate):
    def __init__(self, name, years_experience, technical_score, ml_framework):
        super().__init__(name, years_experience,technical_score)
        self.ml_framework = ml_framework
        # Child 有自己的额外 state → 才需要自己的 __init__
        # NOTE Q - “所有 parent attributes 还得在 child parameter list 里写一遍吗？”
        # Answer -  如果 caller 仍然需要在创建 child object 时提供这些 values，通常需要。不是因为 child 需要“重新定义”这些 attributes。它只是需要接收 arguments，然后转交 parent initializer。

alex = MLCandidate_2(
    "Alex",
    3,
    82,
    "PyTorch",
)

print(alex.name)
print(alex.ml_framework)
print(alex.get_experience_level())


#======= Exer 3 - Add + Override methods =========
print("="*10 + "Exer 3" + "="*10)

class MLCandidate_3(Candidate):
    def __init__(self, name, years_experience, technical_score, ml_framework):
        super().__init__(name, years_experience,technical_score)
        self.ml_framework = ml_framework

    def get_decision(self):
        if self.technical_score >= 75 and (self.ml_framework == "PyTorch" or self.ml_framework == "TensorFlow"):
            # 更pythonic 的写法 self.ml_framework in ("PyTorch", "TensorFlow")
            return "ML Interview"
        return "Reject"

    # def get_decision(self):
    # if (
    #     self.technical_score >= 75
    #     and self.ml_framework in ("PyTorch", "TensorFlow")
    # ):
    #     return "ML Interview"

    # return "Reject"

        
alex = MLCandidate_3("Alex", 3, 82, "PyTorch")
sam = MLCandidate_3("Sam", 4, 90, "Excel")

print(alex.get_decision())
print(sam.get_decision())

# 在 Python 里面，子类重写（overriding）父类方法时，方法签名（参数列表）不一定要完全相同。Python 是动态类型语言，不会强制要求参数严格一致。如果你改变了参数，它依然是重写（覆盖）了原本的方法名，不会自动创建一个全新的独立方法，但调用时如果参数不匹配会报错。行为说明同名即覆盖：只要子类定义了和父类同名的方法，无论参数怎么变，这个名字在子类中都指向新方法。不会自动创建新方法：它不会同时保留父类的方法和子类的新方法，子类实例只会访问到子类自己写的那一个。