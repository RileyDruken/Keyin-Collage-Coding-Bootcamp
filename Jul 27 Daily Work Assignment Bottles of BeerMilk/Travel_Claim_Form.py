# functions
def Travel_Claim_Form(employee_number, employee_name, location_of_trip, start_date, end_date, car_used, number_of_days,
                      total_kilometers_traveled):
    per_diem_amount = 0
    mileage = 0
    claim_amount = 0

    print(f"employee_number #: {employee_number}")
    print(f"employee_name: {employee_name}")
    print(f"location_of_trip: {location_of_trip}")
    print(f"start_date: {start_date}")
    print(f"end_date: {end_date}")
    print(f"number_of_days: {number_of_days} Days")
    if car_used == "O":
        print("car_used: Own")
        print(f"total_kilometers_traveled: {total_kilometers_traveled}")
        mileage = total_kilometers_traveled * .10
        print(f"Mileage_amount: ${mileage}")
    elif car_used == "R":
        print("car_used: Rented")
        mileage = number_of_days * 56.00
        print(f"Mileage_amount: ${mileage}")
    if number_of_days <= 3:
        per_diem_amount = number_of_days * 85.00
    elif number_of_days >= 4:
        per_diem_amount = number_of_days * 100.00
    claim_amount = per_diem_amount + mileage
    hst = round(per_diem_amount * 0.13,2)
    print(f"claim_amount: ${claim_amount}")
    print(f"HST: ${hst}")
    print("claim_total: $" + str(claim_amount + hst))

# variables

# strings
employee_number: str = ""
employee_name: str = ""
location_of_trip: str = ""
start_date: str = ""
end_date: str = ""

# bools
car_used: str = ""

# ints
number_of_days: int = 0
total_kilometers_traveled: int = 0

# input

employee_number = input("employee number> ")
employee_name = input("employee name> ")
location_of_trip = input("location of trip> ")
start_date = input("start date> ")
end_date = input("end date> ")
car_used = input("What car did you use O for own R for rented> ")
while True:
    try:
        number_of_days = int(input("number of days> "))
        if "O" == car_used:
            total_kilometers_traveled = int(input("total kilometers traveled> "))
        else:
            car_used = "R"
    except:
        print("Exception please enter only numbers")
    else:
        break
# outout

Travel_Claim_Form(employee_number,employee_name,location_of_trip,start_date,end_date,car_used,number_of_days,total_kilometers_traveled)
