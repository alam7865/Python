# with open("./Other/text1.txt", "r") as f:
#     print(f.read())


# ////////////////// write file //////////////////////////////

# with open("./Other/text1.txt", "w") as f:
#     # print(f.write("Sabaz"))
#     f.write("My Name is Alam")

# ///////////////// append file ////////////////////////////////
# with open("./Other/text1.txt", "a") as f:
#     f.write("\nGooglesssssssssssssssssssss")
#     f.close()


# with open("./Other/text3.txt", "x+") as f:
#     f.write("AAAAAAAAAAAAAAAAAAAAA")
#     f.seek(0)
#     print(f.read())


# ////////////////////////////////////////////////////////////////////
# arr = [0] * 5
# print(arr)      # [0, 0, 0, 0, 0]

# tuple = (0,) * 5
# print(tuple)

# dict1 = {}


# ////////////////////////////////// Args and kwargs ////////////////////////////////


# def func(*kid):
#     print(kid)


# func("apple", "Banana", "Orange", "Grapes", "Papaya")


def func(**kid):
    print(kid["lname"])


func(fname="Sabaz", lname="Alam", School="HCSB")
