"""output = lambda a,b:f"{a}x{b}={a*b}"
print(output(10,20))
#odd or even using the lambda function
saajan = lambda a:f"{a} is even" if a%2==0 else f"{a} is odd"
print(saajan(10))
#Smallest of 3 numbers
smallest = lambda a,b,c: a if a<b and a<c else b if b<a and b<c else c
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print(smallest(a,b,c))"""
#Cubing numbers from 1-10 using lambda function
cubing = lambda a:f"{a}**3 = {a**3}"
for i in range(1,11):
    print(cubing(i))

