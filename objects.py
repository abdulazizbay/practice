import array
import math
from math import ceil, asin
print("==== what is object ====")
# An object has state and method properties
# Everything is object in python

print(type("hello world"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm => Functional Programming and OOP
# OOP 4concepts => Abstraction, Encapsulation, Inheritance, Polimorphism

result = math.ceil(95.3)  # Call
print(result)

result1 = ceil(92.3)
print(result1)

print("=== Error Handling System ===")

car_dict = dict(name="Tayota", year=2002, electric=False)

try:
    print("passed here")
    a = car_dict.speed
    result = car_dict["origin"]
    print("result", result)
except KeyError as err:
    print("this state not found:", err)
except AttributeError as err:
    print("atribute error happened:", err)
else:
    print("executed successfully without error")
finally:
    print("final closing logic")
