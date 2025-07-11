def task():
    tasks=[];
    print("=====WELCOME TO TASK MANAGEMENT APP====")
    
    total_task=int(input("Enter How Many Task You Want To Add ="))
    for i in range(1,total_task+1):
        task_name=input(f"Enter Task {i}= ")
        tasks.append(task_name)
        
    print(f"Today's Tasks are\n{tasks}\n")
    
    while True:
        operation=int(input("Enter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation==1:
            add=input("Enter the Task You Want to add = ")
            tasks.append(add)
            print(f"Task {add} has been Added....")
            print(f"Task Are: {tasks}\n")
            
        elif operation==2:
            update_val=input("Enter the Value You Want To Update= \n")
            if update_val in tasks:
                up=input("Enter New Task= ")
                idx=tasks.index(update_val)
                tasks[idx]=up;
                print(f"Updated Task are: {tasks}")
                
        elif operation==3:
            delete_val=input("Enter The Task You Want to Delete= \n")
            if delete_val in tasks:
               idx=tasks.index(delete_val);
               tasks.pop(idx)    
               print(f"\nTasks: {tasks}")    
        
        elif operation==4:
            print(f"\nThe Tasks Are: {tasks}")
                   
        elif operation==5:
            print("Programm End...")
            break        
                
    
task();        