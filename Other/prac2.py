# list = []
# list.append(5)
# list.append(6)
# list.append(7)
# print(list)

# # //////////////////////// Update /////////////////
# list[0] = 10
# print(list)

# //////////////////////////// Remove ///////////////
# list.remove(10)  # [6,7]
# print(list)


# ////////////
# list.remove(7)
# list.pop()
# print(list)
# //////////////////////////////// loop////////////////
# for i in range(len(list)):
#     print(list[i])


# /////////
# ////////////////////////////// Tuple /////////////////////////

# tuple1 = ()

# tuple1 = tuple1 + (1,)
# tuple1 = tuple1 + (2,)
# tuple1 = tuple1 + (3,)
# tuple1 = tuple1 + (3,)

# print(tuple1)

# //////////////// Update ///////////////////
# # tuple1[0] = 10
# print(tuple1)
# newList = list(tuple1)
# newList[0] = 10
# newList.remove(3)
# # print(newList)
# tuple1 = tuple(newList)
# print(tuple1)


# //////////////// Set /////////////////////
# thisset = set()
# thisset.add(1)
# thisset.add(5)
# thisset.add(5)
# # set1.append(1)

# print(thisset)


# /////////////////////////// list ///////////////
# list1 = [1, 2, 3, 4]
# list2 = [6, 7, 8]

# # list1.extend(list2)
# list3 = list1.copy()
# list3[0] = 11
# print(list3)
# print(list1)


# ////////////////////////// tuple ////////////////////////
# list1 = (1, 2, 2, 2, 2, 3, 4)
# list2 = (5, 6, 7, 8)

# list3 = list1 + list2
# # print()

# ss = list1.index(2)
# print(ss)


# /////////////////////////  set /////////////////////////

# set1 = set()
# set1.add(3)

# set1.add(10)
# set1.add(15)

# set2 = set()
# set2.add(11)
# set2.add(22)

# for i in range(len(set2)):
#     set1.add(set1[i])
#     print(set1[i])

# /////////////////////////////// unpacking a Tuple ////////////////////

# fruits = (1, 2, 3, 4)
# apple, mango, orange, grapes = fruits

# print(apple)

# /////////////////////////////// deleting the tuple /////////////////////
# del fruits
# print(fruits)

# /////////////////////////////////////////////////////////////////
# fruits = {1, 2, 3, 4}
# fruits.clear()
# print(fruits)

# //////////////////////////////////////////////////////////////////

# dict = {"firstName": "Sabaz", "lastName": "Alam", "Home": "Assam"}
# dict.clear()
# print(dict)

# //////////////////////// Dictionary ////////////////////////////

# dictionary = {1: "Sabaz", 2: "alam", 3: "Gopal", 5: "AAA"}
# # print(dictionary[4])  # error Key
# # print(dictionary.get(5, "Not Found"))

# # Add element in dictionary
# dictionary[10] = "Rahul"

# # Update
# dictionary[1] = "Hello World"

# # delete
# dictionary.pop(101)
# print(dictionary)


# ///////////////////////////////////////////////////

# list1 = [1, 2, 3, 4]
# list2 = ["a", "b", "c", "d"]

# dict1 = dict(zip(list1, list2))
# print(dict1)

# prog = {
#     "js": "Atom",
#     "cs": "VS",
#     "Python": ["pycharm", "subline"],
#     "Java": {"JSE": "Netbeans", "JEE": "Eclips"},
# }

# print(prog["Java"]["JEE"])
# # print(prog.get("js"))

# ////////////////////////////////////////////////////////////////////

# thisset = {"apple", "mango", "Orange", "Grapes"}
# set1 = {"1", "2"}

# print(thisset)
# thisset.update(set1)
# print(thisset)
# # thisset.discard("pp1")
# thisset.pop()

# del thisset
# print(thisset)

# /////////////////////////////////////

# list1 = [1, 2, 3]
# del list1
# print(list1)

# ////////////////////////////////////

# tuple1 = (1, 2, 34)
# del tuple
# print(tuple1)

# //////////////////////////////////////

# dict1 = {1: "a", 2: "b", 3: "c"}
# del dict1
# print(dict1)

# //////////////////////////////////////////

# set1 = {1, 2, 3, 4}
# print(set1)
# set1 = set()
# print(set1)

# /////////////////////// set join  Method /////////////////////

# set1 = {1, 2, 3, 4, 6}
# set2 = {6, 7, 8, 9}

# set1.update(set2)
# print(set1)
# set1.union(set2)
# print(set1)

# ////////////////////////////// update and intersection ///////////

set1 = {1, 2, 3, 4, 6}
set2 = {6, 7, 8, 9}

# set3 = set1.intersection(set2)  # {6}
# print(set3)

set3 = set1.difference(set2)  # {1, 2, 3, 4}
print(set3)
