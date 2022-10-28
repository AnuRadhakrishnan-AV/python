student={'name':'abc','roll_no':1,'mark':[10,20,30]}
print(student)
print(type(student))
print(len(student))
# accessing dict items

student={'name':'abc','roll_no':1,'mark':[10,20,30]}
print(student['name'])
print(student['mark'])

# accessing using get method

student={'name':'abc','roll_no':1,'mark':[10,20,30]}
print(student.get('mark'))

# accessing keys

print(student.keys())

# add a record
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
student['age']=12
print(student)

# access values
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
print(student.values())

# access items
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
print(student.items())
# change values
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
student['mark']=[50,60,70]
print(student)

# update function
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
student.update({'roll_no':2})
print(student)

# pop method to remove
student={'name':'abc','roll_no':1,'mark':[10,20,30]}
student.pop('name')
print(student)
student.popitem()
print(student)
# using delete method

student={'name':'abc','roll_no':1,'mark':[10,20,30]}
del student['roll_no']
print(student)

# for loop in dict

d1={'fruits':'apple','number':1,'color':'red','price':10}
for i in d1:
    print(d1[i])
# using function

d1 = {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
for i in d1.keys():
    print(i)

# using function
d1 = {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
for i,j in d1.items():
    print(i,j)

# copy method
d1 = {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
new=d1.copy()
print(new)

# dict method
d1 = {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
new1=dict()
print(new1)

# nested dictionaries

dic= {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}, {'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10},{'fruits': 'apple', 'number': 1, 'color': 'red', 'price': 10}
print(dic)











