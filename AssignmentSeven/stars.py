x = [4, 'Aaron', 1, 3, 5, 'Butthead', 25]

def draw_stars(arg):
	for x in arg:
		if isinstance(x, int):
			print '*' * x
		if isinstance(x, str):
			print x[0].lower() * len(x)

draw_stars(x)