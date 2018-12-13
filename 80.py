number=int(raw_input(""))
dig = []
while number > 0:
    i = number % 10
    if i & 1 != 0:
        dig.append(str(i))
    number=number/10
dig = reversed(dig)
print (" ".join(dig))
