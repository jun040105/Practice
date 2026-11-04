def merge_list(the_list):

    the_dict = {}

    for start, end in the_list:

        for i in range(start, end+1):
            the_dict.update({i: 1})

    the_dict = sorted(the_dict)
        
    merged = [] 
    parts = [0, -2]

    for i in the_dict:
        if parts[1] == i-1:
            parts[1] = i
        else:
            if parts[1] != -2:
                merged.append(parts.copy())
            parts[0] = i
            parts[1] = i

        if i == the_dict[len(the_dict)-1]:
            merged.append(parts)

    return merged


print(merge_list([[1, 3], [2, 6], [8, 10], [9, 12]]))