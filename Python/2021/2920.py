x = list(map(int, input().split()))
a = 0
d = 0

for i in range(7):
    if x[i] < x[i+1]:
        a = 1
    if x[i] > x[i+1]:
        d = 1

if a == 1 and d == 1:
    print("mixed")
elif a == 1:
    print("ascending")
else: print("descending")