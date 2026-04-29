print("=== what is comprehension and list comprehension ===")
# comprehension acts like spread operator

''' 
Comprehension general syntax:
    a) iterable
    b) <expression> for item in iterable
    c) <expression> for item in iterable <condition>
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers]  # a version

print("list_numbers: ", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("---")
people = [
    ("Robert", 20),
    ("Max", 232),
    ("Steve", 53),
    ("Jenny", 10),
]
list_people = [person[0] for person in people]  # b version
print("list_people: ", list_people)

print("-----")
cars = [
    ("Ferrari", 78),
    ("BMW", 103),
    ("MERS", 18),
    ("AUDI", 131),
    ("LAMBO", 43),
]
list_cars = [car[0] for car in cars if car[1] > 80]
print(list_cars)
