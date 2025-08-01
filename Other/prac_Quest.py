# str = "hello my name is sabaz alam"
# seen = {}
# for i in str:
#     if "a" <= i <= "z":
#         seen[i] = seen.get(i, 0) + 1

# print(seen)

# for i in seen:
#     print(i, seen.get(i))


# ////////////////////////////////////////////////////////////////////////////////

# Str = "hello My Name is sabaz"
# print(Str.capitalize())

# main

str1 = "    Sabaz Alam    "
str = "Sabaz Alam"

# ///// Strip
# print(str1.strip())

# ///// replace
# print(str1.replace("S", "A"))

# //// split
# str1 = "Sabaz Alam"
# print(str1.split(" "))

# ////// sort
# print(str1.capitalize())

# ///// casefold
# print(str.casefold())

# ///// centered
# print(str.center(20))
# print(str.center(20, "#"))

# //// count
# print(str.count("a"))

# //// endsWith
# print(str.endswith("m"))

# text = "Hello\tWorld"
# print(text.expandtabs(4))

# /////// find
# print(str.find("Alam"))

# /////////
txt = "hello sabaz alam"

# aa = "a"
# num = ord(aa)
# print(num)

# print(chr(98))
# //////
# aaa = "A"
# num = ord(aaa)
# print(num)


# for i in txt:
#     num = ord(i)
#     if i - 1 == " " and "a" <= i <= "z":
#         num -= 32
#         print(chr(num))
#     else:
#         print(i)


for i in range(len(txt)):
    ch = txt[i]
    # print(ch, end="")
    num = ord(ch)
    if i == 0:
        if num >= 97:
            num -= 32
            print(chr(num), end="")
    elif txt[i - 1] == " " and "a" <= ch <= "z":
        num -= 32
        print(chr(num), end="")
    else:
        print(ch, end="")


print(txt.title())
