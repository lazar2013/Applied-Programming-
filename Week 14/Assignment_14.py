# Define the Employee base class.
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

# Define the Manager class which will inherit everthing from the Employee class.
class Manager(Employee):

    # Adding bonuses just for managers and setting bonus to 0
    bonus = 0.00

    # Mutator New Method (only for managers):
    def set_bonus(self, b):
        self.bonus = b

    # Accessor New Method (only for managers):
    def get_bonus(self):
        return self.bonus

    # Override position to include "Manager:" in front.
    def get_position(self):
        return 'Manager: ' + self.position

# Three employees information:
employee1 = Employee('Joy Rogers', 81774, 'Manufacturing', 'Engineer') # Regular employee
employee2 = Employee('Mark Jones', 39119, 'IT', 'Programmer') 
manager1 = Manager('Susan Meyers', 47899, 'Accounting', 'Vice President') # Manager employee with bonus and position override
manager1.set_bonus(2500.00)

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

print('Manager 1:')
print('Name:', manager1.get_name())
print('ID Number:', manager1.get_idNumber())
print('Department:', manager1.get_department())
print('Position:', manager1.get_position())
print('Bonus: $', format(manager1.get_bonus(), '.2f'))
print()