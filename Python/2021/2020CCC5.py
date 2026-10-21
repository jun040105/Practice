M = int(input())
N = int(input())
MN = []
index = []
#index.clear()
x = 0
for i in range(M):
    MN.append(list(map(int, input().split())))

print(MN)

def FindIndex(Value):

    x = 0

    for i in range(M):
        for j in range(N):
            if MN[i][j] == Value:
                if MN.count(Value) > 1:
                    MN[i][j] = -1
                coor = (i+1) * (j+1)
                print("coor:", coor)
                x = 1
                if coor == 1:
                    return("yes")                
                else: FindIndex(coor)
        
    if x == 0:
            return("no")
  
                

print(FindIndex(M*N))



# 코드 자체에서만 
# 목표 MN[M-1][N-1]
# 시작점 MN[0][0]