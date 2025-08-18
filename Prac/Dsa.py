# arr = [1, 2, 3, 4, 5]

# for x in range(0, len(arr), 2):
#     print(arr[x])

# arr1 = []
# n = len(arr)
# arr1.append(arr[n - 1])
# for x in range(0, len(arr) - 1):
#     arr1.append(arr[x])

# print(arr1)


# /////////////////////////////////////////////////////////////

# arr = [1, 2, 3, 4, 5]
# n = len(arr) - 1

# prev = arr[0]

# for x in range(1, len(arr)):
#     curr = arr[x]
#     arr[x] = prev
#     prev = curr

# arr[0] = prev
# print(arr)

# //////////////////////////////////////////////////////////////

# arr = [16, 17, 4, 3, 5, 2]
# res = [16, 17, 4, 3, 5, 2]

# st = []
# st.append(-1)

# for x in range(len(arr) - 1, -1, -1):
#     pres = arr[x]

#     if arr[x] >= st[-1]:
#         while st and arr[x] > st[-1]:
#             st.pop()

#     if st:
#         arr[x] = st[-1]
#     else:
#         arr[x] = -1

#     st.append(pres)


# print(arr)


# /////////////////////////////////////////////////////////////////////////////////
str = "testsample"
maxFreq = -1
maxchar = "z"
dict1 = {}

for x in range(len(str)):
    dict1[str[x]] = dict1.get(str[x], 0) + 1
    maxFreq = max(maxFreq, dict1.get(str[x]))


for key, value in dict1.items():
    if maxFreq == value:
        or1 = ord(key)
        or2 = ord(maxchar)
        if or1 < or2:
            maxchar = key

print(maxFreq, maxchar)
