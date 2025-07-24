# import time

# initTime = time.time()
# print(initTime)
# for i in range(10):
#     # print(i)
#     time.sleep(1)

# print(time.time() - initTime)


# ///////////////////////////////////////////////////
# list = ["apple", "mango", "orange"]

# for index, list in enumerate(list, start=1):
#     print(index, list)


# //////////////////////////////////////////////////

# number = ["11", "22", "33", "44", "55"]
number = [1, 2, 3, 4, 5, 6]

# for i in range(len(number)):
#     number[i] = int(number[i])
#     print(number[i] * 10)


# def sqr(x):
#     return x * x


# num = list(map(sqr, number))
# print(num)


# ////////////////////////////////////////////////////


num = list(map(lambda x: x * x, number))
print(num)
