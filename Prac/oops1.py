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


# //////////////////////////////////////////////////////////////////////////////

# list1 = [1, 2, 3]

# list2 = [4, 5, 6]
# list3 = list(zip(list1, list2))

# print(list3)


# /////////////////////////////////////////////

# list1 = [1, 2, 3, 4, 5]

# # map
# list2 = list(map(lambda x: x + 1, list1))
# print(list2)

# # Filter

# list3 = list(filter(lambda x: x > 3, list1))
# print(list3)

# from functools import reduce

# list4 = int(reduce(lambda x, y: x + y, list1))
# print(list4)


# ////////////////////////////////////////  try catch finally ////////////////////////////

# try:
#     a = int(input("Enter a Number 1"))
#     b = int(input("Enter a Number 1"))
#     print(a + b)

# except:
#     print("Some thing went wrong")
# finally:
#     print("Done")


# def fun():
#     pass


# fun()


# def gen():
#     yield 1
#     yield 2


# gen()


# ///////////////////////////////////////////////////////////////////////////////


# class MyClass:
#     class_var = "Hello"

#     @staticmethod
#     def static_method():
#         print("I don’t need class or object.")

#     @classmethod
#     def class_method(cls):
#         print("I can access:", cls.class_var)


# # Usage
# MyClass.static_method()  # Works without object
# MyClass.class_method()


# /////////////////////////
# def my_gen():
#     for i in range(3):
#         yield i


# for val in my_gen():
#     print(val)


# ///////////////////////////////////////////////// reverse a string ////////////////////
str = "Hello Sabaz Alam"

# str2 = str[::-1]
# print(str2)

# str2 = "".join(reversed(str))
# print(str2)

str3 = str[::-1]
print(str3)
