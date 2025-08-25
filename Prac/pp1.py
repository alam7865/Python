# import random

# print(random.randrange(1, 2))


# //////////////////////////////////////////////////////////////////////

# str = "sabbaj"
# str1 = str[::-1]
# print(str1)


# //////////////////////////////////////////////////////////////////////

# tuple1 = ()
# print(type(tuple1))


# //////////////////////////////////////////////////////////////////////
# set1 = set()
# set1.add(1)
# set1.remove(1)
# print(set1)


# //////////////////////////////// list comprehension ////////////////////

# list1 = [1, 2, 3, 4, 5]
# even = [x + 1 for x in list1]
# print(even)


# //////////////////////////////// sort function /////////////////////////
# list1 = [5, 4, 7, 8]-
# list1.sort()            # [4, 5, 7, 8]
# list1.sort(reverse=True)
# print(list1)

# //////////////////////////////// list operation //////////////////////////

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]

# list3 = list1.copy()
# list3.extend(list2)
# print(list3)

# //////////////////////////////// copy ////////////////////////////////////////////

# import copy

# original = [[1, 2, 3], [4, 5, 6]]
# shallowCopy = copy.copy(original)
# deepCopy = copy.deepcopy(original)

# original[0][0] = 100
# print(shallowCopy)
# print(deepCopy)


# /////////////////////////////// args ,kwargs /////////////////////////////////////////

# def func(**kid):
#     print(kid)
#     print(kid["lname"])


# func(fname="Sabaz", lname="Alam")

# //////////////////////////////// lambda ///////////////////////////////////////
x = lambda x: x + 5
print(x(5))
