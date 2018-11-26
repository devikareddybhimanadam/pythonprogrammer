q=int(raw_input())
p=[]
while(q>0):
    digit=q%10
    p.append(digit)
    q=q//10
print sum(p)
