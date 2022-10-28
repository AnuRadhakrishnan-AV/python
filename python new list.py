# using for loop

list=['blue','green','red','yellow','white','black',1,2,3,True,False,True]
print(list)
for i in list:
    print(i)

# using while loop


list=['blue','green','red','yellow','white','black',1,2,3,True,False,True]
i=0
while i<len(list):
    print(list[i])
    i=i+1
new=[]

# check membership

if 'blue' in list:
    print("found")
else:
    print("not found")

 # append function

list=['blue','green','red','yellow','white','black',1,2,3,True,False,True]
list.append('blue')
print(list)
