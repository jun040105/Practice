
array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(array)):
    index = i    
    for j in range(i+1, len(array)):
        if array[index] > array[j]:
            index = j
           
    array[i], array[index] = array[index], array[i]
        
print(array)
''''''

