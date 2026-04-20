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
