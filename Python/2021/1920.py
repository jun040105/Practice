
a = int(input())
x = list(map(int, input().split()))
x.sort()

b = int(input())
y = list(map(int, input().split()))

def binary_search(array, target, start, end):
    # array = x
    # target = i
    # start = 0 
    # end = len(x) - 1
    while start <= end:
        mid = (end + start)//2

        if array[mid] == target:
            return(1)
        
        elif array[mid] > target:
            end = mid - 1
        
        else: 
            start = mid + 1
    return(0)

for i in y:
    print(binary_search(x, i, 0, a-1))

