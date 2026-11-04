def longest_unique(text):

    temp, best = "", ""

    for i in text:

        if i in temp:
            start = temp.index(i)
            temp = temp[start+1:]
            temp = temp + i
        else:
            temp = temp + i

        if len(temp) > len(best):
            best = temp

    return best


print(longest_unique("abcdefffgabcdegggabc"))