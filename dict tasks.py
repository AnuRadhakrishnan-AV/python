# convert two list in to dictionary

list1=[1,2]
list2=['apple','orange']
new={}
for i in range(len(list1)):
    new.update({list1[i]:list2[i]})
print(new)

# convert two dictionaries to a dictionary

d1={'name':'abc','number':1,}
d2={'fruit':'apple','price':10}
d1.update(d2)
print(d1)

# print values,access physics marks

dic={'class':{'student':{'name':'mike','marks':{'physics':70,'history':80,'maths':100}}}}
a=dic['class']['student']['marks']['physics']
print(a)



