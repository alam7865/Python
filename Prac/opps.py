# class Student:
#     @staticmethod
#     def College():
#         print("ABC College")

#     def __init__(self, names):
#         # self.chile_name = name
#         self.names = names

#     def name(self):
#         # print(f"Name:{self.name}")
#         # print(self.chile_name)
#         print(self.names)


# s1 = Student("Sabaz")
# # print(s1.name)
# s1.College()
# s1.name()


# //////////////// class
class Student:
    def __init__(self, names, marks):
        self.names = names
        self.marks = marks

    def Details(self):
        print(f"Name: {self.names}  Marks: {self.marks}")

    def avg(self):
        n = len(self.marks)
        sum = 0

        for x in self.marks:
            sum = sum + x

        ans = int(sum / n)
        print(f"AVG: {ans}")

    #  return int sum/n


s1 = Student("Sabaz", [1, 2, 3])
s1.Details()
s1.avg()
