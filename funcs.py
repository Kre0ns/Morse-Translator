# Dict was written by chatgpt
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', 
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}

def UserInputProcesser(userInput):
    # Gets user input and processes it

    # cleans out the \n that is left at the end of the string by the textbox
    cleanUserInput = userInput.replace("\n","")
    # replaces spaces with slashes for splitting
    reslashedUserInput = cleanUserInput.replace(" ", "/")
    # where the spaces should be we have a /// so we need to replace it with a / / to keep the space
    reformatedUserInput = reslashedUserInput.replace("///", "/ /")
    
    # spliting the formated input to a list 
    splitUserInput = reformatedUserInput.split("/")

    return splitUserInput


def DecipherText(morseCode):
    # Converts the morse into a string

    decipheredLetterList = []

    decipheredString = ""

    for entry in morseCode:

        # Checks if the current entry is a space and if it is, it appends it to the decipheredLetterList
        if entry == " ":

            decipheredLetterList.append(entry)

        else:

            # Checks the MORSE_DICT for the translation of a morse string and appends it to the decipheredLetterList
            try:
                decipheredLetter = list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(entry)]
            except:
                print("The entered text isnt valid")
            decipheredLetterList.append(decipheredLetter)

    #Joins the list into a single string (decipheredString)
    decipheredString = "".join(decipheredLetterList)

    return decipheredString
