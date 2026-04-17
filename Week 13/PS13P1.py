# Define the Employee class.
class Employee: 
    
    # Constructor: Accepts all four values
    def __init__(self, name, idNumber, department, position):
        # Store each value as a member variable
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    # Mutator functions:
    def set_name(self, name):
        self.name = name

    def set_idNumber(self, idNumber):
        self.idNumber = idNumber

    def set_department(self, department):
        self.department = department

    def set_position(self, position):
        self.position = position 

    # Accesor functions:
    def get_name(self):
        return self.name

    def get_idNumber(self):
        return self.idNumber

    def get_department(self):
        return self.department 

    def get_position(self):
        return self.position

# Three employees information:
employee1 = Employee('Susan Meyers', 47899, 'Accounting', 'Vice President')
employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer')
employee3 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer')

# Display the information.
print('Employee 1:')
print('Name:', employee1.get_name())
print('ID Number:', employee1.get_idNumber())
print('Department:', employee1.get_department())
print('Position:', employee1.get_position())
print()

print('Employee 2:')
print('Name:', employee2.get_name())
print('ID Number:', employee2.get_idNumber())
print('Department:', employee2.get_department())
print('Position:', employee2.get_position())
print()

print('Employee 3:')
print('Name:', employee3.get_name())
print('ID Number:', employee3.get_idNumber())
print('Department:', employee3.get_department())
print('Position:', employee3.get_position())
print()