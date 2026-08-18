# exer 1 
def show_welcome(): # : 代表 function header 结束
    print("Welcome to Python Job Prep!") # function body 需要 indentation - 4 spaces 

show_welcome()

# exer 2 
def print_report_header():
    print("=" * 30)
    print("Candidate Report")
    print("=" * 30)

print_report_header()

# exer 3 
def show_python_skills():
    skills = ["python", "sql", "pytorch"]
    for skill in skills:
        print(f"Skill:{skill}")

show_python_skills()

# exer 4 
def say_goodbye():
    print("Goodbye!")        
# NOTE
# Defining a function does not execute it.
# The function runs only when you call it
say_goodbye()

