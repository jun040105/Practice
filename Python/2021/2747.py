'''
a=0
b=1
x=1

for i in range(int(input())):
    if i > 1:
        a = b
        b = x
        x = a + b

print(x)
'''
'''
def fibo (n):
    if n <= 2:
        return 1

    return fibo (n-1)

x = int(input())
'''


d = [0]*(int(input()))
x = list(map(int, input().split()))

d[0] = x[0]
d[1] = max(x[0], x[1])

for i in range(2, len(d)):

    d[i] = max(x[i] + d[i-2], d[i-1])


print(d[-1])


# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

