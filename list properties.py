# how to append list

colors=['blue','green','red','yellow','white','black']
new=[]
for x in colors:
    if 'e' in x:
        new.append(x)
print(new)

 # how to sort a list

colors=['blue','green','red','yellow','white','black']
colors.sort()
print(colors)

 # how to sort reverse order

colors=['blue','green','red','yellow','white','black']
colors.sort(reverse=True)
print(colors)

# numbers reverse

numbers=[1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
print(numbers)

# str reverse

thelist=['apple','banana','cherry','orange']
thelist.reverse()
print(thelist)

# how to copy a list

colors=['blue','green','red','yellow','white','black',1,2,3,True,False,True]
newlist=colors.copy()
print(newlist)

# how to join two list n1+n2  reverse n2+n1

colors=['blue','green','red','yellow','white','black',1,2,3,True,False,True]
thelist=['apple','banana','cherry','orange']
joinlist=thelist+colors
print(joinlist)

