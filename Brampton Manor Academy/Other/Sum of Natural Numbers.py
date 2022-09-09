def numInput():
    n = int(input("Enter the last natural number in the sequence: "))
    return n

def bruteForce(n):
    total = 0
    for i in range (0,n+1):
        total = total + i
        i = i + 1
    print(f"The sum is {total}")

def formula(n):
    total = (((n**2)+n)/2)
    print(f"The sum is {total}")

def approachType():
    approach = input("Brute force or formula: ")
    if approach == "brute force":
        bruteForce(n)
    elif approach == "formula":
        formula(n)

if __name__ == "__main__":
    n = numInput()
    approachType()



            
