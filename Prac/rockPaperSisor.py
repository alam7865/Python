import random;

str=["Rock","Paper","Sisor"];
print(str)
score1=0;
score2=0;

print("----------------------How Many times You Want to Play the Game: ")
x=int (input())
# print(x)
i=1

for i in range(x):  # Generates numbers 0 to 4
    human=input()
    humanGet=human
    idx=random.randrange(0,4);
    computerGet=str[idx];
    
    
    print(humanGet,computerGet)
    
    if humanGet=="Rock":
        if computerGet=="Paper":
            score2+=1;
        elif computerGet=="Sisor":
            score1+=1;  
    
    if humanGet=="Paper":
        if computerGet=="Sisor":
            score2+=1;
        elif computerGet=="Rock":
            score1+=1;          
        

    if humanGet=="Sisor":
        if computerGet=="Rock":
            score2+=1;
        elif computerGet=="Paper":
            score1+=1;


if score1>score2:
    print("Human Win",score1,score2);
elif score2>score1:    
    print("Computer Win",score1,score2);
else:
    print("Match Drow",score1,score2)    