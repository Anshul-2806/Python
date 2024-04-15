'''num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)'''

a = int(input("Please Enter the First value: "))
b = int(input("Please Enter the First value: "))
c = int(input("Please Enter the First value: "))

if (a > b and a > c):
          print("{0} is Greater Than both {1} and {2}". format(a, b, c))
elif (b > a and b > c):
          print("{0} is Greater Than both {1} and {2}". format(b, a, c))
elif (c > a and c > b):
          print("{0} is Greater Than both {1} and {2}". format(c, a, b))
else:
          print("Any two values are equals OR All the three values are equal")