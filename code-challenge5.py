number = eval(input("Enter any number --> "))
factorial = 1
for s in range(number, 0, -1):
    factorial *= s
print("The factorial of ",number," is",factorial)