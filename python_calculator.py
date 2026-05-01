# Simple Calculator in Python

# Take input from the user
num1= float(input("enter number 1:"))
num2= float(input("enter number 2:"))

#input operator from user
operator = input("enter operator(+,-,*,/):")

#now calculator perfomimg
if operator=="+":
  print("Result", num1 + num2)
elif operator == "-":
   print("Result",num1 - num2)
elif operator =="*":
    print("Result", num1 * num2)
elif operator == "/":
    print("Result",num1 / num2)
elif num2== 0:
    print("error: devision waith zzero not allowed")

#invalid eroor
else:
   print("invalid operator error")
