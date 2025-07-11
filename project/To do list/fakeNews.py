import random
gen_Data=[]
def task():
    subject=[]
    action=[]
    place=[]
    
    subject.append("Sabaz Alam");
    subject.append("Salman Khan");
    subject.append("Sohail Alam");
    subject.append("Pratap Sing");
    subject.append("Pradipto Shivam");
    
    
    action.append("riding Cow");
    action.append("riding Bull");
    action.append("Eating Pen");
    action.append("Playing with Balloon");
    action.append("Playing with cart");
    
    place.append("near India Gate");
    place.append("near Taj Mahal");
    place.append("near Fly Over");
    place.append("near Bijni Stand");
    place.append("at Red Fort");
    
    
    print("===== WelCome To Fake News Generator ======")
    while True:
       r1=random.randrange(0,5);
       r2=random.randrange(0,5);
       r3=random.randrange(0,5);
       ss =(f"{subject[r1]} {action[r2]} {place[r3]}")
       print(ss)
      
         
       operation=int(input("Enter\n1 Generate\n2 Save\n3 Exit\n"))
       if operation==1:
         continue 
         
       elif operation==2:
         gen_Data.append(ss)
         print("Generate News Saved Successfully...")
       elif operation==3:
         print("Programm End...")
         print(f"Saved News Are: {gen_Data}")
         break    
    
    
task() 
    


  