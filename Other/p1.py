# Reverse a list
# list = [1, 2, 3, 4, 5, 6]
# n = len(list)
# mid = n / 2

# i = 0
# j = n - 1


# while i < mid:
#     a = list[i]
#     b = list[j]

#     list[i] = b
#     list[j] = a
#     i += 1
#     j -= 1

# print(list)


# ////////////// Max Min in a list

# list = [1, 2, 3, 4, 5, 6, 7, 8]
# max = -1
# min = 11

# for x in list:
#     if x > max:
#         max = x
#     if x < min:
#         min = x

# //////////////////
# print(f"Max: {max}  Min: {min}")

# min_val = float("inf")
# max_val = float("-inf")

# nums = [3, 7, -2, 9, 0]

# for num in nums:
#     if num < min_val:
#         min_val = num
#     if num > max_val:
#         max_val = num

# print("Min:", min_val)
# print("Max:", max_val)


# //////////////////////////////////// remove dublicate

# list = [5, 4, 4, 1, 1, 2, 2, 3]
# list.sort()
# ele = list[0]

# for x in range(len(list)):
#     if list[x] != ele:
#         print(ele, end=" ")
#         ele = list[x]

# print(ele)

# ////////////////////////////////// sum of element of list

# list = [1, 2, 3, 4, 5]
# sum = 0
# for x in list:
#     sum += x


# print(sum)

# ////////////////////////// list comprehension //////////////
list = [1, 2, 3, 4]
# newList = [x * x for x in list]
# print(newList)

# // even

# even = [x for x in list if x % 2 == 0]
# print(even)


items = ["apple", "mango", "orange"]
# newlist = []  5 5 6
# for x in items:
#     newlist.append(len(x))

# print(newlist)

# /////////////////////////////////////////////////////

# newlist = [len(word) for word in items]
# print(newlist)


# //////////////////// reverse a String
# str = "hello"
# newStr = ""

# n = len(str)
# n = n - 1

# while n != -1:
#     newStr += str[n]
#     n -= 1

# print(newStr)


# ///////////////////// check palinmdrom


# def IsPalindrom(str):
#     isPal = 0
#     n = len(str)
#     mid = n / 2
#     n = n - 1
#     i = 0

#     while i < mid:
#         if str[i] != str[n]:
#             print("Not Palindrom")
#             isPal = 1
#             break
#         i += 1
#         n -= 1
#     if isPal == 0:
#         print("Yes Palindrom")


# IsPalindrom("moma")


# /////////////////////////// count char freq

# str = "Hello Sabaz Alam"


# def charFrq(str):
#     seen = {}
#     for x in str:
#         if "a" <= x <= "z":
#             if x not in seen:
#                 seen[x] = 1
#             else:
#                 seen[x] = seen.get(x) + 1
#     print(seen)


# charFrq(str)


# ///////////////////////// check Anagram
# def checkAnagram(str1, str2):
#     n = len(str1)
#     m = len(str2)

#     if n != m:
#         return False

#     # dictionary
#     seen = {}
#     for x in str1:
#         if x not in seen:
#             seen[x] = 1
#         else:
#             seen[x] = seen.get(x) + 1

#     for x in str2:
#         if x in seen:
#             seen[x] = seen.get(x) - 1
#             if seen.get(x) == 0:
#                 del seen[x]
#         else:
#             seen[x] = 1

#     if len(seen) == 0:
#         return True
#     else:
#         return False


# str1 = "hello"
# str2 = "olleho"

# ans = checkAnagram(str1, str2)
# print(ans)


# //////////////////// Capatalized first character of Every Word in Sentence

# str = "hello my name is sabaz alam"

# def Capatalized(str):
#     for x in range(len(str)):
#         # // if i==0 is small character
#         if x == 0 and ord(str[x]) >= 97:
#             num = ord(str[x])
#             num -= 32
#             print(chr(num), end="")
#         elif str[x - 1] == " " and ord(str[x]) >= 97:
#             num = ord(str[x])
#             num -= 32
#             print(chr(num), end="")
#         else:
#             print(str[x], end="")


# Capatalized(str)

# ///////////////////// merge two dictionary //////////////////////
# dict1 = {1: "apple", 2: "mango", 3: "orange"}
# dict2 = {4: "grapes", 2: "Sabaz", 6: "Kiwi"}

# dict3 = {**dict1, **dict2}
# print(dict3)


# dict3 = dict1.update(dict2)
# print(dict3)

# for x in dict2:
#     # print(x, dict2[x])
#     dict1[x] = dict2[x]

# print(dict1)


# ///////////////////////// operation on dictionary

dict1 = {}

# add in dictionary
dict1[1] = "apple"
dict1[2] = "Orange"
dict1[3] = "Mango"
dict1[4] = "Grapes"

# print(dict1)

# ////////////////////// traversing in dict1
# for x in dict1:
#     print(x, dict1[x])

# /////////////////////// updating key value pairs
dict1[4] = "Sabaz Alam"

# print(dict1)


# ////////////////////// iterate in dict1

# for key in dict1.keys():
#     print(key)


# for value in dict1.values():
#     print(value)

# for key, value in dict1.items():
#     print(key, value)


# /////////////////////// control flow and logic ////////////////////////

# //// check even or odd


# def checkNum(num):
#     if num % 2 == 0:
#         print(f"{num} Is Even Number")
#     else:
#         print(f"{num} Is Odd Number")


# checkNum(21)

# //// factorial using iteration


# def factorial(num):
#     # for x in range(num, 1):
#     #     print(x)
#     res = 1
#     while num != 0:
#         res *= num
#         num -= 1
#     print(res)


# factorial(5)


# //// factorial using recursion
# def factorial(num):
#     if num == 1:
#         return num

#     return num * factorial(num - 1)


# print(factorial(5))


# ///// fibonacchi number


# def fibonacchi(num):
#     if num == 1:
#         print(1)
#     elif num == 2:
#         print(0, 1)
#     else:
#         print(0, end=" ")
#         print(1, end=" ")
#         num -= 2
#         a = 0
#         b = 1

#         while num > 0:
#             c = a + b
#             print(c, end=" ")
#             a = b
#             b = c
#             num -= 1

# fibonacchi(5)

# //////// check prime


# def isPrime(num):
#     x = int(num**0.5)
#     i = 2
#     isprime = 1
#     while i <= x:
#         if num % i == 0:
#             print(f"{num} Not Prime")
#             isprime = 0
#             break
#         i += 1
#     if isprime == 1:
#         print(f"{num} is Prime")


# isPrime(6)


# ///////////////////// function
def sum(num):
    sum = 0
    i = 1

    while i <= num:
        sum += i
        i += 1
    return sum


print(sum(5))
