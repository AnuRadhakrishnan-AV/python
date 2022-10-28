# find type and length of tuple

tuple1=('apple','orange','cherry','banana')
print(type(tuple1))
print(len(tuple1))

# access second largest item

number=[1,2,3,4,1,2,3,1,1,1]
number.sort()
print(number[-2])

# convert tuple to list and change items

tuple1=('apple','orange','cherry','banana')
y=list(tuple1)
y[0]='kiwi'
print(y)

# convert tuple to list and append new element

tuple1=('apple','orange','cherry','banana')
y=list(tuple1)
y.append('hello')
print(y)


# append new list

tuple1=('apple','orange','cherry','banana')
y=('abc',)
tuple1 += y
print(tuple1)

# remove tuple

tuple1=('apple','orange','cherry','banana')
y=list(tuple1)
y.remove('apple')
print(y)

# use for loop

tuple1=('apple','orange','cherry','banana')
for i in tuple1:
    print(i)
#
# # # use while loop
# tuple1=('apple','orange','cherry','banana')
# i=tuple1[0]
# while i<(tuple1[3]):
#     print(i)


# print tuple in multiply times

a=(1,2,3,4,5)
b=a*3
print(b)

# join tuples
n1=(1,2,3,4)
n2=(5,6,7,8)
n3=n1+n2
print(n3)



# TUPLE METHODS

# 1.count functions

number=(1,2,3,4,1,2,3,1,1,1)
print(number.count(1))





































