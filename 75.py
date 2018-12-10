number=raw_input("")
h=len(number)
string=list(number)
if h%2==0:
    k=h/2 - 1
    string[k]='*'
    string[k+1]='*'
else:
    k=h/2 - 1
    string[k+1]='*'
print "".join(string)
