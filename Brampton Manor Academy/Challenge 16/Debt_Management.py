def validate_interest(minimum = None, maximum = None):
    try:
        interest_rate = float(input("Enter an interest rate: "))
        if minimum is not None:
            if interest_rate < minimum:
                print(f"The interest rate cannot be less than {minimum}%")
                return validate_interest(minimum, maximum)
            
        if maximum is not None:
            if interest_rate > maximum:
                print(f"The interst rate cannot be greater than {maximum}%")
                return validate_interest(minimum, maximum)
            
    except:
        print("Try again, enter a valid interest rate")
        return validate_interest(minimum, maximum)
    
    return interest_rate


def validate_repayment(minimum = None, maximum = None):
    try:
        repayment = float(input("Enter the repayment: "))
        if minimum is not None:
            if repayment < minimum:
                print(f"The repayment cannot be less than {minimum}%")
                return validate_repayment(minimum, maximum)
            
        if maximum is not None:
            if repayment > maximum:
                print(f"The repayment cannot be greater than {maximum}%")
                return validate_repayment(minimum, maximum)
    except:
        print("Try again, enter a valid repayment")
        return validate_repayment(minimum, maximum)
    
    return repayment



def values():
    interest = validate_interest(minimum = 0, maximum = 100)
    repayment = validate_repayment(minimum = 0, maximum = 100)
    print(interest, repayment)
    

if __name__ == "__main__":
    values()

