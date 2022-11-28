import numpy as np

def ISBN_input():
    ISBN = input("Enter the ISBN: ")
    return ISBN

def calc_total(ISBN):
    count = 10
    X = 10
    total = 0
    for i in range(0, 10):
        if ISBN[i] == "X":
            total += count * 10
        elif ISBN[i] == "?":
            total += count * 0
        else:
            total += count * int(ISBN[i])
        count -= 1
    return total

def check_valid(total):
    if (total % 11) == 0:
        print("Valid ISBN")
    else:
        print("Invalid ISBN")

def find_question_mark(ISBN, total):
    value = np.ceil(total/11)
    correct_total = value * 11
    return correct_total

if __name__ == "__main__":
    ISBN = ISBN_input()
    total = calc_total(ISBN)
    print(total)
    correct_total = find_question_mark(ISBN, total)
    print(correct_total)

    # 15688?111X gives total 226, correct total is 231