n = int(input("Please enter an integer that is not negative: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    print(f"{i}! = {factorial}")

    
