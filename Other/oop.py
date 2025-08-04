# class Student:
#     @staticmethod
#     def college():
#         print("ABC College")


# s1 = Student()
# s1.college()


# ///////////// Encapsulation

# class Animal:
#     def __init__(self, name, sound):
#         self.__name = name
#         self.__sound = sound

#     def speak(self):
#         print(f"{self.__name} make {self.__sound}")

#     def get_name(self):
#         print(f"Animal Is {self.__name}")


# a1 = Animal("Dog", "Bhoue")
# a1.speak()
# a1.get_name()

# //////////////////// Abstraction

# from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def walk(self):
#         pass


# class Hen(Animal):
#     # def walk(self):
#     #     print("hen Walk on 2 Legs")
#     def eat(self):
#         print("Eat Insects")


# class Horse(Animal):
#     def walk(self):
#         print("Horse Walk on 4 Legs")


# h1 = Hen()
# h1.eat()

# h2 = Horse()
# h2.walk()


# /////////////////////////////// Inheritence ////////////


# 1) single level inheritence

# class Animal:
#     def eat(self):
#         print("Animal Eats")

#     def breadth(self):
#         print("Animal Breadth")


# class Dog(Animal):
#     def walk(self):
#         print("Dog walk on 4 legs")


# d1 = Dog()
# d1.eat()
# d1.walk()


# 2)Multi Level Inheritence

# class Animal:
#     def eat(self):
#         print("Animal Eats")

#     def breadth(self):
#         print("Animal Breadth")


# class Mammal(Animal):
#     def birth(self):
#         print("Give Birth Directly")


# class Dog(Mammal):
#     def walk(self):
#         print("Walk on 4 legs")


# d1 = Dog()
# d1.birth()
# d1.walk()


# 3)////////////////// Hierarchial Inheritence

# class Animal:
#     def eat(self):
#         print("Animal Eats")

#     def Breadth(self):
#         print("Animal Breadth")


# class Fish(Animal):
#     def live(self):
#         print("Fish Live in Water")


# class Dog(Animal):
#     def live(self):
#         print("Dog Live in Land")


# f1 = Fish()
# f1.live()


# ///////////////////////////// Hybrid Inheritence //////////////
# class Animal:
#     def eat(self):
#         print("Animal Eats")

#     def breadth(self):
#         print("Animal Breadth")


# class Bird:
#     def fly(self):
#         print("Bird Fly in Sky")


# class Mammal:
#     def birth(self):
#         print("Mammal Give Birth Directly")


# class Bat(Bird, Mammal):
#     def sleep(self):
#         print("Bird Sleep Upside Down")


# b1 = Bat()
# b1.birth()
# b1.sleep()


# /////////////////////////// Hybrid


# class Animal:
#     def eat(self):
#         print("Animal Eats")

#     def breadth(self):
#         print("Animal Breadth")


# class Bird(Animal):
#     def fly(self):
#         print("Bird Fly in Sky")


# class Mammal(Animal):
#     def birth(self):
#         print("Mammal Give Birth Directly")


# class Bat(Bird, Mammal, Animal):
#     def sleep(self):
#         print("Bird Sleep Upside Down")


# b1 = Bat()
# b1.birth()
# b1.sleep()
# del b1.eat()
# b1.eat()


# /////////////////////// super
# class Animal:
#     def eat(self):
#         print("Animal is Eating")


# class Dog(Animal):
#     def eat(self):
#         super().eat()
#         print("Dog is Eating")


# d1 = Dog()
# d1.eat()


# method overloading
# class Calculate:
#     def add(self, a=0, b=0, c=0):
#         return a + b + c


# c1 = Calculate()
# print(c1.add(2, 2, 2))


# ///////////////////////////////////////// list
# list = ["apple", "mango", "orange", "grapes"]

# # for x in list:
# #     print(x, " ", end="")

# a = " ".join(list)
# print(a)
# print(len(a))


# ////////////////////////////// copy
import copy

list = [[1, 2], [3, 4]]

shallow = list.copy()
deep = copy.deepcopy(list)
list[0][0] = 100
print(shallow)
print(deep)
