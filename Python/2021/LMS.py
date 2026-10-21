x = list(input())
count = 0

for i in range(len(x)):
    min = x[i]
    index = i
    for j in range(i+1, len(x)):
        if min >= x[j]:
            min = x[j]
            index = j
    if min != x[i]:
        x[i], x[index] = x[index], x[i]
        count += 1
        
print(count)
        

        


