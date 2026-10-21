'''
x, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

t = 0

for i in range(k):
    if min(A) < max(B):
        A[A.index(min(A))], B[B.index(max(B))] = B[B.index(max(B))], A[A.index(min(A))]
    else: break

for i in A:
    t += i

print(t)
'''

x, k = map(int, input().split())

A = list(map(int, input().split()))
A.sort()
B = list(map(int, input().split()))
B.sort(reverse= True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: break

print(sum(A))

