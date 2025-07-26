# list1 = ["apple", "mango", "banana", "grapes", "Orange"]

# # for x in list1:
# #     print(x)

# a = " @ ".join(list1)

# print(a)

# //////////////////////////////////////////////////////////////

# list1 = list(("apple", "mango"))
# print(list1)

# a = None
# print(a)


# ///////////////////////////////////////////////////////////////

# try:
#     num1 = int(input("Enter Number 1\n"))
#     num2 = int(input("Enter Number 2\n"))

#     print("Sum: ", num1 + num2)
# except:
#     print("SomeThing Went Wrong")


# a = "sabaz"

# b = "123"

# a = a + b
# a.replace("s", "A")
# print(a)


#

# ///////////////////////////////////////////////////////////////////

# num = 55
# print(f"The String is: {num:.2f}")

# num = [1, 2, 3, 4]
# num.remove(4)
# print(num)


# ////////////////////////// List Comprehension //////////////////////
list1 = ["apple", "mango", "orange", "grapes", "papaya", "pppp"]

# newList = []

# for x in list1:
#     if "pp" in x:
#         newList.append(x)

# print(newList)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = [x for x in num if x % 2 == 0]
# print(even)


# //////////////////////////////////////////////////////////

# import copy

# nested = [[1, 2], [3, 4]]

# shallow = copy.copy(nested)
# deep = copy.deepcopy(nested)

# deep[0][0] = 101

# print(shallow)
# print(deep)
