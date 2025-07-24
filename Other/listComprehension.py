# list = [1, 2, 3, 4, 5, 6, 7, 8]
# even = [x for x in list if x % 2 == 0]
# print(even) # [2,4,6,8]

# ///////////////////////////////////////////////////
# list = ["apple", "egg", "orange"]
# newList = [x for x in list if "a" in x]
# print(newList)

# ll = [x for x in list]
# print(ll)

# create a list with 1 to 10 number
# list = [x for x in range(10)]
# print(list)


# //////////////////////// List Sort //////////////////
# list1 = [5, 1, 2, 7, 3]
# # list2 = list(list1)
# list2 = list1.copy()
# print(list2)


# ///////////////////////// function ////////////////////
# def myfunc(a):
#     return a * 5


# res = myfunc(5)
# print(res)

# ////////////////////// function with 2 arguments////////////////


# def myfunc(a, *b):
#     # print(f"Hello {a} {b}")
#     print("Hello", b[1])


# myfunc("Sabaz", "Alam", "ALam1", "Alam2")

# /////////////////////// function with key=value ////////////////////


# def myfunc(arg1, arg2, arg3):
#     print(arg1)


# myfunc(arg3="Sohail", arg2="Sabaz", arg1="Kalam")


# ////////////////////////////
# def myfunc(**kids):
#     print(kids["fname"])


# myfunc(fname="Sabaz", lname="Alam", clas="Sohail")


# /////////////////////////// default parameter //////////////
# def myfunc(country="India"):
#     print(country)


# # myfunc("America")
# myfunc()


# ///////////////////////////// Lambda function /////////////////////
# a = lambda a: a * 5
# print(a(3))

# /////////////////////////////////////////////
# x = lambda a, b: a + b
# print(x(10, 10))

x = lambda a, b, c: a + b + c
print(x(5, 5, 5))
