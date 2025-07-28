# ///////////////////////   reverse a list ///////////////////////////

# list1 = [1, 2, 3, 4, 5]

# n = len(list1)
# mid = n / 2
# i = 0
# n = n - 1

# while i < mid:
#     a = list1[i]
#     b = list1[n]

#     list1[i] = b
#     list1[n] = a
#     i += 1
#     n -= 1


# print(list1)


# /////////////////////// Max Min in List1 ///////////////////////////

# list1 = [1, 2, 3, 4, 5]
# max = -1
# min = 99

# for x in list1:
#     if max < x:
#         max = x

#     if min > x:
#         min = x

# print("Max: ", max, "MIN: ", min)


# /////////////////////// Remove Duplicate from List1 ///////////////////////////

# set1 = set()

# list1 = [1, 1, 2, 2, 3, 4]
# newList = []

# for x in list1:
#     if x not in set1:
#         print("HHH")
#         set1.add(x)
#         newList.append(x)

# print(newList)


# /////////////////////// Sum of Element of  List1 ///////////////////////////

# list1 = [1, 1, 2, 3, 4, 5]
# sum = 0

# for x in list1:
#     sum += x

# print(sum)


# /////////////////////// list Comprehension ///////////////////////////

# list1 = [1, 2, 3, 4, 5]

# even = [x for x in list1 if x % 2 == 0]
# print(even)


# //////////////////////// Reverse a list ////////////////////////////////
# str = "hello"
# # res = ""

# # for x in str:
# #     res = x + res

# # print("Result: ", res)

# ans = str[::-1]
# print("Result: ", ans)


# //////////////////////// Check Palindrom ////////////////////////////////


# def checkPalind(str):
#     i = 0
#     j = len(str)
#     mid = j / 2
#     j = j - 1

#     while i < mid:
#         a = str[i]
#         b = str[j]

#         if a != b:
#             return False

#         i += 1
#         j -= 1

#     return True


# Str = "abbaa"

# res = checkPalind(Str)
# if res == True:
#     print("Yes Palindrom")
# else:
#     print("Not Palindrom")


# ///////////////////////////////////////////////////////
# list1 = ["apple", "mango", "grapes", "ppp"]

# count = 0
# for x in list1:
#     if "a" in x:
#         count += 1

# print(count)

# ///////////////////////////////////// Anagram Check /////////////////////////
# str = "zzabA"
# res = sorted(str)
# print(res)

# ///////////////////////////////////// Merge TWO dictionary /////////////////////
dict1 = {1: "apple", 2: "mango", 3: "Orange"}
dict2 = {5: "Car", 6: "Bike", 7: "PP"}
dict1.update(dict2)


# for x in dict1:
#     print(x, dict1[x])

# print(dict1.get(10))


# for x in dict1.keys():
#     print(x)

# for x in dict1.values():
#     print(x)

# for key, value in dict1.items():
#     print(key, value)


# //////////////////////////////////////////////////////
# def isEvenOdd(num):
#     if num % 2 == 0:
#         print(f"Number: {num} is Even")
#     else:
#         print(f"Number: {num} is Odd")


# isEvenOdd(5)
# isEvenOdd(4)


# /////////////////////////////////////////// Factorial  iteration ////////////////

# def factorial1(num):
#     x = 1
#     for i in range(1, num + 1):
#         x = x * i

#     print(x)


# factorial1(5)


# /////////////////////////////////////////// Factorial  Recursion ////////////////
# def factorial(num):
#     if num == 1:
#         return 1

#     return num * factorial(num - 1)


# print(factorial(5))

# ////////////////////////////////////////// Fibnocchi Sequence /////////////////////


# def fibnocchi(num):
#     a = 0
#     b = 1
#     while num != 0:
#         c = a + b
#         print(c)
#         a = b
#         b = c
#         num -= 1


# print(0)
# print(1)
# fibnocchi(3)

# //////////////////////////////////// Prime Number /////////////////////////////


# def IsPrime(num):
#     count = 0
#     for x in range(2, num):
#         if num % x == 0:
#             count += 1

#     if count > 0:
#         print("Not Prime")
#     else:
#         print("prime")


# IsPrime(6)

# 2) Other Way
