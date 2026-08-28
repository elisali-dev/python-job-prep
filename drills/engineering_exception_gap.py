#======== Challenge ==============
def calculate_average(total_score, count):
    if count == 0:
        raise ValueError("Your count is 0")
    return total_score / count

def generate_report (total_score, count):
    result = calculate_average(total_score, count)
    return result

try:
    print(generate_report(100, 2))
except ValueError as error:
    print(f"Error caught:{error}")



#========= Experiment 3 — 最关键：exception 可以跨 function 往上传 =========== 
def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    return True

def process_candidate (candidate):
    validate_score(candidate["score"])

    print ("Candidate processed.")

candidate = {
    "name": "Alice",
    "score": 120,
}

try:
    process_candidate(candidate)
except ValueError as error:
    print(f"Processing failed: {error}")
# ============= NOTE exception propagation ==========
# exception propagation 
# 观察上边的逻辑, validate_score() 自己没有：try / except; process_candidate() 也没有。 但是最外层有 也依然可以 catch 最里层的 exception 
# main/top level -> process_candidate() -> validate_score() -> rasie ValueError -> validate_score 没处理 -> process_candidate 没处理 - 外层 try 找到 except ValueError - > handled
#‼️ validation 层负责发现问题，workflow 层负责决定问题发生以后怎么办。一个重要 engineering principle 是：能 catch，不代表应该在这里 catch。
#‼️ 发生错误的地方 ≠ 最适合处理错误的地方。 


#======== Experiment 2 - try/except ========== 
def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
    return True

print("Before Validation:")
try:
    validate_score(120) # 如果这里出现exception, 触发异常后，try 块内后续的代码（如果有的话）会被立刻中断，程序直接跳到 except 区域寻找匹配的捕获器。
except ValueError as error:
    print(f"Validation failed: {error}") # 异常被捕获并处理. 异常像是一个警报，except 把它关掉了，所以后面的生活继续。

print("After validation") # 如果except 没有捕获 ValueError 这里不会执行


#======== Experiment 1 - What does Raise do ? ========== 
def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")
        # raise ValueError(...) 不是 return 一个 error
        # 而是 打断当前正常执行流程, 并产生一个exception object. 所以后边正常代码不会继续往下走 

    return True

print("Before validation")
validate_score(120)
print("After validation")


# #====== LEARNING NOTE ===========
# except 是“报错了才执行”。
# else 是“没报错才执行”。else 块只有在 try 里面的代码顺风顺水、没有发生任何异常的情况下，才会进入执行。
# try-except 外部的代码 则是“只要程序没崩溃，无论报不报错都执行”。 aka Exception 被 catch 后，程序可以继续。
    # 1. 裸写 `except` (最宽泛,拦截一切)
    # 2. 捕获基类 except Exception: (最常用:拦截所有常规业务错)
    # 3. 精准捕获多个特定错误 (最佳实践:对症下药) 
        # 通常建议明明白白地列出你预期的错误。如果你想用同一套逻辑处理两种不同的错误，可以用元组 (Tuple) 把它们包起来
        # 比如 except (FileNotFoundError, ValueError) as error:
# finally 专门用来写“无论发生什么惊天动地的大事，都必须履行的安全契约”。
    # 1. 当 try 或 except 块中包含了 return（最常见）在函数内部，一旦遇到 return，整个函数就会立刻结束并退出。写在try-except 外面的代码不会被执行
        # 但 Python 有一个铁律——无论你怎么 return，都必须先执行完 finally 里的代码，才准允许函数带着返回值真正离开。
    # 2. 如果程序抛出了一个你没有用 except 捕获的严重错误（或者你故意 raise 了一个新错误）：
        # 写在外面：程序直接在报错行当场崩溃（Crash）退出，后面的代码直接沦为死代码。
        # 写在 finally 内：程序崩溃前，会强行把 finally 里的遗言（善后代码）执行完毕，然后才崩溃。
    # 3. 在循环（for / while）中使用了 break 或 continue当你在循环中进行错误处理，并使用 break 强行跳出循环时：
        # 写在外面：跳出循环意味着直接去执行循环外层的东西了。
        # 写在 finally 内：在拍拍屁股走人（break）之前，必须把这一轮的 finally 账结清。
    # 4. 最核心的适用场景
        # 资源释放（Cleanup Actions）：关闭文件（防止内存泄露）
        # 断开数据库连接（防止连接数占满导致服务器瘫痪）
        # 释放网络 Socket 锁
        # 现代 Python 中，我们经常使用的 with open(...) 语法，其底层原理其实就是自动帮我们写了一套带 finally 自动关闭文件的逻辑。


# =============== LEARNING NOTE ===============
# 真正理解 exception 是怎么产生、怎么向上传递、在哪里被处理的。
#try: except: 不仅仅是防止程序报错
# 它的流程是 
#             某个 function 发现自己无法正常完成任务
#                     ↓
#             raise Exception
#                     ↓
#             当前正常执行流程立即停止
#                     ↓
#             exception 沿 function-call chain 往上传
#                     ↓
#             如果某一层 except 它
#                     → 这一层处理
#             
#             如果一直没人 except
#                     → program terminates
#                     → traceback


#======= raise vs return =================

# 特性              return                                                         raise       
# 程序意图      # 顺畅交付结果。我算好数据了，给你结果，继续下一步。              # 拉响紧急警报。发生了意外，我无法处理，请求紧急救援！
# 控制流方向    # 回到上一层调用者的下一行代码，继续往下走。                     # 顺着调用栈一路向上引爆，直到被 except 拦截。
# 对程序的影响  # 属于正常的、预料中的程序流。                                 # 如果沿途没有任何 except 捕获它，程序会当场崩溃 (Crash)。

# return ValueError("报错对象") 
    #   # 如果只是 return, 程序还是继续向下走
# raise Valueerror("报错对象") 
    # NOTE except 块只认 raise
    #   # 在后台发生了两步 
                # 1: 创建 ValueError Object 
                # 2: 发射投掷,向 python interpreter叫嚣, 然后让python 解释器触发中止当前函数后续运行,开始找 try..except 盾牌, 如果找到就处理,没有找到程序就崩溃
# return False/ None 
    # Use return False (or return None) when the failure is a normal, common, and expected outcome of the business logic. The calling code should easily handle it with a simple if statement.