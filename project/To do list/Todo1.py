def task():
    tasks=[];
    
    print("===== WelCome To ToDo Application =====")
    len=int(input("How Many The Task You Want To Add ="))
    
    
    for i in range(1,len+1):
        data=input(f"\nEnter The Task {i} : ").lower();
        tasks.append(data)
        
    print(f"Task are: {tasks}");
    
    while True:
        operation=int(input("Enter\n1 Add\n2 Update\n3 Delete\n4 View\n5 Exit/Stop\n"))
        if operation==1:
            data=input("Enter the Task You Want to Add =").lower();
            tasks.append(data);
            print(f"The Task Are: {tasks}")
            
        elif operation==2:
            update_val=input("Enter The Value You Want To Update: ").lower();
            if update_val in tasks:
                data=input("Enter The Value You Want TO Add =").lower();
                idx=tasks.index(update_val);
                tasks[idx]=data;
                print(f"Updated Task: {tasks}")
                
        elif operation==3:
            data=input("Enter the Value You Want To Delete =")
            if data in tasks:
                tasks.remove(data);
                print(f"The Task Are: {tasks}") 
                
        elif operation==4:
            print(f"Task Are: {tasks}")               
        elif operation==5:
            print(f"The Task Are: {tasks}")
            print("Programm End...")
            break
        
    
    
task(); 