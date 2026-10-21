
x = int(input())

for i in range (x):
    a = str(input())
    counter = 0  
    total = 0  

    for j in a:
        if j == "O":
            counter += 1
            total = total + counter
        else:
            counter = 0
    
    print(total)



