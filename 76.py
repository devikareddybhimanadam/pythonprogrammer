number=int(raw_input(""))
cou=0
if number>1:
    for e in range(2,number):
        if number%e==0:
            cou=cou+1
if cou>1:
    print "yes"
else:
    print "no"
