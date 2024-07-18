import tkinter
import customtkinter

window = customtkinter.CTk()
window.title("Morse Translator")
window.resizable(False, False)
window.columnconfigure(0, weight=1)

label1 = customtkinter.CTkLabel(window, font=("Arial", 13.4), text="Type the morse code you wish to translate (Dots . and dashes -)(Formating: Seperate letters with / and words with #):")
label1.grid(row=0, column=0, padx=10, sticky="NSW")

inputTextBox = customtkinter.CTkTextbox(window, wrap="word", height=150)
inputTextBox.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

translateButton = customtkinter.CTkButton(window, font=("Arial", 13.4), text="Translate")
translateButton.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

label1 = customtkinter.CTkLabel(window, font=("Arial", 13.4), text="The translation will appear here:")
label1.grid(row=3, column=0, padx=10, sticky="NSW")

outputTextBox = customtkinter.CTkTextbox(window, wrap="word", height=150)
outputTextBox.grid(row=4, column=0, padx=10, pady=10, sticky="NSEW")

window.mainloop()