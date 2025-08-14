# ///////////////////////////// Encapsulation ////////////////////////////


# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def getAnimal(self):
#         print(f"Animal Name: {self.name}")

#     def getSound(self):
#         print(f"Animal Sound: {self.sound}")


# a1 = Animal("Dog", "Bark")
# a1.getAnimal()
# a1.getSound()


# //////////////////////////// Abstraction ////////////////////////////

# from abc import ABC, abstractmethod

# class Animal:
#     @abstractmethod
#     def walk(slef):
#         pass


# class Hen(Animal):
#     def walk(self):
#         print("Hen Walk on 2 legs")


# class Horse(Animal):
#     def walk(self):
#         print("Horse Walk on 4 legs")


# h1 = Hen()
# h1.walk()

# h2 = Horse()
# h2.walk()


# /////////////////////////////////////// PolyMorphism ////////////////////
# class Animal:
#     def eat(self):
#         print("Animal Eats Anythings")


# class Deer(Animal):
#     def eat(self):
#         print("Deer Eats Grass")


# a1 = Animal()
# a1.eat()
# b1 = Deer()
# b1.eat()


# /////////////////////////////////////////////////////////////////////////////////////
# import time

# aa = time.asctime((time.localtime(time.time())))
# print(aa)

# //////////////////////////// enumerator ///////////////////////////////

# list1 = ["apple", "mango", "orange"]
# for index, x in enumerate(list1):
#     print(index, x)

# ///////////////////////////  higher order function ////////////////////////////

# list1 = [1, 2, 3, 4, 5]

# # list2 = list(map(lambda x: x + 1, list1))
# # print(list2)

# # list2 = list(filter(lambda x: x > 3, list1))
# # print(list2)

# from functools import reduce

# sum = reduce(lambda x, y: x + y, list1)
# print(sum)
