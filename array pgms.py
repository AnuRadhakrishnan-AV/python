# find the minimum and maximum element of the array

array1=[1,2,3,4,5]
print(max(array1))
print(min(array1))


# arr[]={1,5,3,2}
# Give a random set of numbers, print them in sorted order

array={1,5,3,2}
b=list(array)
a=sorted(b)
print(a)

# write a program to reverse the array
arr1=[2,5,6,9]
arr1.reverse()
print(arr1)

# create three arrays and find the common element in these array
array1=[2,5,8,9,4]
array2=[3,2,6,7,8]
array3=[5,5,9,2,9]
set1=set(array1)
set2=set(array2)
set3=set(array3)
n1=set1.intersection(set2, set3)
print(n1)

# using for loop
array1=[2,5,8,9,4]
array2=[3,2,6,7,8]
array3=[5,5,9,2,9]
for i in array1:
    if i in array2 and i in array3:
        print(i)

# find the factorial of a number using array














