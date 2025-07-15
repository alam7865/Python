# x=lambda a:a+10
# print(x(5)) # 15

# x=lambda a,b:a*b
# print(x(5,5))

# x=lambda a,b,c:a+b+c
# print(x(5,5,5))


def myfunc(n):
    return lambda a:a*n

mydouble=myfunc(2)
myTriple=myfunc(3)
print(mydouble(11))
print(myTriple(11))