x = input()
y = input()

l = len(y)
flag = 0

for i in range(l):
    y = y[-1] + y[:l-1]
    print(y)
    if y in x:
        flag = 1
        break

if flag == 0:
    print("no")
else: print("yes")