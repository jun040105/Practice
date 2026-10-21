N = int(input())

x = 1
y = 1

command = list(map(str, input().split()))

for i in command:

    if i == "L":
        if x != 1:
            x -= 1
    elif i == "R":
        if x != N: 
            x += 1
    elif i == "U":
        if y != 1:
            y -= 1
    elif i == "D":
        if y != N:
            y += 1

print(x, y)