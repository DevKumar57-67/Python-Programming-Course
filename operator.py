#using operator in code


import operator
num1 = int(input("Enter an integer"))
num2 = int(input("Enter an integer"))

sum=operator.add(num1,num2)
sub=operator.sub(num1,num2)
mul=operator.mul(num1,num2)


print("The sum is ",sum)
print("The sub is ",sub)
print("The prod is",mul)
