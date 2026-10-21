from collections import Counter

def first_unique_char(text):
    counts = Counter(text)

    for x, value in counts.items():
        if value == 1:
            return x

    return None