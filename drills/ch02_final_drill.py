# pcc = 跟着书练 , drills = 不看书自己做

# """
# 假设：
# employee first name: "  alice"
# employee last name: "WANG  "
# role: "machine learning engineer"
# hourly rate: 135
# hours/week: 40
# working weeks/year: 48
# savings rate: 20%
# 
# 你的程序最终输出：
# Employee: Alice Wang
# Role: MACHINE LEARNING ENGINEER
# Weekly income: $5,400.00
# Annual income: $259,200.00
# Monthly average: $21,600.00
# Annual savings: $51,840.00
# 
# 要求你自己用到：
# variables
# .strip()
# .title()
# .upper()
# arithmetic
# f-string
# :,.2f
# 一个 uppercase constant
# 
# """


employee_first_name = "  alice"
employee_last_name = "WANG  "
role = "machine learning engineer"
hourly_rate = 135
hours_per_week = 40
working_weeks_per_year = 48
SAVINGS_RATE = 0.2

#Employee: Alice Wang
name = employee_first_name.strip().capitalize() + " " + employee_last_name.strip().capitalize()
print(f"Employee: {name}")
# Role: MACHINE LEARNING ENGINEER
print(f"Role: {role.upper()}")
# Weekly income: $5,400.00
weekly_s = hourly_rate * hours_per_week
print (f"Weekly income: ${weekly_s:,.2f}")
# Annual income: $259,200.00
annual_s = weekly_s * working_weeks_per_year
print (f"Annual income: ${annual_s:,.2f}")
# Monthly average: $21,600.00
print (f"Monthly average: ${annual_s / 12:,.2f}")
# Annual savings: $51,840.00
print (f"Annual savings: ${annual_s * SAVINGS_RATE:,.2f}")