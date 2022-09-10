def wordInput():
    word= input("Enter a word: ")
    return word

def checkUpper(word):
    return word.isupper()

if __name__ == "__main__":
    word = wordInput()
    check = checkUpper(word)
    print(check)
