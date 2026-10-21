from collections import Counter

def first_unique_char_index(text):
    counts = Counter(text)

    for x, value in counts.items():
        if value == 1:
            return x

    return None

def char_location(text, x):
    for n, k in enumerate(text):
        if k == x:
            return n

    return -1