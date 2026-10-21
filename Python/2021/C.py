def fac(num):
    if num == 1:
        return 1
    
    else: 
        return fac(num-1)*num

print(fac(5))

# fac(4) * 5
# fac(4) -> fac(3) * 4
# -> fac(2) * 3
# -> fac(1) * 2
# -> fac(0) * 1
# return 0

