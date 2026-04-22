print("=== What is Tuple: tuple vs list ===")
# Java/PHP/Nodejs array => python list

# literal
numbs = [3, 5, 1, 2]

# constructor
letters = list("Hello World")
print(letters)

fruits = ["apple", "lemon ", "banana", "kiwi"]
print("before fruits: ", fruits)

fruits[2] = "mango"
print("after fruits:", fruits)

# tuples == list but  we cannot mutate tuple
animals = ("dog", "cat", "fish")
tuple_obj = ("MIT", 100, True, None)

print(animals[0])
# animals[0] = "penguin"  # error - tuple cannot be changed
