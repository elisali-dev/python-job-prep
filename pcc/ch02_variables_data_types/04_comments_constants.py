# Comment 
    # 好的 comment 主要解释why，而不是重复 code 已经告诉你的 what。
    # Python 没有像 C++ 或 Java 那样的专门多行注释符号（比如 /* ... */）。它只有用 # 的单行注释
    # 常用替代方法
        # 连续单行注释：在每一行前面都加上 #。这也是官方和社区最推荐的做法。VS code 里 [cmd+option + 向下箭头]可以使变成多行光标,打一个字符就可以插入多行
        # 三引号（""" 或 '''）：虽然它本质上是“多行字符串”，如果它没有赋值给任何变量，Python 就会忽略它，所以常被当多行注释使用（通常用于函数或类说明，即 Docstring）。
# Constant
    # Python 没有真正强制的 constant keyword。
    # 大家约定用 ALL_CAPS 表示： “这个 value 不应该被修改。
    # 但是你还是可以改它的值 , 因为 python 并没有强

