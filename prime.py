# Write a program to display all prime numbers within a range

start=int(input("enter the starting number"))
end=int(input("enter the ending number"))
for i in range(start,end+1):
    if i>1:
        for n in range(2,i):
            if i%n== 0:
                break
        else:
          print(i)
 # a=int(input("enter the  limit"))
# for n in range(a):
#     if n>1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)
# #

# a=int(input("enter the number"))
# for n in range(2,a+1):
#     for i in range(2,n):
#         if n%i==0:
#             print("is not a prime number")
#             break
#         else:
#             print("is a prime number")
#             break
