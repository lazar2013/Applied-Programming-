# Import json books file: 
import json 

#Import minidom to read the books XML file: 
import xml.dom.minidom

#JSON search:
with open("books.json", "r") as f:
    data = json.load(f)

# Loop through asking the user about books until they say quit. 
print("---JSON Library Search---")
user_input = input("Enter a title of a book or type quit to exit: ")

while user_input.lower() != "quit":
    # Search for books that match the user's title.
    found = False
    for book in data["books"]:
        if book["title"].lower() == user_input.lower():
            # Show book info if found.
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Year:", book["year"])
            found = True

    # If no match is found display a not found message. 
    if found == False:
        print(user_input, "not found.")

    print()
    user_input = input("Enter a title of a book or type quit to exit: ")


# XML search:

# Parse the XML file using minidom.
domtree = xml.dom.minidom.parse("books.xml")

# Get the library.
library = domtree.documentElement

# Get all the book elements from the XML file. 
books = library.getElementsByTagName("book")

# Loop through asking the user about books until they say quit. 
print()
print("---XML Library Search---")
user_input = input("Enter a title of a book or type quit to exit: ")

while user_input.lower() != "quit":
    # Search for books that match the user's title.
    found = False
    for book in books: 
        title = book.getElementsByTagName("title")[0].childNodes[0].nodeValue
        author = book.getElementsByTagName("author")[0].childNodes[0].nodeValue
        year = book.getElementsByTagName("year")[0].childNodes[0].nodeValue

        if title.lower() == user_input.lower():
            # Show book info if found. 
            print("Title:", title)
            print("Author:", author)
            print("Year:", year)
            found = True

    # If no match is found display a not found message. 
    if found == False:
        print(user_input, "not found.")

    print()
    user_input = input("Enter a title of a book or type quit to exit: ")

print("Goodbye!")