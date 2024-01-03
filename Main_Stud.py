import Stud_Mark_Process as s
def adding_stud():
    reg_no = input("Enter Student Reg. No: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks separated by spaces: ").split()
    marks = [int(i) for i in marks]
    s.add_student(reg_no,name,marks)
def display():
    stud_detail = input("How to display Student Details (All/Specific) :").upper()
    if stud_detail == 'ALL':
        print("\n" , "Student Mark List - I PG - Semester 1 (2023-2024)".center(53), "\n")
        s.display_students()
    else:
        reg = input("Enter Student Register Number: ")
        print("\n" , "Student Mark List - I PG - Semester 1 (2023-2024)".center(53), "\n")
        s.display_students(reg)
no_of_student = int(input("Enter Number of student :"))
for i in range(no_of_student):
    print(f"\nEnter the Details of Student {i+1}: \n")
    adding_stud()
display()
