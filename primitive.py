print("==========")

# in Js , variable is a name of storage location
# in python, variable is a named reference

count = 100
count_type = type(count)
print(f"the count: {count} and type: {count_type}")

result1 = count.bit_count()
result2 = count.numerator
print(result1, result2)

print("====  string ======")
# Methods: upper(), lower(), title(), find(), replace()

course = "AI Python Fullstack"
result = type(course)
print(f"the type of course: {course}")
result = course.title()
print(f"result1 : {result}")

result = course.upper()
print(f"result2 : {result}")

result = course.replace("Fullstack", "Masterclass")
print(f"result3 : {result}")

print("==== boolean =====")

y = input("give ur value for y: ")
result = y.isnumeric()
print(f"result is numeric: {result}")

# Truthy =>  all others
# Falsy => false, 0 , "", none
test_falsy = "" or False or None or 0
print("the test falsy:", bool(test_falsy))

test_truthy = "dsds"
print("the test truthy:", bool(test_truthy))
