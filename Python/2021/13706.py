x = int(input())
start = 1
end = x

def binary_search(x, start, end):
  
    for i in range(x):
        mid = ((end + start) // 2)
        if mid ** 2 > x:
            end = mid - 1
        elif mid ** 2 < x:
            start = mid + 1
        else: 
            return(mid)  

print(binary_search(x, start, end))