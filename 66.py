t=int(raw_input())
if t>1:
    for j in range(2,t):
        if t%j==0:
    	    print "no"
            break
    else:
            print "yes"
