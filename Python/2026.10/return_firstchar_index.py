from collections import Counter

def return_firstchar_index(text):
    counts = Counter(text)

    for index, ch in enumerate(text):
        if counts[ch] == 1:
            return index

    return -1