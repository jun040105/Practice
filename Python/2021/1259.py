x = "1"

while x != "0":
    x = str(input())
    p = 1
    
    for i in range(len(x)//2):
            if x[i] != x[-1-i]:
                p = 0

    if x != "0":
        if p == 1:
            print("yes")
        else: print("no")


