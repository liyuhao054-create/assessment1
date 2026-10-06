run_program = "yes"

# 1. Continuous program loop
while run_program == "yes" or run_program == "y":

    print("\n--- Taylor's Smart Campus EV System ---")

    # Get user inputs
    user_id = input("Enter User ID: ")
    car_plate = input("Enter Car Plate: ")
    # Tell user the exact words to type
    m_type = input("Member Type (First-Time, Staff, Student, Standard): ")
    charger = input("Charger Type (AC / DC): ")

    hours = int(input("How many hours charged? "))

    # Extra conditions
    is_peak = input("Is peak hour? (Y/N): ")
    is_idle = input("Is idle parking? (Y/N): ")
    has_eco = input("Has Eco Pass? (Y/N): ")
    is_lost = input("Lost card? (Y/N): ")

    # 2. Calculate Gross Fee
    gross_fee = 0.0

    # check AC charger (both upper and lower case to avoid errors)
    if charger == "AC" or charger == "ac":
        if hours <= 2:
            gross_fee = hours * 4.0
        elif hours <= 4:
            gross_fee = 8.0 + (hours - 2) * 6.0
        elif hours <= 6:
            gross_fee = 20.0 + (hours - 4) * 8.0
        else:
            gross_fee = 36.0 + (hours - 6) * 12.0
            # AC maximum cap is 80
            if gross_fee > 80.0:
                gross_fee = 80.0

    # check DC charger
    elif charger == "DC" or charger == "dc":
        if hours <= 2:
            gross_fee = hours * 10.0
        elif hours <= 4:
            gross_fee = 20.0 + (hours - 2) * 15.0
        elif hours <= 6:
            gross_fee = 50.0 + (hours - 4) * 20.0
        else:
            gross_fee = 90.0 + (hours - 6) * 30.0
            # DC maximum cap is 150
            if gross_fee > 150.0:
                gross_fee = 150.0

    # 3. Calculate Discounts
    discount = 0.0

    if m_type == "First-Time" or m_type == "first-time":
        discount = gross_fee
    elif m_type == "Staff" or m_type == "staff":
        discount = gross_fee * 0.5
    elif (m_type == "Student" or m_type == "student") and (charger == "AC" or charger == "ac"):
        discount = gross_fee * 0.25

    net_fee = gross_fee - discount

    # minus RM 2 for eco pass
    if has_eco == "Y" or has_eco == "y":
        net_fee = net_fee - 2.0
        if net_fee < 0:
            net_fee = 0.0

    # 4. Calculate Surcharges (penalty)
    penalty = 0.0

    if is_peak == "Y" or is_peak == "y":
        penalty = penalty + 5.0
    if is_idle == "Y" or is_idle == "y":
        penalty = penalty + 15.0
    if is_lost == "Y" or is_lost == "y":
        penalty = penalty + 30.0

    final_total = net_fee + penalty

    # 5. Print final bill receipt
    print("\n==== EV CHARGING RECEIPT ====")
    print("User ID      :", user_id)
    print("Car Plate    :", car_plate)
    print("Gross Fee    : RM", gross_fee)
    print("Discount     : RM", discount)
    print("Surcharge    : RM", penalty)
    print("TOTAL PAYABLE: RM", final_total)
    print("=============================\n")

    # check if want to continue
    run_program = input("Do you want to check another car? (yes/no): ")

print("System Closed.")