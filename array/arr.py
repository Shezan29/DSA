from array import *

val = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# for x in val:
#     print(x, end=", ")
# print("")

# val.reverse()

val.insert(1, 777)
val.append(-99)

copyArr = array(val.typecode, (x * 3 for x in val))

for x in copyArr:
    print(x, end=", ")
