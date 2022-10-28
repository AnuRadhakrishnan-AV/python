# add three numbers without using function
a=2
b=3
c=1
print('sum=',a+b+c)

# functions: to add 3 numbers

sum=0
def add(a,b,c):
    sum=a+b+c
    print('sum of 3 numbers:',sum)

n1=int(input("enter first number"))
n2=int(input("enter second number"))
n3=int(input("enter third number"))
add(n1,n2,n3)

# write a program to find factorial of a number,using recursion
# using function with for loop

def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of the number is:",fact)


n1=int(input("enter a number"))
fac(n1)
# using while loop

def factorial(n1):
    if n1 < 0:
        print("0")
    elif n1==0 or n1==1:
        print("1")
    else:
        fact=1
        while(n1>1):
            fact=fact*n1
            n1=n1-1
        print("factorial of the number is:",fact)

a1=int(input("enter a number"))
factorial(a1)

# write a program to make a simple calculator,using recursion
sum=0
def add(a,b):
    sum=a+b
    print("sum of the numbers:",sum)
sub=0
def minus(a, b):
    sub=a-b
    print("sub of the numbers:", sub)
mul=0
def multiply(a, b):
    mul=a*b
    print("product of the numbers:", mul)
div=0
def division(a,b):
    div=a/b
    print("division of the numbers:",div)


n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
print("1.add\n2.minus\n3.multiply\n4.division")
choice=int(input("enter your selection"))
if choice==1:
    add(n1,n2)
elif choice==2:
    minus(n1,n2)
elif choice==3:
    multiply(n1,n2)
elif choice==4:
    division(n1,n2)
else:
    print("invalid")












