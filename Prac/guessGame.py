import random;



i=1;
score1_Hum=0;
score2_Com=0;
for i in range(5):
    print("Guess The Number From 1 to 10")
    num1=random.randrange(1,11);
    num2=int(input());

    print("Your Guess Is: ",num2)
    print("Computer Guess Is: ",num1)
    
    if num1>num2:
        score2_Com+=1
    elif num1<num2:
        score1_Hum+=1
        
            

if score1_Hum>score2_Com:
    print("Human Wim the game🥳")
    print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);
    
elif score1_Hum<score2_Com:
    print("Computer Wim the game🥳")
    print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);   
else :
    print("Match is Draw")
    print("Human Score: ",score1_Hum,"Computer Score: ",score2_Com);     