import random

person = ["Sabaz Alam", "Salman Khan", "Sohail ALam", "Yuvraj", "Pratap"]
place = ["Bijni", "Delhi", "Agra", "Noida"]
activities = [
    "Playing Card At",
    "Riding Horse Near",
    "Playing FootBall At",
    "Dancing Near",
]

data = []


def myTask():
    print("======== Welcome To Fake News Generator ========")

    while True:
        p1 = random.choice(person)
        p2 = random.choice(activities)
        p3 = random.choice(place)

        print("Enter \n1 Generate\n2 Exit")

        num = int(input("Enter Your Choise\n"))

        if num == 1:
            news = f"Fake News:{p1} {p2} {p3}"
            print(news)

            with open("./Prac/text.txt", "a") as f:
                f.write(news + "\n")
        elif num == 2:

            with open("./Prac/text.txt", "r") as f:
                print(f.read())

            break


myTask()
