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


# from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass


# class Hen(Animal):
#     def move(self):
#         print("Hen Move with 2 Legs")


# class Dog(Animal):
#     def move(self):
#         print("Dog Move with 4 Legs")


# d1 = Dog()
# d1.move()


# ////////////////////////////////////// map
# list1 = [1, 2, 3, 4, 5]
# newList = list(map(lambda x: x + 1, list1))
# print(newList)

# ////////////////////////////////////// filter
# list1 = [1, 2, 3, 4, 5]

# newlist = list(filter(lambda x: x > 3, list1))
# print(newlist)

# ////////////////////////////////////// reduce

# from functools import reduce
# list1 = [1, 2, 3, 4, 5]
# newList = reduce(lambda x, y: x + y, list1)
# print(newList)

# ///
# ///////////////////////////////////// enumerator

# list = ["apple", "mango", "orange", "grapes"]

# newList = [(index, item) for index, item in enumerate(list)]
# print(newList)

# for index, item in enumerate(list, start=1):
#     print(index, item)


# ////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////// Reverse a list

# list = [1, 2, 3, 4]


# def reverse(list1):
#     n = len(list1)
#     n -= 1

#     i = 0

#     while i < n:
#         num1 = list[i]
#         num2 = list[n]
#         list1[i] = num2
#         list1[n] = num1
#         i += 1
#         n -= 1
#     return list1


# print(reverse(list))

# /////////////////////////////////////// Max Min in list ////////////////

# import math

# list1 = [1, 2, 3, 4, 5, 6]

# max1 = -math.inf
# min1 = math.inf

# for x in list1:
#     max1 = max(max1, x)
#     min1 = min(min1, x)

# print(f"MAX: {max1}   Min: {min1}")


# ////////////////////////////////////// remove Dublicate /////////////////

# list1 = [1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5]

# set1 = set()
# newList = []

# for x in list:
#     if x not in set1:
#         newList.append(x)
#         set1.add(x)

# print(newList)

# i = 0
# # newList.append(list[0])
# for x in range(len(list1)):
#     if list1[x] != list1[i]:
#         newList.append(list1[i])
#         i = x

# newList.append(list1[i])

# print(newList)


# ///////////////////////////////////////// square of list
# list1 = [2, 4, 5, 10]


# def square1(list1):
#     newList = [x * x for x in list1]
#     return newList

# print(square1(list1))


# //////////////////////
# def even(list1):
#     newList = [x for x in list1 if x % 2 == 0]
#     print(newList)


# even(list1)

# ////////////////////////////////

# list1 = ["apple", "mango", "orange", "PP"]


# def wordLen(list1):
#     newList = [len(x) for x in list1]
#     print(newList)

# wordLen(list1)

# ///////////////////////    Merge two List

# a = [1, 2, 2, 3]
# b = [4, 5, 5, 6]

# newList = []
# i = 0
# j = 0

# while i < len(a) and j < len(b):
#     if a[i] == b[j]:
#         newList.append(a[i])
#         newList.append(b[j])
#         i += 1
#         j += 1
#     elif a[i] < b[j]:
#         newList.append(a[i])
#         i += 1
#     else:
#         newList.append(b[j])
#         j += 1

# while i < len(a):
#     newList.append(a[i])
#     i += 1

# while j < len(b):
#     newList.append(b[j])
#     j += 1

# print(newList)


# //////////////////////////// Reverse a String
# str = "sabaz"
# str2 = ""

# n = len(str)

# while n != 0:
#     str2 += str[n - 1]
#     n -= 1

# print(str2)

# /////////////////////////// store Frequency

# str = "sabaz alam"
# dict = {}

# for x in range(len(str)):
#     if str[x] in dict:
#         dict[str[x]] = dict.get(str[x]) + 1
#     else:
#         dict[str[x]] = 1


# for x in dict:
#     print(x, dict[x])


# ////////////////////////// Dictionary
# str = "aab"
# dict1 = {"a": 2, "b": 1}

# dict1["b"] = dict1.get("b") - 1
# del dict1["b"]
# print(dict1)


# ////////////////////////// Capatalized
import math

str = "hello sabaz 787787 alam"
# print(str.title())

for x in range(len(str)):
    num = ord(str[x])
    if x == 0:
        if num >= 97:
            num -= 32
            print(chr(num), end="")
    elif str[x - 1] == " " and "a" <= str[x] <= "z":
        print(chr(num - 32), end="")
    else:
        print(str[x], end="")
