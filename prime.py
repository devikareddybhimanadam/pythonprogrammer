num=int(raw_input(""))
if num > 1:
  for i in range(2,num):
      if(num % i)==0:
	print("is not a prime number")
	break
else:
	print("is a prime number")
