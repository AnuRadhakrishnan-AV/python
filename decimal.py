# 2.Write a program named to print the decimal part.the decimal part of a number. If decimal part is zero function should return this string: "INTEGER".
a=float(input("enter a number"))
if a - int(a)!=0:
    print(a-int(a))
else:
    print("INTEGER")
