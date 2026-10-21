word = input().upper()
mySet = list(set(word))
cnt = []
for i in mySet:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(mySet[cnt.index(max(cnt))])

