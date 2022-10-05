def find_factors_products():
    num = int(input("Enter an integer greather than 1: "))
    product = 1
    factor = 0

    while product < num:
        factor = factor + 1
        product = product * factor
        
    if num == product:
        product = 1
        for i in range (1,factor+1):
            product = product * i
            print(i)
    else:
        print("No results")


if __name__ == '__main__':
    find_factors_products()
    
