# x="Alam";
# def myfun():
#     x="Sabaz Alam"
#     print(x);
    
# myfun()
# print(x);
# /////////////////////////////////////////
    
# x="Alam";
# def myfun():
#     print(x);

# myfun(); #////// Alam        

# ////////////////////////////////////////////

# def myfun():
#     global x
#     x="Alam";
#     print(x);
    
# myfun();
# print(x)

# ////////////////////////////////////////////////////

x=1;
y=2.8;
z=1j;

# p=float(z);
# print(p);
# print(type(float(z)))

# //////////////////////////////
# p=int(z)
# print(p)
# print(type(p))

#///////////////////////////////////
# import random
# print(random.randrange(1,11));

#/////////////////////////////////////

# s="Banana";
# for x in "Sabaz":
#  print(x);

#/////////////////////////////////////////

# txt="Hello Sabaz Alam Bhai";
# if "Sabaz" in txt:
#     print("Yes It is Present");
    

# txt1="Hello Bhai kk";
# if "kk1" not in txt1:
#     print("It is Not Present");    

#////////////////////////////////////////
# s="Hello World";
# # print(s[0:5])  // Hello
# # print(s[:5])   // printing from the start
# print(s[5:]);

#/////////////////////////////////////////
# x=" Sabaz Alam ";
# print(x.upper()) #  SABAZ ALAM 
# print(x.strip()) # Sabaz Alam
# print(x.split()) #['Sabaz', 'Alam']
# print(x.replace('S','K')) #  Kabaz Alam

# ////////////////// Concation /////////////////////////
# a="Sabaz";
# b="Alam";
# c=a+" "+b;
# print("Result: "+ c) // Result: Sabaz Alam

# /////////////////////////////////////////////////////
# age=21;
# txt=f"My Name is {age}. I read in B.Tech";
# print(txt);

#//////////////////////////////////////////////////////
# price=12;
# txt=f"The Price is {price:.2f}";
# print(txt);

#//////////////////////////////////////////////////////
# txt="Hello my name is \"Sabaz\" from India";
# print(txt);

#//////////////////////////////////////////////////////
str="Hello my Name is Sabaz";

# print(str.capitalize()) # Hello my name is sabaz
# print(str.casefold()) # hello my name is sabaz
# print(str.center(30,'-')) # ----hello my Name is Sabaz----
# print(str.count('p')) # 0
# print(str.encode()) # b'Hello my Name is Sabaz'
# print(str.endswith('Sabaz')); # True
# print(str.expandtabs()) # Hello my        Name     is Sabaz
# print(str.find('z')) # 21
# print(str.isnumeric()) # true
# print(str.join("Hero"));
# print(str.swapcase())
# print(str.title()) # Hello My Name Is Sabaz
print(str.translate())
