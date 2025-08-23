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


with open("./Other/text3.txt", "x+") as f:
    f.write("AAAAAAAAAAAAAAAAAAAAA")
    f.seek(0)
    print(f.read())
