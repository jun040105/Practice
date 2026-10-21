'''
x = int(input())

a = [500, 100, 50, 10]

z = 0

while x != 0:
    b[i] = x // a[i]
    x -= a[i]*(x//a[i]) 

for i in range(len(b)):
    if i == 3:
        print(z)
'''

x = int(input())

coins = [500, 100, 50, 10]
a = 0

for coin in coins:
    a += x//coin
    x = x%coin

print(a)
