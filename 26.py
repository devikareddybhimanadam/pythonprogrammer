num = int(raw_input())
list=[int(i) for i in raw_input().split()]
list.sort()
print" ".join(map(str,list))
