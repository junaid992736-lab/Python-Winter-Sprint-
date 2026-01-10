#CALCULATING AVG MARKS
Student_name=input("Please Enter Your Name:")
Subject=int(input("Please Enter No. Of Subject:"))

i=1
Sum=0
while i<=Subject:      
    Marks=int(input(f"Please Enter Your Marks Of Subject {i}:"))
    i=i+1
    Sum=Sum+Marks                          
      
if Subject==0:
    print("Subject Can Not Be Zero")
else:
    Average=Sum/Subject
    print("\n    |RESULT SUMMARY|    ")           
    print("STUDENT NAME:",Student_name)                    
    print("TOTAL MARKS:",Sum)     
    print("AVERAGE MARKS:",Average)
