'''a = int(input())
x = []

for i in range(a):
    x.append(int(input()).split(" "))

z = sorted(x, key = lambda x : (x[1], -x[2], x[3], str(x[0])))

for i in range(a):
    print (z[i])
'''

N = int(input()) 
score_list = [] 
for i in range(N): 
    [name, kor, eng, math] = map(str, input().split()) 
    score_list.append([name, int(kor), int(eng), int(math)])

score_list.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(len(score_list)):
    print (score_list[i][0])

