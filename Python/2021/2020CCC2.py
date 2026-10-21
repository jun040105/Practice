P = int(input())
N = int(input())
R = int(input())
D = 0
T = N
K = N

while T <= P:
    D += 1
    T += K*R
    K = K*R


print(D)