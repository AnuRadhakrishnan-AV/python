# 2.write a program to check the last digit of the user entered number is divisible by 3 or not.?

a=int(input("enter a number"))
a=a%10
if(a%3):
    print("this number is divisible by 3")
else:
    print("this number is not divisible by 3")

