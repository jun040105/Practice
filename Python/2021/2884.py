a = str(input())
x, y = a.split(" ")

x = int(x)
y = int(y)

if y < 45:
    y = 60 - (45 - y)
    if x == 0:
        x = 23
    else: 
        x = x-1
else: 
    y = y - 45

print (x, y)
