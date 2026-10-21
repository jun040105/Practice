x = input().split("-")
z = []

for i in range (len(x)):
    y = x[i].split("+")
    z.append(0)
    for j in range (len(y)):
        z[i] += int(y[j])
    
for i in range (len(z)):
    if i == 0:
        t = z[i]
    else: t -= z[i]

print(t)
