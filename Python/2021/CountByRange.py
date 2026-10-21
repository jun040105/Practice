from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

def count_by_range(x, a, b):
    return(bisect_right(x, b) - bisect_left(x, a))

count_by_range(a, 4, 4)
count_by_range(a, -1, 3)
