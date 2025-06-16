# def fun():
#     print("Hello Bhai")

# fun()

# //////////////////////////////////////////////////
# def fun(x):
#     print("Hello",x)

# fun(["apple","Mango","Orange"])        

#///////////////////////////////////////////////////
# def fun(a,b):
#     print("Hello: ",a+" "+b)
 
# fun("Sabaz","Alam")   

#///////////////////////////////////////////////////////
# def fun(*key):
#     print("My Name is: ",key[3]); 

# fun("Alam","Gopal","Kiran")    

#/////////////////////////////////////////////////////////

# def fun(child1,child2,child3):
#     print("My name is : ",child3)
    
# fun(child1="Sabaz Alam",child2="Abdul Kalam",child3="Gopal")    

#////////////////////////////////////////////////////////

# def fun(**kid):
#     print("His last name is " + kid["first"])
    
# fun(first="Sabaz",last="Alam",age="23");    


#///////////////////////////////////////////////////////
# def fun(country="India"):
#     print("My Country is: ",country)
 
# fun("America");    
# fun("Ice Land");    
# fun("Brazil");
# fun()

#///////////////////////////////////////////////////////

# def fun(x):
#     for i in x:
#         print(i)

# fun(["Apple","mango","orange","Banana"])        

#////////////// Return //////////////////////////////////

# def fun(x):
#     # return x*10;
#     return ["Apple","Mango","Orange","Banana"];

# x=fun(3)
# print(x)

#////////////////////////////////////////////////////////

def fun(x):
    if x>0:
        fun(x-1)
        print(x);

fun(6)        