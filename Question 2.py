# 2.To swap two variables using a temporary variable

a=eval(input("Enter the 1st Number: "))
b=eval(input("Enter the 2nd Number: "))

temp=a
a=b
b=temp

print("a=",a, sep='')
print("b=",b, sep='')