def oddEven():
	for x in xrange(1,2001):
		if x%2 == 1:
			print 'Number is {0!s}. This is an odd number.'.format(x)
		if x % 2 == 0:
			print 'Number is {0!s}. This is an even number.'.format(x)

# oddEven()

def multiply(arg, mult):
	for x in xrange(0, len(arg)):
		arg[x] *= mult

# a = [2,4,10,16]
# multiply(a, 5)
# print a

def layered_multiply(arg):
	print arg
	new_list = []
	ones_list = []
	for x in arg:
		print x
		for y in xrange(0,x):
			ones_list.append(1)
			pass
		new_list.append(ones_list)
		ones_list = []
		pass
	return new_list

x = [2,4,5]
multiply(x, 3)
print x
a = layered_multiply(x)
print a