import math
d,e=map(int,raw_input("").split())
b=d * e
if math.sqrt(b).is_integer():
    print "yes"
else:
    print "no"
