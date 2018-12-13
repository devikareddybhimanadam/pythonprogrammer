def do_stuff(input):
	i, j = [int(i) for i in input.split(" ")]
	print(j-i)
		

while True:
  try:
    value = raw_input()
    do_stuff(value.rstrip()) 
  except (EOFError):
    break 
