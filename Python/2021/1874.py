stack = []
ans = []
count = 1

for i in range (int(input())):

    x = int(input())

    while count <= x:
        stack.append(count)
        ans.append("+")
        count += 1
    
    if stack[-1] == x:
        ans.append("-")
        stack.pop()
    else: 
        print("NO")
        break
    
if len(ans) == 2*(count-1):
    for i in range(len(ans)):
        print(ans[i])
    