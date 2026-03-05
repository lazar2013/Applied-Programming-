# Open the names.txt file. 
file = open("names.txt", "r")

names_list = []

for line in file: 
    name = line.strip()
    names_list.append(name)

file.close()

# Ask the user for a name.
user_name = input("Enter a name or type 'exit' to quit").strip()

while user_name != "exit":
    if user_name in names_list:
        print("The string '"+ user_name +"' is already in the file.")

    else:
            output_file = open("nofound.txt", "a")
            output_file.write(user_name + "\n")
            output_file.close()
            print ("The string '" + user_name +"' has been written to nofound.txt.")
            
    user_name = input("Enter a name or type 'exit' to quit").strip()