print("=== Inheritance ===")

# Parent > Child
# Parent provides only public and _protected properties(state + method) to children


class Animal:  # Parent
    # state
    description = "this class creates animals"
    # constructor

    def __init__(self, voice):
        self._voice = voice

    # method
    def make_voice(self):
        print(f"animal can make voice: {self._voice}")


class Dog(Animal):  # Child
    # state
    # constructor
    def __init__(self, voice, name, sound):
        super().__init__(voice)
        self.name = name
        self.sound = sound
    # method

    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def protect(self):
        print("yes i can protect u")

    def make_voice(self):
        print(f"{self.name} says: {self.sound}")


class Cat(Animal):  # Child
    # state
    # constructor
    def __init__(self, voice, name, sound):
        super().__init__(voice)
        self.name = name
        self.sound = sound

    # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def play(self):
        print("yes i play")


class Fish(Animal):  # Child
    # state
    # constructor
    def __init__(self, voice, name, sound):
        super().__init__(voice)
        self.name = name
        self.sound = sound
    # method

    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def swim(self):
        print("yes i can swim")


dog = Dog(True, "Bobik", "woff")
cat = Cat(True, "Tom", "myew")
fish = Fish(False, "Nemo", "ZZZ")

dog.introduce()
cat.introduce()
fish.introduce()

dog.make_voice()
cat.make_voice()
fish.make_voice()

print(Animal.description)
print(dog._voice)

print("=== Polymorphism ===")  # bir xil method lekn xar xil vazifa
dog.make_voice()
cat.make_voice()

print("-----")
# fish > Fish > Animal > object
a = isinstance(fish, Fish)
b = isinstance(fish, Animal)
c = isinstance(fish, object)
print("result:", a and b and c)

# Fish > Animal > object

data1 = issubclass(Fish, Animal)
data2 = issubclass(Animal, object)
print("data:", data1, data2)
