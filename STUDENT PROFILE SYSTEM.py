
class Student:
    
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks


    def display_info(self):
        print("\n--- STUDENT PROFILE ---")
        print("Name  :", self.name)
        print("Roll  :", self.roll)
        print("Marks :", self.marks)

    
    def check_result(self):
        if self.marks >= 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")



name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))


student1 = Student(name, roll, marks)


student1.display_info()
student1.check_result()
