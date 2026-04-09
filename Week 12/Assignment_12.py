import sqlite3
import sys 

# File location:
DATABASE = "C:/Users/lazar/OneDrive/Desktop/Northwind.db"

def execute_sql(sql, params=None):
    try:
        # Connect to the database.
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise 

    try: 
        # Cursor to execute SQL commands.
        cursor = connection.cursor()
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        # Save the changes to the database.
        connection.commit()

    except Exception as exception:
        print(f"Unable to execute {sql}")
        print(exception)
    finally:
        # Close connection when done.
        connection.close()


# Connect to the database and retrieve all table names. 
def list_tables():
    try:
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise

    try:
        cursor = connection.cursor()
        # Get all the table names from the database. 
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Put all tables in a numbered list. 
        print("Tables in the Northwind Database:")
        counter = 1
        for row in rows:
            print(counter, ".", row[0])
            counter = counter + 1

        # Have the user select a table. 
        choice = int(input("Enter the number of the table you want to view: "))
        table_name = rows[choice - 1][0]
        return table_name

    except Exception as exception: 
        print("Could not retrieve tables.")
        print(exception)
    finally:
        connection.close()


# Connect to the database and show all records for selected table.
def display_table(table_name):
    try:
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise

    try:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table_name};"
        cursor.execute(sql)
        rows = cursor.fetchall()

        # Get the column names from the table. 
        column_names = []
        for description in cursor.description:
            column_names.append(description[0])

        print("Row", end="")
        for column in column_names:
            print(f"\t{column}", end="")
        print()

        # Print each row with a row number.
        row_number = 1
        for row in rows:
            print(row_number, end="")
            for value in row:
                print(f"\t{value}", end="")
            print()
            row_number = row_number + 1
    
    except Exception as exception:
         print("Error retrieving table.")
         print(exception)
    finally:
        connection.close()


def modify_table():
    # Display all tables and allow the user to pick one. 
    table_name = list_tables()

    # Ask the user if they want to Insert, Update, or Delete the table.
    print("Select what you would like to do from the following options:")
    print("(I)nsert")
    print("(U)pdate")
    print("(D)elete")
    action = input("Enter I, U, or D to make a choice: ")

    # Functions based on user's choice.
    if action == "I":
        insert_record(table_name)
    elif action == "U":
        update_record(table_name)
    elif action == "D":
        delete_record(table_name)
    else:
        print("Please use I, U, or D to make a choice: ")


def insert_record(table_name):
    # Show the table so the user can see the records.
    display_table(table_name)

    # Get values needed from user. 
    print("Enter the desired values for the new record.")
    print("Type the column name and value name for each field.")
    columns = input("Enter the names for the columns: ")
    values = input("Enter the values: ")

    # The Insert SQL statement. 
    try:
        connection = sqlite3.connect(DATABASE)
    except:
        print("Unable to connect {DATABASE}")
        raise

    try:
        cursor = connection.cursor()
        sql = f"INSERT INTO {table_name} ({columns}) Values ({values});"
        cursor.execute(sql)
        connection.commit()
        print("Updated successfully")
    except Exception as exception:
        print("Retry the import")
        print(exception)
    finally:
        connection.close()


def update_record(table_name):
    display_table(table_name)

    # Get the information needed to update (ID, column, value).
    row_id = input("Enter the ID of the record you want to update: ")
    column = input("Enter the name of the column you want to update: ")
    value = input("Enter the new value: ")

    # SQL statement to update. 
    try:
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise

    try:
        cursor = connection.cursor()
        sql = f"UPDATE {table_name} SET {column} = '{value}' WHERE rowid = {row_id};"
        cursor.execute(sql)
        connection.commit()
        print("Record is updated!")
    except Exception as exception:
        print("Updating record error.")
        print(exception)
    finally:
        connection.close()


def delete_record(table_name):
    display_table(table_name)

    # Get the ID of the record to be deleted. 
    row_id = input("Enter the ID of the record you want to delete: ")

    # Delete SQL statement.
    try: 
        connection = sqlite3.connect(DATABASE)
    except:
        print(f"Unable to connect to {DATABASE}")
        raise

    try: 
        cursor = connection.cursor()
        sql = f"DELETE FROM {table_name} WHERE rowid = {row_id};"
        cursor.execute(sql)
        connection.commit()
        print("Record has been deleted!")
    except Exception as exception:
        print("Error deleting record.")
        print(exception)
    finally:
        connection.close()


# Run the program.
def main():
    print("Welcome!")

    # Keep running until the user decides to stop. 
    running = True
    while running:
        print("1. View a table")
        print("2. Modify a table")
        print("3. Quit")
        choice = input("Select 1, 2, or 3: ")


    # Use appropriate functions based on user's choice.
        if choice == "1":
            table_name = list_tables()
            display_table(table_name)
        elif choice == "2":
            modify_table()
        elif choice == "3":
            print("Goodbye!")
            running = False
        else:
            print("Choice is not valid")

main()