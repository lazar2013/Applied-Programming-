import csv
# Read the customers file and create a list of customers. 
def read_customers(filename):
    customers = [] #create an empty list 
    file = open(filename, "r")
    reader = csv.reader(file)
    for parts in reader:
        if len(parts) >= 10:
            company = parts[1]
            contact = parts [2]
            phone = parts[9]
            customer = (company, contact, phone)
            customers.append(customer)
    file.close()
    return customers

# Display customers by company name. 
def display_by_company(customers):
    print()
    print("Customers sorted by company name")
    print()

    for customer in sorted(customers): #loop through sorted customers
        print ("Company:", customer[0])
        print("Contact:", customer[1])
        print("Phone:", customer [2])
        print()


# Display customers by contact name.
def display_by_contact(customers):
    print()
    print("Customers sorted by contact name")
    print()

    contact_list = []

    for customer in customers: 
        contact_list.append(customer[1])

    contact_list.sort()

    for contact in contact_list:
        for customer in customers: 
            if customer[1] == contact: 
                print("Contact:", customer[1])
                print("Company:", customer[0])
                print("Phone:", customer[2])
                print()


# Search customers by company name.
def search_company(customers):
    name = input("Enter company name to search:")
    
    for customer in customers:
        if name in customer[0]:
            print("Company:", customer[0])
            print("Contact:", customer[1])
            print("Phone:", customer[2])
            print()

# Search customers by contact name. 
def search_contact(customers):
    name = input("Enter contact name to search:")

    for customer in customers:
        if name in customer[1]:
            print("Contact:", customer[1])
            print("Company:", customer[0])
            print("Phone:", customer[2])
            print()

# Menu Function.
def menu():
    print("1. Customers sorted by company name")
    print("2. Customers sorted by contact name")
    print("3. Search customers by company name")
    print("4. Search customers by contact name")
    print("5. Exit")


#Main Function.
def main():
    customers = read_customers("Northwind Customers.txt")
    choice = 0
    while choice !=5:
        menu()
        choice = input("Enter Choice Number:")

        if choice == "1":
            display_by_company(customers)

        elif choice == "2":
            display_by_contact(customers)

        elif choice == "3":
            search_company(customers)

        elif choice == "4":
            search_contact(customers)

        elif choice == "5":
            print("Exit")

        else:
            print("Invalid choice")

main()