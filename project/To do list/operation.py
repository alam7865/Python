# with open('content.txt', 'r') as f:
#     data = f.read()
#     print(data)

# ////////////////////// Read //////////////////////////
# with open('content.txt','r') as f:
#     data=f.read()
#     print(data)

# ////////////////////////// Write /////////////////////
# with open('context1.txt','w') as f:
#     f.write("Hello World");
#     print("File Write SuccessFully")


# ////////////////////////////// Append ////////////////////
# with open('context1.txt','a') as f: 
#     f.write("\nThis Is Sabaz Alam")

# ///////////////////////////// Read + write //////////////////
with open('content.txt', 'r+') as f:
    content1 = f.read()
    # f.seek(0)
    print(content1)
    f.write("Updated content")