def UserInput():
    # Gets user input and processes it

    userInput = input(
        "Type the morse code you wish to translate (Dots . and dashes -)(Formating: Seperate letters with / and words with #):"
                      )
    
    # Replacing "#" with "/ /" for easier splitting
    respacedUserInput = userInput.replace("#", "/ /")
    # Spliting the string to individual letters and spaces
    processedUserInput = respacedUserInput.split("/")

    return processedUserInput