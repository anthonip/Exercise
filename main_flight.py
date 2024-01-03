import Flight_Tkt as f
print("\n1. Display Status")
print("2. Change Status\n")
user = int(input("Enter your Choice: "))
while user == 1 or user == 2:
    if user == 1:
        f.display_status()
    elif user == 2:
        clas = input("Enter Class: ")
        seat = input("Enter Seat No: ")
        f.change_status(clas,seat)
    print("\n1. Display Status")
    print("2. Change Status\n")
    user = int(input("Enter your Choice: "))
