# importing libs
import tkinter
import customtkinter
import time

# importing funcs
from funcs import (UserInputProcesser, DecipherText)

def ButtonPressed():
    # on button press, takes the user input from the inputTextbox and deciphers it outputing it to the outputTextbox
    
    # gets text box text
    inputText = inputTextBox.get("0.0", "end")

    # processes the text
    processedUserInput = UserInputProcesser(inputText)

    # deciphers the text
    decipheredText = DecipherText(processedUserInput)

    # outputs the decipherd text to the outputTextbox
    outputTextBox.delete("0.0", "end")
    outputTextBox.insert("0.0", text=decipheredText)


# creating and configing the window
window = customtkinter.CTk()
window.title("Morse Translator")
window.resizable(False, False)
window.columnconfigure(0, weight=1)

# creating and configing the formating explanation/input signifier label
label1 = customtkinter.CTkLabel(window, font=("Arial", 13.4), text="Type the morse code you wish to translate (Dots . and dashes -)(Formating: Seperate letters with / and words with #):")
label1.grid(row=0, column=0, padx=10, sticky="NSW")

# creating and configing the input textbox
inputTextBox = customtkinter.CTkTextbox(window, wrap="word", height=150)
inputTextBox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# creating and configing the translate button
translateButton = customtkinter.CTkButton(window, font=("Arial", 13.4), text="Translate", command=ButtonPressed)
translateButton.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

# creating and configing the output signifier label
label2 = customtkinter.CTkLabel(window, font=("Arial", 13.4), text="The translation will appear here:")
label2.grid(row=3, column=0, padx=10, sticky="NSW")

# creating and configing the outut text box
outputTextBox = customtkinter.CTkTextbox(window, wrap="word", height=150)
outputTextBox.grid(row=4, column=0, padx=10, pady=10, sticky="NSEW")

# initializing the window
window.mainloop()
