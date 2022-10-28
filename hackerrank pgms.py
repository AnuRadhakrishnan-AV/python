n = int(input("enter a number").strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2<n<5:
    print("Not Weird")
elif n % 2 == 0 and 6<n<20:
    print("Weird")
elif n%2==0 and n>20:
    print("Not Wierd")
# hackerrank questions

#     n = int(input().strip())
# if (n % 2) != 0:
#     print("Weird")
# elif 2 < n <= 5:
#     print("Not Weird")
# elif 6 < n <= 20:
#     print("Weird")
# elif n > 20:
#     print("Not Weird")


