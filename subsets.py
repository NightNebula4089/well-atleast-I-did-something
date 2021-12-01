import numpy
import math
array = []
x = 0
while x == 0:
    l = int(input("enter the array/enter 69 to end this process"))
    if l == 69:
      x = x+1
    array.append(l)
    print(array)


sequence = []
y = 0
while y == 0:
    z = int(input("enter the sequence/enter 69 to end this process"))
    if z == 69:
      y = y+1
    sequence.append(z)
    print(sequence)

boolean = 0
for i in range(0, len(sequence)-1):
    if array.index((sequence[i])) < array.index((sequence[i+1])):
        boolean = boolean +1
    if boolean == len(sequence)-1:
        print(True)





