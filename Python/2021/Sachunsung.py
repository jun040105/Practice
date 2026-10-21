'''
s = int(input())
ans = []

l = (input()[1:-1])
l = sorted(l.split(","))
a = []


while len(l) > 0:
    x = l.count(min(l))
    if int(min(l)) <= s:
        a.append([int(min(l)), x/len(l)])
    else: a.append([s, 0])
    l = l[x:]


for i in range(len(a)):
    for j in range (len(a)-1):
        if a[j][1] < a[j+1][1]:
            a[j], a[j+1] = a[j+1], a[j]

for i in range(len(a)):
    ans.append(a[i][0])

print(ans)
'''

'''
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    
    a =[]
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        x = stages.count(i)
        answer.append(i)
        if length == 0:
            a.append(0)
        else: a.append(x/length)
        length = length-x
    
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] < a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                answer[j], answer[j+1] = answer[j+1], answer[j]

    return answer

print(solution(N, stages))
'''
'''
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):

    c = []
    f = []
    a = []
    answer = []
    t = len(stages)

    for i in range (1, N+1):
        c.append(stages.count(i))

    for i in range (N):   
        f.append(c[i]/t)
        t -= c[i]

    print(f)
    a = sorted(f, reverse =True)

    for i in range(N):
        answer.append(f.index(a[i]) + 1)
        f[f.index(a[i])] = 2

    return(answer)

print(solution(N, stages))
'''

N = 5	
stages = [2, 1, 2, 6, 2, 4, 3, 3]
def soltion(N, stages):
    result = {} #[1, 2, 3, 4]
                #[0.2, 0.3, 0.4, 0]
                # {"준형":"jun", "세진":"sj"} result["세진"] = "sj"
    denominator = len(stages)

    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage]= 0 # result[4] = 0

    return sorted(result, key= lambda x : -result[x])

print(soltion(N, stages))
