import json
# give single quote to a dictionary for json
x='{"name":"abc","age":10,"city":"chennai"}'
# parsing
y=json.loads(x)
print(y['name'])
# convert python to json
a={"name":"abc","age":10,"city":"chennai"}
y1=json.dumps(a)
print(y1)
y2=json.loads(y1)
print(y2['age'])
print(json.dumps(['apple','banana','orange']))


