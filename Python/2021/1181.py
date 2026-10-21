x = []

for i in range(int(input())):
    x.append(str(input()))

x = set(x)
x = list(x)
x = sorted(x, key = lambda x: (len(x), x))

for i in x:
    print(i)
