# /////////////////  Encapsulation ////////////////////////

# class Animal:
#     def __init__(self, name, sound):
#         self.__name = name
#         self.__sound = sound

#     def getName(self):
#         print("Animal Name: ", self.__name)

#     def getSound(self):
#         print("Animal Sound: ", self.__sound)


# a1 = Animal("Dog", "Bark")
# a1.getName()
# a1.getSound()


# /////////////////////// PolyMorphism /////////////////////

# class Animal:
#     def speak(self):
#         print("Animal Make a Sound")


# class Hen:
#     def speak(self):
#         print("Hen Make Che Che")


# class Horse:
#     def speak(self):
#         print("Horse make Houre Houre")


# # a = Animal()
# # a.speak()

# Animal().speak()
# Hen().speak()
# Horse().speak()


# //////////////////////////////////// Abstract /////////////////////////

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Hen(Animal):
    def move(self):
        print("Hen Move on 2 Legs")


class Horse(Animal):
    def move(self):
        print("Horse Move on 4 Legs")


a1 = Horse()
a1.move()
