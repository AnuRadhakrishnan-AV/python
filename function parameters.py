def name(a,b,c):
    print("younger child is :",a)

name(a='ram',b='tom',c='sita')

# arbitory keyword-**
def child(**args):
    print("name is:",args['lname'])

child(name='tom',lname='cruise',age=20,city='chennai')

# default parameter
def my_function(country="Norway"):
    print("i am from"+country)

my_function()
my_function('India')

# passing list as arguments

def foodlist(a):
    for x in a:
        print(x)

list=['a','b','c','d']
foodlist(list)

# write a program to find lcm of a number using function
def lcmof_num(n1,n2):
    if(n1>n2):
        largest=n1
    else:
        largest=n2
    value=largest
    while(True):
        if(largest%n1==0 and largest%n2==0):
            print("lcm of the numbers:",largest)
            break
        else:
            largest=largest+value


n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
lcmof_num(n1,n2)

# assign a differend name to a function
def function():
    print("hii")

name=function
name()

# generate a python list of all the even numbers b/w 9 to 14

def even_no(a):
    for i in range(9,14):
        if i%2==0:
            print(i)

n1=[]
even_no(n1)













