#Trial5
from ecc import FieldElement
from ecc import Point 
prime=223
a = FieldElement(0,prime)
b = FieldElement(7, prime)
x = FieldElement(15, prime)
y = FieldElement(86, prime)
# p = Point(x,y,a,b)
# print(7*p)
i = 3
num = 5
result = 0
while i:
    if i & 1:
        result+= num
    num+=num
    i >>= 1
print(result)    