def answerInput():
    answer = int(input("*YOU* --> This will be the answer. Select a number between 1-49: "))
    while not 1 <= answer <= 49:
        answer = int(input("*YOU* --> This will be the answer. Select a number between 1-49: "))
    return answer

def factorCalculate(answer):
    factor = 99 - answer
    return factor

def friendInput():
    friendInputNum = int(input("*PLAYER* --> Pick any number between 50-99: "))
    while not 50 <= friendInputNum <= 99:
        friendInputNum = int(input("*PLAYER* --> Pick any number between 50-99: "))
    return friendInputNum

def friendNum(friendInputNum,factor):
    friendMainNum = friendInputNum + factor
    return friendMainNum

def friendNumCalculation(friendMainNum):
    convertedNum = friendMainNum - 99
    return convertedNum

def result(friendInputNum,convertedNum):
    friendResult = friendInputNum - convertedNum
    return friendResult


if __name__ == "__main__":
    
    print(f"We are going to play a game. I want you to pick a number then do a series of calculations."
          f"I bet I know what the result of those calculations will be!")

    answer = answerInput()
    friendInputNum = friendInput()
    factor = factorCalculate(answer)
    friendMainNum = friendNum(friendInputNum,factor)
    convertedNum = friendNumCalculation(friendMainNum)
    friendResult = result(friendInputNum,convertedNum)

    print(f"I said the answer was {answer} and the calculation result is {friendResult}")

          
    
