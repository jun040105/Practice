a, b = map(int, input().split())
# target = b

x = list(map(int, input().split()))
start = min(x)
end = max(x)

def binary_search(x, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        t = 0
        for i in x:
            if i - mid > 0:
                t += i - mid

        if t == target:
            return mid
        
        elif t > target:
            start = mid + 1
        
        else:
            end = mid - 1

    return end


result = binary_search(x, b, 0, end)

print(result)