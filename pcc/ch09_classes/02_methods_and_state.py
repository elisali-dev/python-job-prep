# ============================================================
# Ch09 - 02 Methods and State
# Knowledge Notes
# ============================================================

# 所有实例method 都得用 self 做第一个 argument 
# 其他method还有 static method (纯工具函数, 不能访问class的属性或对象的属性), class method (必须用 cls 做第一个 argument,代表当前类)

# 在 Python 中，self 并不是一个强制的关键字。如果你高兴，写成 def __init__(this, name): 也是完全可以运行的。但是强烈建议永远使用 self，因为这是全 Python 社区统一的黄金标准


# ------------------------------------------------------------
# 1. A method is a function defined inside a class
# 2. self refers to the current instance
# ------------------------------------------------------------
# Normal function:
#
# def get_experience_level(candidate):
#     ...
#
#
# Method:
#
# class Candidate:
#
#     def get_experience_level(self):
#          if self.years_experience >= 5:
#             return "Senior"
#         ...
#
#
# A method describes behavior that belongs to an object.

# ------------------------------------------------------------
# 3. Calling a method automatically supplies self
# 4. Methods can access object attributes
# 5. A method can return a value
# 6. Methods can use multiple attributes
# 7. Methods can modify object state
# 8. Methods can have parameters besides self (NOTE method can have parameters supplied by caller)
# 9. One method can call another method
# 10. Data + behavior live together
# 11. Why use update_score() instead of direct assignment?

# ------------------------------------------------------------

# We write:
#
# alex.get_experience_level()
#
# NOT:
#
# alex.get_experience_level(alex)
#
#
# Conceptually, Python is doing something similar to:
#
# Candidate.get_experience_level(alex)
#
# Python automatically passes the instance as "self".


# ================ Exercise ==================== 

class Candidate:
    def __init__(self,name, years_experience, technical_score):
        self.name = name
        self.years_experience = years_experience
        self.technical_score = technical_score
    # instance method (function inside a class) must has self as its argument! and must be the first argument!!! 
    # NOTE # self lets an instance method access the current object's attributes / state. -> 一个 instance 所有的 attribute 组合起来是这个 object 当前的 state  


    def get_experience_level(self):
        if self.years_experience >= 5:
            return "Senior"
        elif self.years_experience >=2:
            return "Mid"
        else:
            return "Entry"
    # 没有 self 就不能 refer instance  state (aka variable) 了
    def is_qualified(self):
        return self.years_experience >= 2 and self.technical_score >= 75 

    def update_score(self, new_score):
        # 最好加上invalid test 
        if 0 <= new_score <= 100:
            self.technical_score = new_score
            return True
        else:
            return False

    def get_decision(self):
        if self.is_qualified():
            return "Pass"
        else:
            return "Reject"

    



#====== Exer 1 Move Ch08 functions into the class  ===========    

alex = Candidate("Alex", 3, 82)
sam = Candidate("Sam", 1, 90)


print(alex.get_experience_level())
print(alex.is_qualified())

print(sam.get_experience_level())
print(sam.is_qualified())

#===== Exer 2 Modify state through a method ======
## 练习 method 控制 object state 的变化。
print(alex.technical_score)

result = alex.update_score(95)

print(result)
print(alex.technical_score)

#===== Exer 3 — One method calls another ======
## 测试 get_decision()

alex = Candidate("Alex", 3, 82)
sam = Candidate("Sam", 1, 90)

print(alex.get_decision())  # Pass
print(sam.get_decision())   # Reject