#https://www.codewars.com/kata/56cd44e1aa4ac7879200010b

def wordInput():
    word = input("Enter: ")
    return word

def is_uppercase(word):
    return word.upper()== word

if __name__ == "__main__":
    word = wordInput()
    upper = is_uppercase(word)
    print(upper)
