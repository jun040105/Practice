import math

x = int(input())

a = ""

z = (int(math.log2(x)))

for i in range (z, -1, -1):
    
    if x - pow(2, i) >= 0:
        a = a+"1"
        x = x - pow(2, i)
    else: a = a+"0"

print(a)
