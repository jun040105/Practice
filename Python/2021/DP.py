'''
x = [0]*1000
x[1] = 1
x[2] = 3

a = int(input())

for i in range(3, a+1):
    x[i] = x[i-2]*2 + x[i-1]


print(x[a])
'''

