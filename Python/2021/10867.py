'''
x = int(input())
a = list(map(int, input().split()))
a.sort()

while len(a) > 0:

    print(a[0], end= " ")

    count = a.count(a[0])
    del a[:count]
'''

x = int(input())
a = list(map(int, input().split()))

a = sorted(list(set(a)))

for i in range(len(a)):
    print(a[i], end=" ")


    
