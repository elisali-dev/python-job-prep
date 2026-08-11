# string is text enclosed by single quote or double quotes
# string is immutable. i.e. name.upper() doesn't modify orignal name variable value, unless you reassign it like name = name.upper()
# fstring

#Eexr 1 - Chaning Case
name = "ada lovelace"
print (f"{name.title()}")
# f-string 没必要。如果只是打印一个 expression，直接：print(name.title()) 更简单。
# f-string 主要用于把变量/表达式嵌进其他文字：例如 print(f"Hello, {name.title()}!")
print (f"{name.upper()}")
print (f"{name.lower()}")

#Exer 2- f string
first_name = "elisa"
last_name = "li"
job = "machine learning engineer"

print(f"{first_name.title()} {last_name.title()} is preparing to become a {job.title()}")

#Exer 3 - White space  
print (f"Skills:\n\tPython\n\tPytorch\n\tSQL")
# 这里不需要f-string. 没有函数,只有一个 expression 用 print("Skills:\n\tPython\n\tPyTorch\n\tSQL")

#Exer 4 - Stripping
language = "   Python   " # Spaces inside a string are part of the string.
print (language)
print (language.lstrip()) #? print such function call, is it good practice to add f-string or just write like this? 
print (language.rstrip())
print (language.strip())

language = language.strip()
print(language)

#Exer 5 — method chaining

language = "   machine learning   "

language = language.strip().upper()
print(language)

# Exer6 — removeprefix

github_url = "https://github.com/elisali-dev"
new_url = github_url.removeprefix("https://")
print(github_url) # orginal URL doesn't change 
print(new_url)

# Close-book exer
first_name = "  alice"
last_name = "wang  "
role = "machine learning engineer"

print(f"Employee: {first_name.strip().title()} {last_name.strip().title()}\nRole: {role.upper()}")