student={'name':'anu','roll_no':1,'age':18,'marks':30}
fruits={'color':'red','price':10,'quantity':1,'names':'apple'}
student.update(fruits)
print(student)


# lists
a=[1,2,3]
b=['apple','orange','banana']
a.append(b)
print(a)
# list to dict using for loop
a=[1,2,3]
b=['apple','orange','banana']
res={}
for i in range(len(a)):
    res.update({a[i]:b[i]})
print(res)

# qns

# multiple
a=[1,2,3]
for i in a:
    print(i*i*i)

#add tuple to list and vice versa

list1=[1,2,3]
list2=(4,5,6)
list3=list(list2)
print(list1+list3)

a=['hello','apple','orange']
for i in a:
    print(i)

#     a
for i in range(100,200,5):
    print(i)



# function


def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of the number is:",fact)


n1=int(input("enter a number"))
fac(n1)









