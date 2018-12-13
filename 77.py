number=int(raw_input(""))
cou=0
if number>0:
    for f in range(1,number+1):
        if number%f==0:
            print f,
