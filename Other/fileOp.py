# //////////////////////////////////Opening File //////////////////////////////

# with open("./Other/text1.txt", "r") as f:
#     print(f.read())

# ////////////////////////////////// Write File //////////////////////////////

# with open("./Other/text1.txt", "w") as f:
#     f.write("This Is Sabaz Alam")

# ////////////////////////////////// Append file //////////////////////////////

# with open("./Other/text1.txt", "a") as f:
#     f.write("\nHHHHHHH")

# ////////////////////////////////////// x //////////////////////////////////////

# with open("./Other/text2.txt", "x") as f:
#     print("file Created")

# /////////////////////////////// Delete File ////////////////////////////

# import os
# os.remove("./Other/text2.txt")

# //////////////////////////////

# import os

# if os.path.exists("./Other/text1.txt"):
#     os.remove("./Other/text1.txt")
# else:
#     print("File Does Not Exit")
