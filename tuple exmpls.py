
#1. Python program to Find the size of a Tuple

tuple1=('apple','orange','cherry','banana')
print(len(tuple1))

#2. Python – Maximum and Minimum K elements in Tuple

number=(1,2,3,4,1,2,3,1,1,1)
max_num=max(number)
min_num=min(number)
print(max_num)
print(min_num)

#3.Create a list of tuples from given list having number and its cube in each tuple
a=(1,2,3,4,5,6)
for i in a:
    print(i*i*i)

#4. Python – Adding Tuple to List and vice – versa

list1=['apple','orange','cherry','banana']
tuple1=(1,2,3,4,1,2,3,1,1,1)
tuple2=list(tuple1)
add=list1+tuple2
add1=tuple2+list1
print(add)
print(add1)

#5. Python – Sum of tuple elements

tuple1=(1,2,3,4,1,2,3,1,1,1)
sum=0
for x in tuple1:
    sum=sum+x
print(sum)

# Python – Modulo of tuple elements
numbers=(1,2,3,4,5,6,7,8)

# Python – Row-wise element Addition in Tuple Matrix





# Python – Update each element in tuple list
tuple1=('apple','orange','cherry','banana')
t1=list(tuple1)
t1[0:len(t1)]='a1','a2','a3','a4'
t2=tuple(t1)
print(t2)

# Python – Remove Tuples of Length K

t1=[(1,2,3),('apple','banana','orange','cherry'),(1,2,3,4,5,6),(1,2,3,4,5,6),('a1','b1'),('a','b'),(1,2),('a','b'),(1,2),('c','d')]
a=int(input("enter length"))
res=[]
for i in t1:
  if len(i) !=a:
      res.append(i)
print(res)

# # Python – Join Tuples if similar initial element
# a1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
# a2=list(a1)
# res=[]
# for x in a2:
#     if res and res[-1][0] == x[0]:
#         res[-1].append(x[1:])
#     else:
#         res.append([ele for ele in x])
#         res = list(map(tuple, res))
#         print(res)



# perm=permutations([1,2])
# for i in list(perm):
#     print(i)








# Python – Remove Tuples from the List having every element as None

t1=[('apple','orange','banana','cherry'),(1,2,3),('a1','a2'),(None),(None)]
res=[]
for i in t1:
    if i!=None:
        res.append(i)
print(res)

# Python – All pair combinations of 2 tuples

list1=[1,2]
list2=[2,3]
res=[(x,y) for x in list1 for y in list2]
res=res+[(x,y) for x in list2 for y in list1]
print(res)

from itertools import permutations
list=[1,2]
perm=permutations(list,3)
print(perm)
res=[]
for i in perm:
    res.append(i)
    print(res)





































































































