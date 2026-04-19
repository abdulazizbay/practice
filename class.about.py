

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
