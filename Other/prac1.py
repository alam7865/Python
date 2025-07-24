# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius**2)

#     def perimeter(self):
#         return 2 * 3.14 * self.radius


# ss = Circle(7)
# print(ss.area())


# ///////////////////////////////////////////////////////////////////////////
class Employee:
    def __init__(self, role, dept, sal):
        self.role = role
        self.sal = sal
        self.dept = dept

    def showDetails(self):
        print(self.role, self.dept, self.sal)


class Enginner(Employee):
    def __init__(self, name, age, role, dept, sal):
        self.name = name
        self.age = age
        super().__init__(role, dept, sal)  # call parent constructor

    def showDetails2(self):
        print("Engineer Details2:", self.name, self.age, self.dept)


ee = Enginner("sabaz", 22, "Engineer", "IT", 5000)
ee.showDetails2()

ss = Employee("Developer", "IT", 1200)
ss.showDetails()
