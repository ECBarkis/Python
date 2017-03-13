import random
import math

def scores():
	print 'Scores and Grades'
	for x in xrange(0,10):
		num = math.floor((random.random() * 41)) + 60
		if num > 89:
			print 'Score: {0!s}. Your grade is A' .format(num)
		elif num > 79:
			print 'Score: {0!s}. Your grade is B' .format(num)
		elif num > 69:
			print 'Score: {0!s}. Your grade is C' .format(num)
		else:
			print 'Score: {0!s}. Your grade is D' .format(num)
	print 'End of program. Bye!'
scores()