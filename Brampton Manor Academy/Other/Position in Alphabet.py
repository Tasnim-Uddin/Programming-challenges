def letterInput():
    letter = input("Enter a letter: ")
    return letter

def alphabetPosition(letter):
    position = ord(letter.lower())-96
    return position

def findOrdinalIndicator(position):
    if position == 1:
        ordinalIndicator = "st"
    elif position == 2:
        ordinalIndicator = "nd"
    elif position == 3:
        ordinalIndicator = "rd"
    else:
        ordinalIndicator = "th"
    return ordinalIndicator
    

if __name__ == "__main__":
    letter = letterInput()
    position = alphabetPosition(letter)
    ordinalIndicator = findOrdinalIndicator(position)
    print(f"The letter {letter} is {position}{ordinalIndicator} in the alphabet.")




