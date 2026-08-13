# Python 很常见的设计习惯：一个 method 如果主要作用是直接修改 object，通常不把修改后的 object return 给你 


# list.sort() #  modifies original list in-place -> return None 
# sorted(list) # original unchanged, returns a new sorted list -> return new list
# list.reverse() # modifies original list in-place  -> return None
# len(list) # returns number of elements -> return an int 

# Exercise 1 — sort() — permanently sort
print(f"\n{'=' * 20} EXER 1 - list.sort() - in-place sort {'=' * 20}")

cars = ["bmw", "audi", "toyota", "subaru"]
print (f"Before sort, original car list is {cars}" )

cars.sort()
result = cars.sort()
print (f" let result = cars. sort (),  result is {result}" )
print (f" after calling sort(), cars is {cars}")

cars.sort(reverse=True)
print (f" after calling sort(resverse = True), cars is {cars}")

# Exercise 2 - sorted() — temporary sorting
print(f"\n{'=' * 20} EXER 2 - sorted(list) - return new sorted object {'=' * 20}")

cars = ["bmw", "audi", "toyota", "subaru"]
print (f"Before sort, original car list is {cars}" )

print(sorted(cars)) # sorted() 是一个 built-in function，它 return 一个新的 list。
print(f"after calling sorted(cars), the orignal cars var is still {cars}\nsorted result is returned from the functional call sorted(cars)")

# Exercise 3 - reverse() — reverse()
print(f"\n{'=' * 20} EXER 3 - list.reverse() {'=' * 20}")
numbers = [1, 2, 3, 4]
print(f"Before list.reverse(), numbers is a list of {numbers}")
numbers.reverse()
print(f"Afer list.reverse(), numbers is a list of {numbers}")
print(numbers)

# Exercise 4 - len(list) 
print(f"\n{'=' * 20} EXER 4 - len(list) {'=' * 20}")
skills = ["python", "sql", "git"]

print(len(skills))


# Exer 1  - sort()
print(f"\n{'=' * 20} EXTRA EXER {'=' * 20}")
languages = ["python", "java", "c++", "sql"]
print(languages)
# print(languages.sort()) I guess it returned none? 
languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

# Exer 2 - sorted()
scores = [88, 72, 95, 81, 90]
print(f"Original: {scores}")
sorted_score = sorted(scores)
print(f"Sorted: {sorted_score}")
print(f"Original again: {scores}")

# Exer 3 - sort() return value 
numbers = [5, 2, 9, 1]

result = numbers.sort() # guess result is None 
print(numbers) # guess numbers is [1,2,5,9]
print(result)

# Exer 4 - reverse()
steps = ["collect data", "clean data", "train model", "deploy model"]
print (f"steps is {steps}")
steps.reverse() # guess it also return none? 
print(f"reverse()call one time, steps becomes {steps}")
steps.reverse()
print(f"reverse()call two times, steps becomes {steps}")

# Exer 5 - len()
applicants = ["alice", "bob", "charlie", "david", "emma"]
print (f"There are {len(applicants)} applicants.")

# Exer 6 - combine them
model_scores = [0.82, 0.91, 0.76, 0.88]
#print original
print (model_scores)

#print ascending sorted version，但 original 不变
sorted_asc = sorted(model_scores)
print(sorted_asc)

# print original again
print (model_scores)

# permanently sort descending
# model_scores.sort() # ascending 
model_scores.sort(reverse=True) # descending 
print (model_scores)
print(len(model_scores))

