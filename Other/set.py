# set1 = {"apple", "mange", "orange"}
# print(set1)

# ////////////////////////////////////////////////
set2 = {"apple", "mango", "orange", "apple"}
# print(set2) #  {'orange', 'mango', 'apple'}

# ////////////////////////////////////////////////////

# set3 = {"apple", "mango", "orange", True, 1}
# print(set3)  # {'apple', True, 'orange', 'mango'}

# ////////////////////////////////////////////////////
set4 = {"apple", "mango", "orange", 0, False}
# print(set4)  # {0, 'apple', 'mango', 'orange'}
# print(len(set4))  # 4
# print(type(set4))


# ////////////////////////////////////////////////////////

# thisset = set(("apple", "mango", "Orange"))
# print(type(thisset))

# ///////////////////////////// Loop ////////////////////////
set5 = {"apple", "mango", "orange", "graps", "kiwi"}

# for x in set5:
#     print(x)

# //////////////////////////// present //////////////////////

# if "orange1" in set5:
#     print("Yes It Is Present")

# else:
#     print("Not Present")

# ////////////////////////////// set add //////////////////////
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 10}
# set2.update(set1)
# print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ////////////////////////////////////////////////////////////

# set1 = {1, 2, 3, 4, 5}
# set2 = (6, 7, 8, 9, 10, 10)
# set1.update(set2)
# print(set1)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# //////////////////////////// Remove ///////////////////////

# set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# # set.discard(11)
# set.clear()
# # set.add(12)
# # print(set)
# del set
# print(set)

# //////////////////////////// set join ////////////////////////
# set1 = {1, 2, 3, 4, 5}
# set2 = {16, 7, 8, 9}
# # set3 = set1.union(set2) # {1, 2, 3, 4, 5, 7, 8, 9, 16}
# set3 = set1 | set2
# print(set3)  # {1, 2, 3, 4, 5, 7, 8, 9, 16}

# ///////////////////////////// Multiple join /////////////////
# set1 = {1, 3}
# set2 = {5, 6}
# set3 = {8, 9}
# set4 = set1 | set2 | set3
# print(set4)

# /////////////////////////// join set and touple //////////////

# set1 = {1, 2, 3, 4, 5}
# set2 = (4, 5, 6)
# set3 = set1.union(set2)
# print(set3)

# ///////////////////////////// Difference //////////////////////
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)
