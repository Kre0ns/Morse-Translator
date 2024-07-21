MORSE_DICT = {
    # Dict was written by chatgt
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

translationProtocol = "morseToEnglish"


def ChangeTranslationProtocol(protocolChangeRequest):
    # changes the protocol on request

    global translationProtocol

    # checks what translation protocol to change to. raises error if invalid.
    if protocolChangeRequest == "morseToEnglish" and protocolChangeRequest != translationProtocol:

        translationProtocol = protocolChangeRequest

    elif protocolChangeRequest == "englishToMorse" and protocolChangeRequest != translationProtocol:

        translationProtocol = protocolChangeRequest

    else:
        raise NameError("Invalid Protocol Change Request")


def UserInputProcesser(userInput):
    # Gets user input and processes it

    processedUserInput = ""

    # cleans out the \n that is left at the end of the string by the textbox
    cleanUserInput = userInput.replace("\n","")
    cleanUserInput = cleanUserInput.rstrip()

    # checks what translation protocol to use and processes the userInput based on that
    if translationProtocol == "morseToEnglish":

        # replaces spaces with slashes for splitting
        reslashedUserInput = cleanUserInput.replace(" ", "/")
        # where the spaces should be we have a /// so we need to replace it with a / / to keep the space
        reformatedUserInput = reslashedUserInput.replace("///", "/ /")
    
        # spliting the formated input to a list 
        processedUserInput = reformatedUserInput.split("/")

        return processedUserInput
        
    elif translationProtocol == "englishToMorse":

        # capitalizes the string
        capitalizedUserInput = cleanUserInput.upper()

        # turns the string into a list of characters
        processedUserInput = list(capitalizedUserInput)

        return processedUserInput
    
    else:

        raise ValueError("Invalid Translation Protocol")


def RetriveTranslation(request):
    # retrives the translation of the input and returns it

    translation = ""

    # checks what translation protocol to use and translates the request based on that
    if translationProtocol == "morseToEnglish":

        try:
            translation = list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(request)]

            return translation
        except:
            return "#"
        
    elif translationProtocol == "englishToMorse":

        try:
            translation = MORSE_DICT.get(request)

            return translation
        except:
            return "#"

    else:

        raise ValueError("Invalid Translation Protocol")


def TranslateText(processedUserInput):
    # Converts the morse into a string

    decipheredLetter = ""

    decipheredLetterList = []

    translatedString = ""

    for entry in processedUserInput:

        # Checks if the current entry is a space and if it is, it appends it to the decipheredLetterList
        if entry == " ":

            decipheredLetterList.append(entry)

        else:

            # requests retrival of a translation for the entry and appends it to the decipheredLetterList
            decipheredLetter = RetriveTranslation(entry)

            decipheredLetterList.append(decipheredLetter)

    # checks what translation protocol to use and prepares the string based on that
    if translationProtocol == "morseToEnglish":

        # Joins the list into a single string 
        translatedString = "".join(decipheredLetterList)

        # makes the first letter upper case and the others lower so it looks nicer
        return translatedString.capitalize()
        
    elif translationProtocol == "englishToMorse":

        # Joins the list into a single string 
        translatedString = " ".join(decipheredLetterList)

        # adds the classic morse formating for readability
        reformatedTranslatedString = translatedString.replace("   ", " / ")

        return reformatedTranslatedString