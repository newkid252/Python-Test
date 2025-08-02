# 5.Calculate the factorial of a number using a loop

num=eval(input("Enter a Number: "))
factorial=1

if num<0:
    print("Error! Please enter a positive number")
else:
    for i in range(1, num+1):
        factorial *= i
    print("Factorial: ", factorial, sep='')