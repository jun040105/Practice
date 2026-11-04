def is_palindrome(text):
    if text == "":
        return True

    start, end = 0, len(text)-1

    while start < end:
        if text[start] == text[end]:
            start += 1
            end -= 1
        else:
            return False

    return True