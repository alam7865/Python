import re

def task():
    print("===== WelCome To CalCulator App =====")
    
    with open("context1.txt",'w') as f:
        f.write("")
    while True:
        operation=int(input("Enter\n1 Operation\n2 History\n3 Clear\n4 Exit\n"))
        ans=0
        if operation==1:
            data=input("Enter The Operation =")
            
            parts=re.split(r'(\+|\-|\*|/)',data);
            a=int(parts[0])
            b=parts[1];
            c=int(parts[2])
            
            
            if b=="+":
                ans=a+c
            elif b=="-":
                ans=a-c
            elif b=="*":
                ans=a*c 
            elif b=="/":
                ans=a/c   
            else:
                print("Invalid Operation")
                continue    
            print(ans)
            
            str=f"{a} + {c}={ans}"
            
            with open ("context1.txt",'a') as f:
                f.write(f"{str}\n")
                
        elif operation==2:  
            print("Restored History")  
            with open("context1.txt",'r') as f:
                print(f.read())
                
        elif operation==3:
            with open("context1.txt",'w') as f:
                f.write("");   
                          
        elif operation==4:
            with open("context1.txt",'r') as f:
                print(f.read());
            print("Programm Exit....") 
            break 
        
        else:
            print("Enter a Valid Choice")
            continue    
    
    
    # /////////////////////////////////////////////////////////////////
   
task()                  