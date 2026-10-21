'''
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range (1, len(array)):
    a = i
    for j in range (1, i+1):
        if array[a] < array[i-j]:
            array[i-j], array[a] = array[a], array[i-j]
            a -= 1
        else:
            break

print(array)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): 
        if array[j] < array[j - 1]: 
            array[j], array[j - 1] = array[j - 1], array[j]
        else: 
            break


# 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
# 한 칸씩 왼쪽으로 이동
# 자기보다 작은 데이터를 만나면 그 위치에서 멈춤