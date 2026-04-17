# Define the Patient class.
class Patient: 
    
    # Constructor: Accepts all patient information
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone, emergency_name, emergency_phone):
        # Store each value as a member variable
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.emergency_name = emergency_name
        self.emergency_phone = emergency_phone

    # Mutator functions:
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_middle_name(self, middle_name):
        self,middle_name = middle_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_address(self, address):
        self.address = address

    def set_city(self, city):
        self.city = city 
    
    def set_state(self, state):
        self.state = state

    def set_zip_code(self, zip_code):
        self.zip_code = zip_code

    def set_phone(self, phone):
        self.phone = phone

    def set_emergency_name(self, emergency_name):
        self.emergency_name = emergency_name

    def set_emergency_phone(self, emergency_phone):
        self.emergency_phone = emergency_phone

    # Accesor functions:
    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.last_name

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_zip_code(self):
        return self.zip_code

    def get_phone(self):
        return self.phone

    def get_emergency_name(self):
        return self.emergency_name

    def get_emergency_phone(self):
        return self.emergency_phone

# Define the Procedure class.
class Procedure: 
    
    # Constructor: Accepts all four values
    def __init__(self, name, date, practitioner, charge):
        # Store each value as a member variable
        self.name = name
        self.date = date
        self.practitioner = practitioner
        self.charge = charge

    # Mutator functions:
    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_practitioner(self, practitioner):
        self.practitioner = practitioner

    def set_charge(self, charge):
        self.charge = charge

    # Accesor functions:
    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def get_practitioner(self):
        return self.practitioner

    def get_charge(self):
        return self.charge

# Sample Patient:
patient = Patient('Susan', 'Velma', 'Meyers', '444 Shrek Drive', 'Chicago', 'IL', '60004', '555-052-1234', 'Sandy Bistro', '888-078-1234')

# Procedure objects with provided data:
procedure1 = Procedure('Physical Exam', '04/16/2026', 'Dr. Irvine', '250.00')
procedure2 = Procedure('X-Ray', '04/16/2026', 'Dr. Jamison', '500.00')
procedure3 = Procedure('Blood Test', '04/16/2026', 'Dr. Smith', '200.00')

# Display the patient information.
print('Patient Information:')
print('Name:', patient.get_first_name(), patient.get_middle_name(), patient.get_last_name())
print('Address:', patient.get_address(), patient.get_city(), patient.get_state(), patient.get_zip_code())
print('Phone:', patient.get_phone())
print('Emergency Contact:', patient.get_emergency_name(), patient.get_emergency_phone())
print()

# Display Procedure 1 information:
print('Procedure 1:')
print('Name:', procedure1.get_name())
print('Date:', procedure1.get_date())
print('Practitioner:', procedure1.get_practitioner())
print('Charge: $', procedure1.get_charge())
print()

# Display Procedure 2 information:
print('Procedure 2:')
print('Name:', procedure2.get_name())
print('Date:', procedure2.get_date())
print('Practitioner:', procedure2.get_practitioner())
print('Charge: $', procedure2.get_charge())
print()

# Display Procedure 3 information:
print('Procedure 3:')
print('Name:', procedure3.get_name())
print('Date:', procedure3.get_date())
print('Practitioner:', procedure3.get_practitioner())
print('Charge: $', procedure3.get_charge())
print()

# Display total charges:
total = float(procedure1.get_charge()) + float(procedure2.get_charge()) + float(procedure3.get_charge())
print('Total Charges: $', format(total, '.2f'))