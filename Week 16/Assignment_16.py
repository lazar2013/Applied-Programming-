import tkinter
import random 

# Main window set up:
window = tkinter.Tk()
window.title("Coin Flip")
window.geometry("350x400")

# Possible coin flip results:
# random.choice() will pick one of these each time the button is pressed. 
outcomes = ("Heads", "Tails")

# Graphics for each outcome:
graphic = {
    "Heads": "🌞",
    "Tails": "🌑"
}

# Function to do a coin flip each time the button is clicked:
def flip_coin():
    result = random.choice(outcomes)
    graphic_label["text"] = graphic[result]
    result_label["text"] = result

# Window Layout:
title_label = tkinter.Label(window, text="Coin Flip Generator", font=("Arial Bold", 24), bg="white", fg="blue")
title_label.grid(row=0, column=0, pady=16)

# Instructions for the player:
instruction_label = tkinter.Label(window, text="Click The 'Flip Coin' Button!", font=("Arial", 12))
instruction_label.grid(row=1, column=0, pady=6)

# Starting graphic - using Earth instead of a coin and updates to sun(heads) or moon(tails) with each flip:
graphic_label = tkinter.Label(window, text="🌎", font=("Arial", 80))
graphic_label.grid(row=2, column=0, pady=10)

# Show results after each flip:
result_label = tkinter.Label(window, text="", font=("Arial Bold", 22))
result_label.grid(row=3, column=0, pady=6)

# Flip Coin Button:
flip_button = tkinter.Button(window, text="Flip Coin", font=("Arial Bold",14), bg="blue", fg="white")
flip_button["command"] = flip_coin
flip_button.grid(row=4, column=0, pady=16)

window.mainloop()