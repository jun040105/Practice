x = int(input())
c = 0

if x % 5 == 0:
    c = x // 5 
    x = 0

else:
    while x % 5 != 0 and x > 0:
        x -= 3
        c += 1

if x % 5 == 0:
    c = c + x//5
    print(c)

else: print(-1)

