class Animal:
    def speak(self):
        print("Animal speaking")


class Cat(Animal):
    def speak(self):
        print("meow")


class Dog(Animal):
    def speak(self):
        print("gaw")

class CatDog (Cat, Dog):
    def speak(self):
        print("meow gaw")
         