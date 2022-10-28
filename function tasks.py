# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# def num():
#     for i in range(2000,3200):
#         if i%7==0 and i%5!=0:
#             print(i,end=",")
#
# num()

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
# that is an integral number between 1 and n (both included). and then the program should print the
#  di4ctionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def dictionaries(a):
    n2={}
    for i in range(1,n1+1):
        n2.update({i:i*i})
    print(n2)

n1=int(input("enter a number"))
dictionaries(n1)

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)

n1=int(input("enter a number"))
fac(n1)
# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

x=input("numbers")
def numbers():
    a1=[]
    a2=[]
    a1.append(x)
    a2.append(x)
    print(list(a1))
    print(tuple(a2))

numbers()


# Write a program that accepts a sentence and calculate the number of upper
# case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

x=str(input("enter the sentence:"))
def num(x):
    n1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','X','Y','Z']
    n2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count1=0
    count2=0
    for i in x:
        if i in n1:
            count1=count1+1
    for i in x:
        if i in n2:
            count2=count2+1
    print("upper case:",count1)
    print("lower case:",count2)

num(x)

# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as
# following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# def amount():
#     deposit=[]
#     withdrawl=[]
#     total=0
#     while True:
#         D = int(input("Deposit amount :"))
#         W = int(input("withdrawing amount:"))
#         deposit.append(D)
#         withdrawl.append(W)
#         total=sum(deposit) - sum(withdrawl)
#         print(total)
#
# amount()





#     write a program that tests the compatibility between two peaple.(Love Calculator)To work out the love score between two peaple:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs
# 2. Then check for the number of times the letters in the word LOVE occurs.Then combine these numbers to make a two digit number
# *For Love Scores less than 10 or greater than 90, the messages should be :"Your score is **x**,you go together like coke and mentos."
# *For Love Scores between 40 and 50, the message should be :"Your score is **y**,you are alright together."
# Otherwise, the message will just be their score.e.g.:Your Score is **z**."
# EXPL:
# name1="Angela Yu" name2="Jack Bauer"
# T occurs 0 times R occurs 1 time
# U occurs 2 times E occurs 2 times Total=5
# L occurs 1 time o occurs 0 times V occurs o times E occurs 2 times Total=3
# Love score=53

def calc():
    name1=str(input("enter the first name"))
    name2=str(input("enter second name"))
    word1=['t','r','u','e','T','R','U','E']
    word2=['l','o','v','e','L','O','V','E']
    count1=0
    count2=0
    for i in name1:
        if i in word1:
            count1=count1+1

    for i in name2:
        if i in word1:
            count1 = count1 + 1

    for i in name1:
        if i in word2:
            count2 = count2 + 1

    for i in name2:
        if i in word2:
            count2 = count2 + 1
    total = int((str(count1)) + (str(count2)))
    if total <10 or total >90:
        print("Your score is ", total,  "you go together like coke and mentos.")
    if total >40 and total >50 :
        print("Your score is",total,"you are alright together.")
    else:
        print("Your Score is",total)

calc()






