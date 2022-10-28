x=lambda a:a*10
print(x(2))

n1=lambda a,b:a+b
print(n1(2,3))

# lambda function
def function(n):
    return lambda a:a*n
result=function(5)
print(result(10))
# a*a
def function():
    return lambda a:a*a
r=function()
print(r(20))