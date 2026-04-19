

print("=== what is class ===")


class Person():
    # state
    message = "class state property"
    # constructor

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method

    def introduce(self):
        print(f"{self.name} says: How do u do")

    def say_age(self):
        print(f"{self.name} says i am {self.age}!")

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 = Person("Abdulaziz", "42")
person2 = Person("Bunyod", "4322")

# ordinary state
print("person1 name: ", person1.name)

# ordinary method
person1.introduce()
person2.say_age()

print("=== ordinary vs static property ===")
# static state
new_message = Person.message
print("new message:", new_message)

# static method
Person.explain()


print("=== special/magic methods ===")


class Car():
    # state
    description = "this class makes cars"
    # constuctor

    def __new__(cls, *args):
        print("*__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year
    # methods

    def start_engine(self):
        print(f"the {self.name} started engine")

    def stop_engine(self):
        print(f"the {self.name} stopped engine")

    def __str__(self):
        return f"{self.name} was produced in {self.year} year!"

    def __call__(self):
        print(f"Obj called __call__")
        return True


myCar = Car("Ferrari", 2025)
myCar.start_engine()
myCar.stop_engine()

print("-------")
your_car = Car("Tayota", 2026)
print(your_car)  # __str__
response = your_car()  # __call__
print(response)
