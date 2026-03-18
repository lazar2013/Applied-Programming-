import csv

# Read customers file and create a list of dictionaries. 
def read_customers():
    customers = []
    with open("customers.csv", "r") as file:
        reader = csv.DictReader(file)
        # Make each row into a dictionary.
        for row in reader: 
            customers.append(row)

    return customers

# Sort by company name.
def display_by_company(customers):
    sorted_customers = sorted(customers, key=lambda c: c["CompanyName"].lower())
    print("\nCompany Name, Contact Name, Phone")
    print("----------------------------------------")
    # Print each customer record. 
    for customer in sorted_customers:
        print(customer["CompanyName"], customer["ContactName"], customer["Phone"])

#Sort by contact name. 
def display_by_contact(customers):
    sorted_customers = sorted(customers, key=lambda c: c["ContactName"].lower())
    print("\nContact Name, Company Name, Phone")
    print("----------------------------------------")
    # Print each customer record. 
    for customer in sorted_customers:
        print(customer["ContactName"], customer["CompanyName"], customer["Phone"])

# Search for a company name or part of the name.
def search_company(customers):
    search = input("Enter the company name or part of the company's name: ").lower()
    found = False
    print("\nContact Name, Company Name, Phone")
    print("----------------------------------------")

    #Look through each customer. 
    for customer in customers: 
        if search in customer["CompanyName"].lower():
            print(customer["CompanyName"], customer["ContactName"], customer["Phone"])
            found = True

    # If nothing is a match.
    if found == False:
        print("No match found!")

#Search for contact or part of contact. 
def search_contact(customers):
    search = input("Enter the contact name or part of the contact's name: ").lower()
    found = False
    print("\nContact Name, Company Name, Phone")
    print("----------------------------------------")

    #Look through each customer. 
    for customer in customers: 
        if search in customer["ContactName"].lower():
            print(customer["ContactName"], customer["CompanyName"], customer["Phone"])
            found = True

    # If nothing is a match.
    if found == False:
        print("No match found!")

# Choice Menu 
def get_choice():
    print("\nMenu")
    print("Type 1 to display by company name")
    print("Type 2 to display by contact name")
    print("Type 3 to search by company name")
    print("Type 4 to search by contact name")
    print("Type 5 to Quit/Exit")

    choice = input("Enter your choice: ")

    while choice not in ["1", "2", "3", "4", "5"]:
        print("Choice Not Valid")
        choice = input("Enter your choice: ")
    return choice 

# Main Function
def main():
    # Read customers.csv file and store the data in customers list. 
    customers = read_customers()

    choice = get_choice()

    while choice != "5":
        if choice == "1":
            display_by_company(customers)
        elif choice == "2":
            display_by_contact(customers)
        elif choice == "3":
            search_company(customers)
        elif choice == "4":
            search_contact(customers)

        choice = get_choice()

        print("Please exit! Goodbye!")

main()