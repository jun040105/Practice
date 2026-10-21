M = int(input())
N = int(input())
K = int(input())
a = []
b = []
g = 0
Rc = 0
Mc = 0

for i in range(K):
    a.append(input())

a.sort()

for i in range(len(set(a))):
    count = a.count(a[0])
    if count % 2 == 1:
        b.append(a[0])
    del a[:count]

for i in range(len(b)):
    c = b[i]
    if c[0] == "R":
        g += N
        Rc += 1
    else: 
        g += M
        Mc += 1
    
print(g - Rc*Mc*2)




