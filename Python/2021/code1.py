'''
y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
while x>0:
    y[x%10] += 1
    x = x//10

for i in y:
    print(i)
'''


'''
x = [9, 78, 27, 100, 65, 37, 1, 89]
y = [1, 1, 1, 1, 1, 1, 1, 1]

for i in range(0,8):
    for j in range(0,8):
        if x[i] < x[j]:
            y[i] += 1

print (y)
'''

'''
x = [9, 78, 27, 100, 65, 37, 1, 89]

def sort():
    y = [1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(0,8):
        for j in range(0,8):
            if x[i] < x[j]:
                y[i] += 1

    print (y)

sort()
'''

'''
x, y = input().split()

x_ = x[2] + x[1] + x[0]
y_ = y[2] + y[1] + y[0]

if int(x_) > int(y_):
    print (int(x_))
else:
    print (int(y_))
'''

'''
x, y = input().split()

if x[::-1] > y[::-1]:
    print (x[::-1])
else:
    print (y[::-1])
'''

'''
f = open("a.txt", "r")
for i in f.readlines():
    print(i.strip()) 
'''

'''
f = open("a.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)
f.close()
'''

'''
dic = {1: "apple", 2: "pineapple"}
for i in dic.keys():  
    print(dic[i])
'''

'''
class Cal: 
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2
    
    def add(self):
        return (self._num1 + self._num2)
    
    def times(self):
        return (self._num1 * self._num2)

    def sub(self):
        return (self._num1 - self._num2)
    
    def div(self):
        return (self._num1 // self._num2)

    @property
    def number1(self):
        return(self._num1)
        
    @number1.setter
    def number1(self, num1):
        self._num1 = num1
    
    @property
    def number2(self):
        return(self._num2)
        
    @number2.setter
    def number2(self, num2):
        self._num2 = num2
    
myCal = Cal(8,2)

myCal.number1 = 6

print(myCal.number1)

print(myCal.div())
'''

 


