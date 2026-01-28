from array import *
import random

arr = array("i", [])

n = int(input("Enter element number: "))

for i in range(n):
    x = random.randrange(1, 6)
    arr.append(x)

ind = arr.index(3)

for val in arr:
    print(val, end=" ")
print("")

print(ind)
