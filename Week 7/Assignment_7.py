def escape(character):
    # Use # to treat a digit like a character.
    if character.isdigit():
        return "#" + character
    # Use ## to treat # like a regular character.
    if character == "#":
        return "##"
    return character

def rle_encode(text):
    output = "##00" # Indicate the sequence is encoded.
    last = "" # Keeps track of previous character.
    count = 0 # Counts how many times a character repeats.

    # Loop through each character in the input.
    for character in text:
        if character == last: # Check if the character is the same as the last one.
            count += 1
        else:
            if last != "":
                # If character only appears once, do not add a number next to it. 
                if count == 1:
                    output = output + last

                # If character appears more than once, add the number next to it. 
                else: 
                    output = output + last + str(count)

            last = character # Update to new character. 
            count = 1 # Reset count for new character. 

    if count == 1:
        output = output + last 
    else: 
        output = output + last + str(count)

    return output

def rle_decode(text):
    text = text[4:] # Remove ##00
    output = ""
    last = ""
    escape = False

    for character in text: 
        if escape:
            output += character
            last = character
            escape = False # Normal decoding if no # present.
        elif character == "#":
            escape = True # Next character is literal.

        # Check if the character is a number.
        elif character.isdigit():
            number = int(character)
            count = 0

            # Repeat the last letter as many times as the number.
            while count < number:
                output += last
                count += 1
        
        else:
            output += character # If it's a letter, add it one time.
            last = character # Remember the letter in case it's followed by a number. 

    return output

def main():
    text = input("Enter alphabetic characters only:")

    # Make sure the input is not blank. 
    while text == "":
        print("Make sure to only use alphabetic characters!")
        text = input("Enter alphabetic characters only:")

    # If only letters, encode. 
    if text.isalpha():
        encode = rle_encode(text)
        print("Encoded:", encode)
    # If there are numbers decode and repeat the letter that many times.
    else:
        decode = rle_decode(text)
        print("Decoded:", decode)

main()