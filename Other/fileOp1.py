# with open("./Other/text1.txt", "r") as f:
#     print(f.read())


#  write operation

# with open("./Other/text2.txt", "w") as f:
#     f.write("MANGO kkkkkkkkkkkkkk")

# append new word

# with open("./Other/text2.txt", "a") as f:
#     f.write("\nMango,Orange,Grapes")

# dict = {}
# with open("./Other/text2.txt", "r") as f:
#     str = f.read()
#     for x in range(len(str)):
#         if str[x] != " ":
#             if str[x] not in dict:
#                 dict[str[x]] = 1
#             else:
#                 dict[str[x]] = dict.get(str[x]) + 1

# print(dict)


# str = "hjhjhj"
# for x in range(len(str)):
#     print(str[x])


# ////////////////////////// try except /////////////////

# try:
#     with open(".Other/text1.txt", "r") as f:
#         print(f.read())
# except:
#     print("Some Thing Went Wrong")


# ///////////////////////// Decerator ///////////////////
# def dev(num1, num2):
#     print(num1 / num2)


# def smartdev(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)

#     return inner


# dev = smartdev(dev)

# dev(2, 4)


# ///////////////////////// two sum ///////////////////////

# arr = [2, 7, 11, 15]
# target = 9


# def solve(arr, target):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] + arr[j] == target:
#                 return [i, j]

# print(solve(arr, target))

# ////////////////////////// Missing Number ////////////////


# def missing(list, n):
#     tsum = int(n * (n + 1) / 2)
#     listSum = 0
#     for x in list:
#         listSum += x

#     missingNum = tsum - listSum
#     return missingNum


# list1 = [1, 2, 3, 5]
# n = 5
# print(missing(list1, n))

# ///////////////////////// Kadance Algorithm ////////////////
# list = [2, 3, -8, 7, -1, 2, 3]  # 11  [7,-1,2,3]

# list = [-2, -4]  # 11  [7,-1,2,3]
# list = [5, 4, 1, 7, 8]  # 11  [7,-1,2,3]


# def solve(list):
#     currSum = 0
#     maxSum = float("-inf")
#     for x in list:
#         currSum += x
#         maxSum = max(maxSum, currSum)
#         if currSum < 0:
#             currSum = 0

#     return maxSum


# print(solve(list))

# /////////////////////////////////// HCF of Two Number
a = 4
b = 8


def findGcd(a, b):
    a1 = a
    b1 = b
    pro = a1 * b1
    while b != 0:
        num1 = a
        num2 = b
        a = num2
        b = int(num1 / num2)

    hcf = int((a1 * b1) / a)
    print(hcf)


findGcd(4, 8)
