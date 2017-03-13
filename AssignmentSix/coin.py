import random

def coin_toss():
	print 'Starting the program........'
	heads = 0
	tails = 0
	for x in xrange(1,5001):
		num = round(random.random())
		if num == 1:
			heads += 1
			print 'Attempt #{0!s}: Throwing the coin... It\'s heads! ...Got {1!s} head(s) so far, and {2!s} tail(s) so far.'.format(x, heads, tails)
			pass
		else:
			tails += 1
			print 'Attempt #{0!s}: Throwing the coin... It\'s heads! ...Got {1!s} head(s) so far, and {2!s} tail(s) so far.'.format(x, heads, tails)
	print 'Ending the program..........'

coin_toss()