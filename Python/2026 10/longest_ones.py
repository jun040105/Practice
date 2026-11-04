'''def longest_ones(streams, k):

    token = 0
    initials = []
    series = 0 
    best = 0
    bullets = k

    for i in range(len(streams)):
        if token == 0 and streams[i] == 1:
            token += 1
            initials.append(i)
        elif token == 1 and streams[i] == 0:
            token -= 1


    for i in initials:
        for j in streams[i:len(streams)]:
            if j == 1:
                series += 1
            elif bullets > 0:
                series += 1
                bullets -= 1
            else:
                if series >= best:
                    best = series            
                series = 0

    return best
'''

def longest_ones(stream, k):
    head, tail = 0, 0
    length, best = 0, 0

    while head < len(stream):
        
        if stream[head] == 1:
            length += 1
            head += 1
            
        elif stream[head] == 0 and k != 0:
            head += 1
            length += 1
            k -= 1

        elif stream[head] == 0 and k == 0:

            if stream[tail] == 0:
                k += 1

            tail += 1
            length -= 1


        if length > best:
            best = length
        
    return best

