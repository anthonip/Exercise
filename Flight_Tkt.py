available_seats = {
    "Economy": {"A1":True, "A2":False, "B1":True, "B2":True},
    "Business": {"C1":False, "C2":True, "D1":True, "D2":False}
    }
def display_status():
    for key, value in available_seats.items():
        print(f"\n Class: {key}")
        print(" {:<10} {:<15}".format('_'*10,'_'*15))
        print("|{:<10}|{:<15}|".format('Seat','Status'))
        for i, val in value.items():
            def status():
                if val:
                    return "Available"
                else:
                    return "Not Available"
            print("|{:<10}|{:<15}|".format('_'*10,'_'*15))
            print("|{:<10}|{:<15}|".format(i, status()))
        print("|{:<10}|{:<15}|".format('_'*10,'_'*15))
def change_status(class_n, seat_no):
    for key, value in available_seats.items():
        if key == class_n:
            for i, val in value.items():
                if i == seat_no and val:
                    available_seats[class_n][i] = False
                    print("Success. Booking Confirmed")
                    break
                elif i == seat_no and val == False:
                    print("Seat is already booked")
                    
    
