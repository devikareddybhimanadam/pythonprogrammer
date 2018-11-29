y=raw_input()
"""if all(j in '01' for f in y):
    print "yes"
else:
    print "No"
    """
if not(y.translate(None,'01')):
    print "yes"
else:
    print "No"
	
