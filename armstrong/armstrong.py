num = int(input('enter the number : '))
s = 0
temp = num
while temp > 0:
    c = temp % 10
    s += c**3
    temp //= 10
if num == s:
   print ('it is Amstrong number')
else:
    print('it is not an Armstrong number')