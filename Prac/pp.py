# x=["apple",'banana'];
# y=["apple","banana"];

# print(x is y)


# ////////////////////// Expoential ///////////////////////////
# print(2**3)
# print(5**2)
# x=int (9**0.5);
# # print(9**0.5)
# print(x)

#////////////////////// List /////////////////////////////////
# list=[]
# list.append("apple");
# list.append("Mango");
# list.append("Orange");
# # print(list)

# list[1]='Sabaz Alam'
# print(list)

# list.pop(1)
# print(list)
# print(len(list))

# ///////////////////////////////////// List Operation ///////////////////
# list=["Apple","mango","Orange"];
# print(list)

# list=("apple","mango","orange");
# list[0]="sabaz";
# print(list[0])

# //////////////////////////////////////// Operation //////////////////////
# list1=["apple","mango","orange","banana","graps","kiwi"];
# # print(list1[0:3])
# print(list1[2:3])

# ////////////////////////////////////// Combining ////////////////////////
# list1=["apple","mango","Orange"]
# list2=["Ants","Elephant","Ostrich"]
# # list1.extend(list2);  #['apple', 'mango', 'Orange', 'Ants', 'Elephant', 'Ostrich']
# # print(list1[1:])

# list1.clear();
# print(list1)

#//////////////////////////////////////// Loop //////////////////////////
# list1=["apple","mango","Orange"]
# list2=["Ants","Elephant","Ostrich"]
# list1.extend(list2)
# # for x in list1:
# #     print(x)

# n=len(list1)

# for x in range(0,n):
#     print(list1[x])

#///////////////////////////////////// Lower ////////////////
# list1=["apple","mango","Orange"]
# list2=["ants","Elephant","Ostrich"]
# # print(list1.toLowerCase())

# list3=[]
# list1.extend(list2)

# for x in list1:
#     if "a" in x:
#         list3.append(x)
        

# print(list3)        


# for i in range(len(list1)):
#     list1[i]=list1[i].lower();
    
# list1.sort(reverse=True)    
# print(list1)    

# ////////////////////////////////////////

# list4=list(list1)
# list4=list1.copy()
# print(list4)

#//////////////////////////////////////////
# def myfunc(x):
#     print(x+" "+"Alam")

# # myfunc("Sabaz")
# myfunc("Abul")

#////////////////////////////////////////////

# def myfunc(*x):
#     print(x[1])
    
# myfunc("apple","mango","orange","banana","graps")    


# /////////////////////////////// File Operation ////////////////////

# 1)read

# with open("text.txt","r") as f:
#     print(f.read())


# 2)write
# with open("text.txt","w") as f:
#     f.write("AAAAAAAAAAAA")

# 3)Append
# with open("text.txt","a") as f:
#     f.write("\nSabaz ALam")

# 4)read line by line
with open("text.txt","r") as f:
    for line in f:
        print(line)