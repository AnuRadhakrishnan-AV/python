# 1.Python program to interchange first and last elements in a list

list=['apple','kiwi','orange','banana','cherry','gua','grapes']
list[0]='a1'
list[-1]='a2'
print(list)

#2. Python program to swap two elements in a list

list=['apple','kiwi','orange','banana','cherry','gua','grapes']
temp=list[0]
list[0]=list[1]
list[1]=temp
print(list)

#3.Python – Swap elements in String list


# 4.Maximum of two numbers in Python

number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
max_number=max(number)
print(max_number)


# 5.Minimum of two numbers in Python


number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
min_number=min(number)
print(min_number)

#6.Python | Reversing a List

list=['apple','kiwi','orange','banana','cherry','gua','grapes']
list.reverse()
print(list)

#7. Python | Count occurrences of an element in a list

list=['apple','kiwi','orange','banana','cherry','gua','grapes','apple','orange','apple']
count=list.count('apple')
print(count)

#8.Python Program to find sum and average of List in Python

number=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
sum =0
for i in range(1,len(number)):
    sum=sum+i
print(sum)
avg=0
for i in range(1,len(number)):
    avg=sum/len(number)
print(avg)


#9. Python | Sum of number digits in List

number=[10,11,12,13,14,15,16,17,18,19,20]
res=[]
for i in number:
    sum=0
    for digit in str(i):
        sum+=int(digit)
    res.append(sum)
print(res)

# #10 Python | Multiply all numbers in the list

number=[10,11,12,13,14,15,16,17,18,19,20]
mul=1
for x in number:
    mul=mul * x
print(mul)

#11 Python program to find smallest number in a list

number=[10,11,12,13,14,15,16,17,18,19,20]
min_number=min(number)
print(min_number)

#12 Python program to find largest number in a list


number=[10,11,12,13,14,15,16,17,18,19,20]
max_number=max(number)
print(max_number)

#13 Python program to find second largest number in a list


number=[10,11,12,13,14,15,16,17,18,19,20]
number.sort()
print(number[-2])

#14 Python program to print even numbers in a list

number=[10,11,12,13,14,15,16,17,18,19,20]
print("even numbers")
for x in number:
    if x % 2==0:
        print(x)

#15  Python program to print odd numbers in a List

number=[10,11,12,13,14,15,16,17,18,19,20]
print("odd numbers")
for x in number:
    if x % 2!=0:
        print(x)

#16. Python program to print all even numbers in a range

number=[10,11,12,13,14,15,16,17,18,19,20]
print("even")
for x in range(number[0],number[6]):
    if x % 2==0:
        print(x)

#17. Python program to print all odd numbers in a range

number=[10,11,12,13,14,15,16,17,18,19,20]
print("odd")
for x in range(number[0],number[6]):
    if x % 2!=0:
        print(x)

#18. Python program to count Even and Odd numbers in a List

number=[10,11,12,13,14,15,16,17,18,19,20]
even_count=0
odd_count=0
for x in number:
    if x % 2 ==0:
        even_count += 1
    else:
      odd_count += 1
print("even cont",even_count)
print("odd count",odd_count)

#19. Python program to print positive numbers in a list

number=[-5,-4,-3,-2,-1,1,2,3,4,5]
for x in number:
    if x>0:
        print("positive numbers",x)

#20. Python program to print negative numbers in a list


number=[-5,-4,-3,-2,-1,1,2,3,4,5]
for x in number:
    if x<0:
        print("negative numbers",x)

#21. Python program to print all positive numbers in a range

numbers=[-5,-4,-3,-2,-1,1,2,3,4,5,-6,-7,-8]
for num in range(number[0],number[8]):
    if num>0:
        print("positive",num)

#22. Python program to print all negative numbers in a range

numbers=[-5,-4,-3,-2,-1,1,2,3,4,5,-6,-7,-8]
for num in range(numbers[1], numbers[9]):
    if num < 0:
        print("negative",num)

#23.Python program to count positive and negative numbers in a list
numbers=[-5,-4,-3,-2,-1,1,2,3,4,5,-6,-7,-8]
positive_count=0
negative_count=0
for x in numbers:
    if x>0:
        positive_count += 1
    else:
      negative_count += 1
print("positive cont",positive_count)
print("negative count",negative_count)
#
# # Remove multiple elements from a list in Python
list=[1,2,3,4,5,6]
del list[1:4]
# print(*list1)













































