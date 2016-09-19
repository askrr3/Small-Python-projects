count = 1
while count < 11:
	var = int(raw_input("enter score:"))
	# if var == "quit": break
	if var >= 90 and var <=100:
		print str(var) +' '+ "your grade is A"
	elif var >= 80 and var <=90:
		print str(var) +' '+ "your grade is B"
	elif var >= 70 and var <=80:
		print str(var) +' '+ "your grade is C"
	elif var >= 60 and var <=70:
		print str(var) +' '+ "your grade is D"
	count +=1
