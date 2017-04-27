beers = 5
covers = 0
bottles = 0
total = 0
while beers > 0:
	print 'drinking %d beers'% beers
	total += beers
	covers += beers
	bottles += beers
	beers = 0
	
	beers = (covers + 2*bottles)/4
	covers = (covers + 2*bottles)%4
	bottles = 0
	print 'exchange %d beers'% beers

print 'You have drunk %d beers...'% total
	
