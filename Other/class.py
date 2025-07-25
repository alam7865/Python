# class Student:
#     name = "Alam"


# s1 = Student
# print(s1.name)


# /////////////////////////////////////////////////////


# class Car:
#     # def __init__(self):
#     #     print("Hello")
#     wheel = 4
#     door = 4
#     comfort = "good"


# c1 = Car()

# print(c1.door, c1.comfort, c1.wheel)


# /////////////////////////////////////////////////////

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Constructor is Being Called")


# s1 = Student("Alam")
# print(s1.name)

# ////////////////////////////////////////////////////////


# class Student:
#     def __init__(self, name):
#         self.name = name
#         print(f"New Student {self.name} added To dataBase...")


# s1 = Student("Sabaz")
# print(s1.name)

# s2 = Student("Alam")
# print(s2.name)

# ////////////////////////////////////////////////////////////


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


# s1 = Student("Ramu", 77)
# print("Name: ", s1.name + " " + "Marks: ", s1.marks)

# ////////////////////////////////////////////////////////////


# class Student:
#     College = "Nit Silchar"

#     def __init__(self, name):
#         self.name = name


# s1 = Student("Sabaz")
# # print(s1.name)
# s1.College = "IIT Bombay"
# print(s1.name)
# print(s1.College)
# print(Student.College)

# ////////////////////////////////////////


# class Student:
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Hello: ", self.name)


# s1 = Student("Sabaz")
# s1.hello()


# /////////////////////////////////////// name marks of 3 student ////////////

# class Student:
#     # def __init__(self, name, mark1, mark2, mark3):
#     #     self.name = name
#     #     self.mark1 = mark1
#     #     self.mark2 = mark2
#     #     self.mark3 = mark3


#     def printStudent(self):
#         print("Name: ", self.name + " " + "Marks: ", self.mark1, self.mark2, self.mark3)


# s1 = Student("Sabaz", 78, 79, 80)
# s1.printStudent()


# ////////////////////////////////////////// pass mark array ////////////////


# class Student:
#     def __init__(self, name, list):
#         self.name = name
#         for i in range(len(list)):
#             self.l

#     def printStudent(self):
#         print("Name: ", self.name + " " + "Marks: ", self.mark1, self.mark2, self.mark3)


# s1 = Student("Sabaz", [56, 57, 58])
# s1.printStudent()


# /////////////////////////////////////////////////////////////////////


# class Student:
#     def __init__(self, name=None, marks=None):
#         self.name = name
#         self.marks = marks

#     def showDetails(self):
#         print("Name:", self.name, "Marks: ", self.marks)


# s1 = Student()
# s1.marks = [12, 13, 14, 15]
# s1.name = "Alam"
# print(s1.name)
# print(s1.marks)


# ///////////////////////////////////////////////////////


# class Student:
#     def showDetails(self):
#         print("Name:", self.name + " " + "Marks:", self.marks)


# s1 = Student()
# s1.name = "Sabaz"
# s1.marks = [98, 99, 100]
# s1.showDetails()


# //////////////////////////////////////////////////////////
class Student:
    @staticmethod
    def College():
        print("Hello World")


s1 = Student()
s1.College()
