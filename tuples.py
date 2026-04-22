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

print("=== Unpacking arguments ===")
groups = ["MIT", "Flexy", "devex", "mg"]

(x, y, *z) = groups
print(f"x-{x} , y-{y}")
print("z", z)

# *args => tuple


def calculate(*args):
    print("*args:", args)
    total = 1
    for x in args:
        total *= x
    print("total:", total)
    return total


calculate(1, 7, 2, 3)
