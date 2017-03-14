import re
words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

def get_matching_v(words):
	matches = []
	for word in words:
		if re.search(r'v',word):
			matches.append(word)
	return matches

# print get_matching_v(words)

def get_matching_ss(words):
	matches = []
	for word in words:
		if re.search(r'ss',word):
			matches.append(word)
	return matches

# print get_matching_ss(words)

def get_matching_e(words):
	matches = []
	for word in words:
		if re.search(r'e$',word):
			matches.append(word)
	return matches

# print get_matching_e(words)

def get_matching_b(words):
	matches = []
	for word in words:
		if re.search(r'b.b',word):
			matches.append(word)
	return matches

# print get_matching_b(words)

def get_matching_bb(words):
	matches = []
	for word in words:
		if re.search(r'b*b',word):
			matches.append(word)
	return matches

# print get_matching_bb(words)

def get_matching_vowel(words):
	matches = []
	for word in words:
		if re.search(r'a.e.i.o*u',word):
			matches.append(word)
	return matches

# print get_matching_vowel(words)

def get_matching_reg(words):
	matches = []
	for word in words:
		if re.search(r'',word):
			matches.append(word)
	return matches

# print get_matching_reg(words)

def get_matching_double(words):
	matches = []
	for word in words:
		if re.search(r'[a-z]{2}',word):
			matches.append(word)
	return matches

print get_matching_double(words)