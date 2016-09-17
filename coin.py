def cointoss():
	import random
	count = 1
	heads = 0
	tails = 0
	while count <5001: 
		random_num = random.random()
		rounded = round(random_num)
		if rounded == 1:
			heads += 1
			print 'Throwing a coin .... its a head' + 'Got' + str(heads) + ' heads so far and' + str(tails) + 'tails so far'
		else: 
			tails +=1
			print 'Throwing a coin .... its a tail' + 'Got' + str(tails) + ' tails so far and' + str(heads) + 'heads so far'
		count += 1

cointoss()

