a = int(input('enter first number'))
b = int(input('enter second number'))
n = int(input('enter the number of elements'))
print(a,b,end="")
while n-2:
    c = a+b
    a = b
    b = c
    print (c,end="")
    n = n-1