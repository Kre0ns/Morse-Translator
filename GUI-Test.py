from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Morse Translator")

mainFrame = ttk.Frame(root, padding=10)
mainFrame.grid()

ttk.Label(mainFrame, text="Type the morse code you wish to translate (Dots . and dashes -)(Formating: Seperate letters with / and words with #):", font=30).grid(column=0, row=0, sticky=(N,S,W,E))
ttk.Entry(mainFrame, font=30).grid(column=0, row=1, sticky=(N,S,W,E))
ttk.Button(mainFrame, text="Translate").grid(column=0, row=2)
ttk.Label(mainFrame, text="Translation will apper here.", font=30).grid(column=0, row=3, sticky=(N,S,W,E))

root.mainloop()