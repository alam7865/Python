# print random number

# import random
# print(random.randrange(1, 6))

# ////////////// Display the price upto 2 decimal place
a = 8

# print(f"The value of 2 IS:{a:.2f}")


# ///////////////// List operation /////////////////////////////
# list = []

# # // add
# list.append("apple")
# list.append("mango")
# list.append("orange")

# update
# list[0] = "Banda Govi"

# delete
# del list[0]

# list clear
# list.clear()

# print(list)

# ///////////////////////////// Tuple  ////////////////
# tuple1 = ("apple",)
# list1 = list(tuple1)
# list1.append("mango")
# list1.append("orange")
# tuple1 = tuple(list1)
# print(tuple1)

# ///////////////////////////// set //////////////////
# set1 = set()
# set1.add("apple")
# set1.add("mango")
# set1.add("orange")

# for x in set1:
#     print(x)

# ///////////////////////////// dictionary /////////////
# dict1 = {}

# # add

# dict1[0] = "apple"
# dict1[1] = "mango"

# # Update

# # dict1[0] = "sabaz"

# # Delete
# del dict1[0]
# print(dict1)


# ///////////////////////////////////// combing operation ////////////

# //// list1
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# list3 = list1.copy()

# print(list3)

# //////////////////////////////////// tuple
# tuple1 = ("apple", "mango", "orange")
# tuple2 = (1, 2, 3, 4)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# //////////////////////////////////// set

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# # set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)

# //////////////////////////////////// dict

# dict1 = {1: "apple", 2: "mango"}
# dict2 = {4: "A", 5: "B"}
# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)


# ///////////////////////////////////////////////// list
# list1 = ["apple", "mango", "orange", "grapes", "papaya"]

# for x in range(len(list1)):
#     print(list1[x])


# /////////////////////////////////// list comprehension

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = [x for x in list1 if x % 2 == 0]
# print(even)


# /////////////////////////////// args kwargs

# def add(key1, *kids):
#     print(key1)
#     print(kids)


# list = ["apple", "mango", "orange", "grapes"]
# add("apple", "mango", "Papaya")

# /////////////////////////////// kwargs


# def getValue(**kids):
#     print(kids["alam"])


# getValue(alam="sabaz", pp="kk")


# /////////////////////////////// OOp pillar
# 1) Encapsulation


# class Animal:
#     def __eat(self):
#         print("Animal Eats")

#     def animal_eat(self):
#         self.__eat()


# a1 = Animal()
# a1.animal_eat()

# 2) Abstraction


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass


class Hen(Animal):
    def move(self):
        print("Hen Move with 2 Legs")


class Dog(Animal):
    def move(self):
        print("Dog Move with 4 Legs")


d1 = Dog()
d1.move()
