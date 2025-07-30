# import qading

# print("HHHHHH")


# //////////////////////////////
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# /////////////////////  map

# newList = list(map(lambda x: x + 1, list1))
# print(newList)
# print(list1)

# ////////////////////// Filter
# newList = list(filter(lambda x: x > 5, list1))
# print(newList)

# ///////////////////// Reduce

# from functools import reduce

# newList = int(reduce(lambda x, y: x + y, list1))
# print(newList)


# ///////////////////// zip

# list1 = [1, 2, 3, 4]
# list2 = ["apple", "mango", "orange", "grapes"]

# list3 = list(zip(list1, list2))
# print(list3)

# ////////////////////// emumerator

# list1 = ["apple", "mango", "orange"]
# for index, list1 in enumerate(list1, 0):
#     print(index, list1)

# ///////////////////// Lambda
# x = lambda x: x + 5
# print(x(5))

# str = "sabaz"
# print(str[0:])

# list1 = [1, 2, 3, 4, 5]
# list1[0] = 100
# # newList = list1.copy()
# # print(newList)

# newList = list(list1)
# print(newList)


# //////////////////// lambda function //////////////
x = lambda x: x + 5
print(x(5))
