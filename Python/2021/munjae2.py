from bisect import bisect_left, bisect_right

x, a = map(int, input().split())
z = list(map(int, input().split()))

def count_by_range(z, a, b):
    return(bisect_right(z, b) - bisect_left(z, a))

if count_by_range(z, a, a) == 0:
    print(-1)
else: print(count_by_range(z, a, a))
