while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except EOFError:
        break
