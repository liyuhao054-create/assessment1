class User:
    def __init__(self, uid, plate):
        self.__uid = uid
        self.__plate = plate

    def get_uid(self):
        return self.__uid

    def get_plate(self):
        return self.__plate

    # Parent method for polymorphism
    def calculate_fee(self, gross):
        return gross


class MemberUser(User):
    def __init__(self, uid, plate, m_type, eco):
        super().__init__(uid, plate)  # Inheritance
        self.__m_type = m_type
        self.__eco = eco

    def get_m_type(self):
        return self.__m_type

    # Polymorphism: Overriding the calculate_fee method
    def calculate_fee(self, gross, charger_type="AC"):
        discount = 0
        if self.__m_type == "First-Time":
            discount = gross
        elif self.__m_type == "Staff":
            discount = gross * 0.5
        elif self.__m_type == "Student" and charger_type == "AC":
            discount = gross * 0.25

        net = gross - discount

        if self.__eco == "Y":
            net = net - 2
            if net < 0:
                net = 0
        return net


class EVCharger:
    def __init__(self):
        self.__c_type = "AC"  # Default

    # SETTER VALIDATION LOGIC (As required by the assignment)
    def set_c_type(self, c_type):
        if c_type == "AC" or c_type == "DC":
            self.__c_type = c_type
        else:
            print("Invalid Charger! Defaulting to AC.")
            self.__c_type = "AC"

    def get_c_type(self):
        return self.__c_type


class ChargingSession:
    def __init__(self, user_obj, charger_obj):
        self.__user = user_obj
        self.__charger = charger_obj
        self.__hrs = 0

    # SETTER VALIDATION LOGIC (Checking if hours are valid)
    def set_hours(self, hrs):
        if hrs > 0:
            self.__hrs = hrs
        else:
            print("Error: Hours must be more than 0!")
            self.__hrs = 1

    def generate_bill(self, peak, idle, lost):
        h = self.__hrs
        c = self.__charger.get_c_type()

        # Calculate gross fee
        gross = 0
        if c == "AC":
            if h <= 2:
                gross = h * 4
            elif h <= 4:
                gross = 8 + (h - 2) * 6
            elif h <= 6:
                gross = 20 + (h - 4) * 8
            else:
                gross = 36 + (h - 6) * 12
                if gross > 80: gross = 80
        elif c == "DC":
            if h <= 2:
                gross = h * 10
            elif h <= 4:
                gross = 20 + (h - 2) * 15
            elif h <= 6:
                gross = 50 + (h - 4) * 20
            else:
                gross = 90 + (h - 6) * 30
                if gross > 150: gross = 150

        # Polymorphism check
        m_type = "Standard"
        if type(self.__user) == MemberUser:
            net = self.__user.calculate_fee(gross, c)
            m_type = self.__user.get_m_type()
        else:
            net = self.__user.calculate_fee(gross)

        penalty = 0
        if peak == "Y": penalty += 5
        if idle == "Y": penalty += 15
        if lost == "Y": penalty += 30

        final_pay = net + penalty

        print("\n=== OOP RECEIPT ===")
        print("User ID:", self.__user.get_uid())
        print("Car Plate:", self.__user.get_plate())
        print("Type:", m_type)
        print("Charger:", c)
        print("Hours:", h)
        print("Total RM:", final_pay)


# === 2 Test Cases (Instantiating Multiple Objects) ===
if __name__ == "__main__":
    # Case 1: Staff, DC charger, 3 hours (Testing setter validation)
    u1 = MemberUser("0395254", "WAA1234", "Staff", "N")
    c1 = EVCharger()
    c1.set_c_type("DC")  # Using setter validation
    s1 = ChargingSession(u1, c1)
    s1.set_hours(3)  # Using setter validation
    s1.generate_bill("N", "N", "N")

    # Case 2: Student, AC charger, 5 hours, Eco-Pass, Peak hour
    u2 = MemberUser("STU888", "VBB9999", "Student", "Y")
    c2 = EVCharger()
    c2.set_c_type("AC")
    s2 = ChargingSession(u2, c2)
    s2.set_hours(5)
    s2.generate_bill("Y", "N", "N")