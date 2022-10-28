
# print set,find type and length of the set
a={'apple','orange','cherry','apple'}
print(a)
print(type(a))
print(len(a))

# tuple to set
b=('apple','orange','cherry','apple')
print(set(b))

# accessing set items
a={'apple','orange','cherry','apple'}
for i in a:
    print(i)
# add new value,remove and discard item,discard function did'nt show any error
a={'apple','orange','cherry','apple'}
a.add('banana')
print(a)
a.remove('apple')
print(a)
a.discard('orange')
print(a)

# add a set to another set

a={'apple','orange','cherry','apple'}
b={1,2,3,4,5}
a.update(b)
print(a)

# add list to set
a={'apple','orange','cherry','apple'}
c=['a','b']
a.update(c)
print(a)

# join sets
# union,intersection
a={'apple','orange','cherry','apple'}
b={1,2,3,4,5}
d=a.union(b)
print(d)

# intersection,intersection_update
a={'apple','orange','cherry','apple','a'}
b={1,2,3,4,5,'a'}
d=a.intersection(b)
print(d)

# symmetric difference,symmetric difference_update
a={'apple','orange','cherry','apple','a'}
b={1,2,3,4,5,'a'}
d=a.symmetric_difference(b)
print(d)

















