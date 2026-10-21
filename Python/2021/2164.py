x = []

for i in range(1, int(input())+1):
    x.append(i)

for i in range(len(x)-1):

    x = x[1:]
    x.append(x[0])

    del x[0]

print(x)