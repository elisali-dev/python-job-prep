ml_stack = ["python", "tensorflow", "sql"]

# desired output ["python", "pytorch", "git", "sql"]
# 要求必须用到：
# 修改某个 index, 
# insert()
# 不要重新手写整个 list
# 然后： 
# pop() 最后一个元素并保存
# print 被 pop 的 value
# 再 print 最终 list

ml_stack[1] = "pytorch"
ml_stack.insert(2, "git")
last_element = ml_stack.pop()
print(last_element)
print (ml_stack)