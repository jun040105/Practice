a = 1
while a != 0:
    a, b, c = map(int, input().split())

    if a == 0: break
    if a*a + b*b == c*c or c*c + b*b == a*a or a*a + c*c == b*b:
        print("right")
    else: print("wrong")
