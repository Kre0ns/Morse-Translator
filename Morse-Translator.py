# Dict was written by chatgpt
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
    }

def UserInput():
    # Gets user input and processes it

    userInput = input(
        "Type the morse code you wish to translate (Dots . and dashes -)(Formating: Seperate letters with / and words with #):"
                      )
    
    # Replacing "#" with "/ /" for easier splitting
    respacedUserInput = userInput.replace("#", "/ /")
    # Spliting the string to individual letters and spaces
    processedUserInput = respacedUserInput.split("/")

    # Debug: print(processedUserInput)
    return processedUserInput


def DecipherMorse(morseCode):
    # Converts the morse into a string

    decipheredLetterList = []

    decipheredString = ""

    for entry in morseCode:

        # Checks if the current entry is a space and if it is, it appends it to the decipheredLetterList
        if entry == " ":

            decipheredLetterList.append(entry)

        else:

            # Checks the MORSE_DICT for the translation of a morse string and appends it to the decipheredLetterList
            decipheredLetter = list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(entry)]
            decipheredLetterList.append(decipheredLetter)

    #Joins the list into a single string (decipheredString)
    decipheredString = "".join(decipheredLetterList)

    # Debug: print(decipheredString)
    return decipheredString
