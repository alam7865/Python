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


# ///////////////////////////////////////////////////////// Lambda Function ////////////////////////////////

# x = lambda x: x + 5

# print(x(5))


# x = lambda x, y: x + y

# print(x(5, 5))


# ////////////////////////////////////////////////////////////////////

# dict1 = {1: "apple"}
# # print(dict1.get(1))

# # /////////// Add

# dict1[2] = "Mango"
# dict1[4] = "Orange"

# print(dict1.get(1))
# print(dict1[10])

# # /////////////// get

# print(dict1[2])

# # ////////////// update
# dict1[1] = "Sabaz"

# # //////////// delete
# del dict1[1]
# print(dict1)


# //////////////////////// Dictionary with mixed ////////////
# dict1 = {
#     1: "apple",
#     2: "Mango",
#     "place": ("Assam", "Bihar", "Hydrabad"),
#     "even": [2, 4, 6, 8],
#     "job": {1: "It", 2: "Doctor", 3: "Teacher"},
#     "country": ["India", "America", "Nepal", "Bangladesh"],
# }


# print(dict1["place"][1])  # Bihar
# print(dict1["even"][0])  # 2
# print(dict1["job"][2])  # Doctor
# print(dict1["country"][0])  # India


# set1 = {"apple", "mango", "Orange"}
# print(set1.get(0))


# //////////////////////////////////////////////////////////

# set1 = {1, 2, 3, 4, 5, 6}
# set1.remove(6)
# print(set1)


# ///////////////////////////////////////////////////////////


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def showDetails(self):
#         print("Name: ", self.name, " ", self.marks)

#     def showAgv(self):
#         sum = 0
#         for x in self.marks:
#             sum += x

#         print("Average: ", sum / 3)


# s1 = Student("Sabaz Alam", [55, 66, 77])
# s1.showDetails()
# s1.showAgv()


# /////////////////////////////////////////


def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


div = smart_div(div)

div(4, 2)
