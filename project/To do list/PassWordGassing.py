import random
def task():
    print("======= WelCome To PassWord Gassing Game =======")
    
    easy_lvl=["apple","tiger","dog","horse","cat","lion"];
    medium_lvl=["python","bottle","monkey","plant","laptop"]
    hard_lvl=["elephant","diamond","umberalla","computer","mountain"]
    
    print("Choose The Defficulty Level Among :Easy Medium  Hard");
    chosen_data=input("Enter Defficulty Level =").lower()
    
    while True:
        if chosen_data=="easy":
            comp_chos=random.choice(easy_lvl)
            count=0
            for i in range(1,5):
                my_chos=input("Enter Your Choice: ").lower()
                count=count+1
                if my_chos==comp_chos:
                    print(f"Congroulation You Win: Time = {count}")
                    return
                else:
                    print("Wrong Guess Try Again.")

            return        
        elif chosen_data=="medium":
            comp_chos=random.choice(medium_lvl)
            count=0
            for i in range(1,5):
                my_chos=input("Enter Your Choice: ").lower()
                count=count+1
                if my_chos==comp_chos:
                    print(f"Congroulation You Win: Time = {count}")
                    return
                else:
                    print("Wrong Guess Try Again.")
                    
        elif chosen_data=="hard":
            comp_chos=random.choice(easy_lvl)
            count=0
            for i in range(1,5):
                my_chos=input("Enter Your Choice: ").lower()
                count=count+1
                if my_chos==comp_chos:
                    print(f"Congroulation You Win: Time = {count}")
                    return
                else:
                    print("Wrong Guess Try Again.") 
                               
        else:
            print("Enter a Valid Choise")  
            return
        
task()                  