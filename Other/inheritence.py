# class Animal:
#     def eat(self):
#         print("Animal eats")


# class Cat(Animal):
#     def walk(self):
#         print("Cat uses to Walk on 4 legs")


# c1 = Cat()
# c1.eat()
# c1.walk()


# ////////////////////////////// Multiple Level //////////////////////

# class Animal:
#     def eat(self):
#         print("Animal eats")


# class Mammals(Animal):
#     def birth(self):
#         print("Give Birth")


# class Dog(Mammals):
#     def walk(self):
#         print("Dog walk on 4 Legs")


# d1 = Dog()
# d1.eat()
# d1.birth()
# d1.walk()

# ////////////////////////////////// Hierarchial Inheritence ///////////////////


# class Animal:
#     def eat(self):
#         print("Animal Eats")


# class Dog(Animal):
#     def live(self):
#         print("They Live on Land")


# class Fish(Animal):
#     def live(self):
#         print("They Live on Water")


# f1 = Fish()
# f1.eat()
# f1.live()

# print("======================")
# d1 = Dog()
# d1.eat()
# d1.live()


# ////////////////////////////////////// Multiple Inheritence /////////////////////


# class Bird:
#     def fly(self):
#         print("They Fly on Sky")


# class Mammals:
#     def birth(self):
#         print("They give Birth")


# class Bat(Bird, Mammals):
#     def sleep(self):
#         print("They Sleep Upside down")


# b1 = Bat()
# b1.sleep()
# b1.fly()
# b1.birth()


# //////////////////////////////// Hybroid /////////////////////////////


# class Animal:
#     def eat(self):
#         print("Animal Eats")


# class Bird(Animal):
#     def fly(self):
#         print("They fly in Sky")


# class Mammal(Animal):
#     def birth(self):
#         print("They Give Birth")


# class Bat(Bird, Mammal):
#     def sleep(self):
#         print("They Sleep Upside Down")


# b1 = Bat()
# b1.birth()
# b1.fly()
# b1.eat()


# //////////////////////////////// Super ///////////////////////

# class Animal:
#     def eat(self):
#         print("They Eats")


# class Dog(Animal):
#     def walk(self):
#         super().eat()
#         print("They Live in land")


# d1 = Dog()
# d1.walk()


# /////////////////////////////////////////////////////////////////
