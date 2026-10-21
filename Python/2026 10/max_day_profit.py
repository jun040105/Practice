import math

def max_profit(prices):
  min = math.inf
  total = 0
  
  for i in prices:
    if total < i - min:
        total = i - min
    if min > i:
        min = i

  return total

print(max_profit([7, 1, 5, 3, 6, 4]))