# def anagram(num1, num2):
#     dict1 = {}
#     while num1 != 0:
#         last = num1 % 10
#         if last in dict1:
#             dict1[last] = dict1.get(last) + 1
#         else:
#             dict1[last] = 1
#         num1 = num1 // 10

#     while num2 != 0:
#         last = num2 % 10
#         if last in dict1:
#             dict1[last] = dict1.get(last) - 1

#             if dict1.get(last) == 0:
#                 del dict1[last]
#         else:
#             return False
#         num2 = num2 // 10

#     if len(dict1) == 0:
#         return True
#     else:
#         return False
#     print(dict1)


# x = anagram(123, 345)
# print(x)


# //////////////////////////////////////// 2 ////////////////////////////////////////////////

# def palindrom(str):
#     n = len(str)

#     low = 0
#     high = n - 1

#     while low < high:
#         ch1 = str[low]
#         ch2 = str[high]

#         if ch1 != ch2:
#             return False

#         low += 1
#         high -= 1

#     return True


# x = palindrom("sabaz")
# print(x)


# //////////////////////////////////////////////// 3 //////////////////////////////////////


# def evev1(list):
#     even = [x for x in list if x % 2 != 0]
#     return even


# x = evev1([1, 2, 3, 4, 5, 6])
# print(x)


# /////////////////////////////////////////////// 4 //////////////////////////////////////


# def wordfreq(list):
#     dict1 = {}

#     for x in list:
#         if x in dict1:
#             dict1[x] = dict1.get(x) + 1
#         else:
#             dict1[x] = 1

#     return dict1


# x = wordfreq(["apple", "banana", "apple"])
# print(x)


# /////////////////////////////////////////// 5 //////////////////////

# import math

# def maxValue(list):
#     max = -math.inf

#     for x in list:
#         if max < x:
#             max = x

#     return max


# x = maxValue([1, 2, 3, 4, 5, 6])
# print(x)


# /////////////////////////////////////// 6 ///////////////////////////

# def commonElem(list1, list2):
#     list3 = []
#     set1 = set()

#     for x in list1:
#         set1.add(x)

#     for x in list2:
#         if x in set1:
#             list3.append(x)
#             print(x)

#     return list3


# x = commonElem([1, 2, 3, 4], [3, 4, 5, 6])
# print(x)


# ///////////////////////////////////////// 7 //////////////////////////


# def removeDub(list1):
#     list2 = []

#     for x in list1:
#         if x not in list2:
#             list2.append(x)

#     return list2


# x = removeDub([1, 1, 2, 2, 3, 3, 3, 4, 5])
# print(x)


# //////////////////////////////////////  8 ////////////////////////
# def sortDict(dict1):
#     for x in dict1:
#         print(x, dict1[x])


# sortDict({"a": 3, "b": 1, "c": 2})


# /////////////////////////////////////// 9 ////////////////////////

# def mergeDict(dict1, dict2):
#     dict3 = {}
#     dict3 = dict1.copy()
#     dict3.update(dict2)
#     print(dict3)

# mergeDict({"a": 1, "b": 2}, {"d": 3, "e": 5})


# ///////////////////////////////////// 10 /////////////////////////
# def sumOdDigit(num1):
#     sum = 0

#     while num1 != 0:
#         last = num1 % 10
#         sum += last
#         num1 = num1 // 10

#     print(sum)


# sumOdDigit(123)


# ///////////////////////////////// 11 ///////////////////////////

# def findMiddle(list):
#     list1 = []
#     n = len(list)
#     mid = int(n / 2)

#     list1.append(list[mid - 1])
#     list1.append(list[mid])
#     list1.append(list[mid + 1])

#     return list1


# x = findMiddle([1, 2, 3, 4, 5, 6, 7])
# print(x)


# //////////////////////////////////  15 /////////////////////////////
# swap key and value in dict


# def swapKeyValue(dict1):
#     swapDict = {}
#     for x in dict1:
#         # print(x, dict1[x])
#         swapDict[dict1[x]] = x
#     dict1 = swapDict
#     print(dict1)


# swapKeyValue({"a": 1, "b": 2})


# ///////////////////////////////////////////// 14 ///////////////////////////
# tuple

# def bigGram(str):
#     list = []
#     word = str.split(" ")
#     for x in range(len(word) - 1):
#         list.append((word[x], word[x + 1]))

#     print(list)


# bigGram("I Love NLP")


# ///////////////////////////////////////////  17 //////////////////////////////

# def highestScore(tuple):
#     list1 = []
#     min = -1
#     for name, num in tuple:
#         if min < num:
#             min = num

#     for name, num in tuple:
#         if num == min:
#             list1.append(name)

#     return list1


# x = highestScore([("Alice", 88), ("Charlie", 91), ("Bob", 91)])
# print(x)


# ///////////////////////////////////////   bank Account ////////////////////////


# class Bankaccount:

#     def __init__(self):
#         self.balance = 0

#     def Deposite(self, amount):
#         self.balance += amount
#         print(f"Deposite Balance: {self.balance}")

#     def WithDraw(self, amount):
#         self.balance -= amount
#         print(f"WithDraw Balance: {self.balance}")

#     def getBalance(self):
#         print(f"Get Balance: {self.balance}")


# b1 = Bankaccount()
# b1.Deposite(10)
# b1.Deposite(5)
# b1.WithDraw(5)
# b1.getBalance()


# ///////////////////////////////////// Sort Dictionary /////////////////////////

def DictSort(dict1):
    return dict(sorted(dict1.items(), key=lambda x: x[1]))


dict1 = {"a": 3, "b": 1, "c": 2}
x = DictSort(dict1)
print(x)


# //////////////////////////////////// Find Diff Character ////////////////////////
# def diffChar(str1, str2):
#     for x in range(len(str1)):
#         if str1[x] != str2[x]:
#             print(str1[x], end=" ")


# diffChar("hello", "hallo")


# //////////////////////////////////// Extract number /////////////////////////////
# def extractNum(num1, num2):
#     print(num1 + num2)


# extractNum(5, 5)

# /////////////////////////////////////// sum of number /////////////////////////

# import re

text = "The Bill is 20 and the tip is 20"
number = re.findall(r"\d+", text)
print(number)
number = [int(num) for num in number]
total_Sum = sum(number)
print(total_Sum)


# ///////////////////////////////////// Dublicate number /////////////////////
# def findDublicate(list):
#     for x in range(len(list) - 1):
#         if list[x] == list[x + 1]:
#             return list[x]


# list = [1, 2, 3, 4, 4]
# x = findDublicate(list)
# print(f"Dublicate Element: {x}")


# /////////////////////////////////////// Merge Sorted Array ////////////////////


# def SortedList(list1, list2):
#     list3 = []
#     n = len(list1)
#     m = len(list2)

#     low1 = 0
#     low2 = 0

#     while low1 < n and low2 < m:
#         if list1[low1] == list2[low2]:
#             list3.append(list1[low1])
#             list3.append(list2[low2])
#             low1 += 1
#             low2 += 1
#         elif list1[low1] < list2[low2]:
#             list3.append(list1[low1])
#             low1 += 1
#         else:
#             list3.append(list2[low2])
#             low2 += 1

#     while low1 < n:
#         list3.append(list1[low1])
#         low1 += 1

#     while low2 < m:
#         list3.append(list2[low2])
#         low2 += 1

#     print(list3)


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]

# SortedList(list1, list2)


# ///////////////////////////////////////////////// continious sum ///////////////////
# import math


# def continious_Sum(list1):
#     max_sum = -math.inf
#     current_sum = 0

#     for x in list1:
#         current_sum += x
#         max_sum = max(current_sum, max_sum)
#         if current_sum < 0:
#             current_sum = 0
#     return max_sum


# x = continious_Sum([-1, -2, -3])
# print(x)


# ///////////////////////////////////////////////// without repeating element ////////////////////


# def longestSub(str):
#     dict1 = {}
#     maxLen = 0
#     n = len(str)
#     low = 0

#     for x in range(len(str)):
#         ch1 = str[x]

#         if ch1 in dict1:
#             dict1[ch1] = dict1.get(ch1) + 1
#         else:
#             dict1[ch1] = 1

#         if dict1[ch1] > 1:
#             while dict1[ch1] > 1:
#                 ch2 = str[low]
#                 dict1[ch2] = dict1.get(ch2) - 1
#                 if dict1.get(ch2) == 0:
#                     del dict1[ch2]
#                 low += 1

#         if (x - low) + 1 == len(dict1):
#             maxLen = max(maxLen, (x - low) + 1)
#     return maxLen


# x = longestSub("abcabcbb")
# print(x)


# /////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////////////////////////////

# import copy


# def mergeDict(dict1, dict2):
#     dict3 = {}
#     dict3 = dict1.copy()
#     dict3.update(dict2)
#     print(dict3)


# mergeDict({"a": 1, "b": 2}, {"c": 3, "d": 4})


# //////////////////////////// class


# class BankAccount:
#     def __init__(self, Balance=0):
#         self.Balance = Balance

#     def Deposite(self, Amount):
#         self.Balance += Amount
#         print(f"Balance: {self.Balance}")


# b1 = BankAccount()
# b1.Deposite(10)
# b1.Deposite(20)


# /////////////////////////// pp


# def mergeDiccc(list1):
#     list3 = []
#     list2 = []
#     list2 = list1.split(" ")
#     for x in range(len(list2) - 1):
#         list3.append((list2[x], list2[x + 1]))

#     print(list3)


# mergeDiccc("I Love Nlp")

# //////////////////////////////  swap key value


def mergeDict(dict1):
    dict3 = {}

    for x in dict1:
        dict3[dict1[x]] = x

    print(dict3)


mergeDict({"a": 1, "b": 2})
