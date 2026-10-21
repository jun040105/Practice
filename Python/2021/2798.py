x = list(map(int, input().split()))
y = list(map(int, input().split()))
t = x[1]

for i in range(x[0]-2):
    for j in range(i+1, x[0]-1):
        for k in range(j+1, x[0]):
            if x[1] - y[i] - y[j] - y[k] < t and x[1] - y[i] - y[j] - y[k] >= 0 :
                t = x[1] - y[i] - y[j] - y[k]
                a =  y[i] + y[j] + y[k]

print(a)