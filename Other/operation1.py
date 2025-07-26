# try:
#     num1 = int(input("Enter the Number1\n"))
#     num2 = int(input("Enter the Number2\n"))
#     print("Sum: ", num1 + num2)

# except:
#     print("Something Went Wrong")


# ////////////////////////////////////////////////////////////////

# import time

# localTime = time.asctime(time.localtime(time.time()))
# print(localTime)

# ///////////////////////////////////////////////////////////////

# list = ["apple", "mango", "orange", "grapes"]
# for index, list in enumerate(list, start=1):
#     print(index, list)


# list = [1, 2, 3, 4, 5, 6]

# for i in range(len(list)):
#     print(list[i] * list[i])


# /////////////////////////// Map //////////////////////
# def square1(x):
#     # print(x * x)
#     return x * x


# lst = [1, 2, 3, 4, 5, 6]
# # square = map(square1, lst)
# square = map(lambda x: x * x, lst)
# print(list(square))


# /////////////////////////// Filter ////////////////////////
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# myList = filter(lambda x: x % 2 == 0, list1)
# print(list(myList))

# /////
# def even(x):
#     if x % 2 == 0:
#         return x


# myList = filter(even, list1)
# print(list(myList))


# //////////////////////////// Reduce /////////////////////

from functools import reduce

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# sum = 0

# for i in list1:
#     sum += i

# print(sum)

sum = reduce(lambda x, y: x + y, list1)
print(sum)
