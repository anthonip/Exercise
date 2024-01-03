student = []
def add_student(reg_no , name, marks):
    stud = {
        "Reg.no" : reg_no,
        "Name" : name,
        "Marks": marks
        }
    student.append(stud)
    print(f"{name} added to the list.")
def calculate_marks(marks):
    total = sum(marks)
    count = len(marks)
    average = total/count
    def grade():
        grade = ["A","B","C","D","NG"]
        if average >= 90:
            return grade[0]
        elif 80 <= average <= 89:
            return grade[1]
        elif 70 <= average <=79:
            return grade[2]
        elif 60 <= average <= 69:
            return grade[3]
        else:
            return grade[4] 
    return total, average, grade()
def display_students(reg_no = "ALL"):
    if reg_no == "ALL":
        print(f"{'Reg.No':<10}{'Name':<20}{'Total':<8}{'Average':<10}{'Grade':<5}")
        for stud_dict in student:
            total, average, grade = calculate_marks(stud_dict["Marks"])
            print(f"{stud_dict['Reg.no']:<10}{stud_dict['Name']:<20}{total:<8}{average:<10}{grade:<5}")
    else:
        for stud_dict in student:
            if reg_no == stud_dict["Reg.no"]:
                total, average, grade = calculate_marks(stud_dict["Marks"])
                print(f"{'Reg.no':<10} : {stud_dict['Reg.no']} \n{'Name':<10} : {stud_dict['Name']} \n{'Total':<10} : {total} \n{'Average':<10} : {average} \n{'Grade':<10} : {grade}")
            
            
        

