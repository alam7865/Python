def myTask():

    task = []

    print("=======  WelCome To List Operation ========")
    while True:
        print(f"1 Add\n2 Update\n3 delete\n4 Print\n5 Exit")

        num = int(input("Enter Your Choise\n"))

        if num == 1:
            data = input("Enter The Task You Want To Add\n").lower()
            task.append(data)

        elif num == 2:
            data = int(input("Enter The Index Where You Want To Insert\n"))
            newTask = input("Enter New task\n")
            task[data] = newTask
            print("Your Task are: ", task)

        elif num == 3:
            data = input("Enter the task You Want To Delete\n")

            while True:
                if data in task:
                    idx1 = task.index(data)
                    task.remove(task[idx1])
                    print("Your New Task Are: ", task)
                    break

                else:
                    print("Enter a Valid Task To remove")
                    data = input("Try Again")

        elif num == 4:
            print("Your Task Are: ", task)
        elif num == 5:
            break


myTask()
