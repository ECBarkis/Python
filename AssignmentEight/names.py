students = [
 {'first_name':  'Michael', 'last_name' : 'Jordan'},
 {'first_name' : 'John', 'last_name' : 'Rosales'},
 {'first_name' : 'Mark', 'last_name' : 'Guillen'},
 {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def names(names):
	for name in names:
		print name['first_name'], name['last_name']

# names(students)

users = {
	'Students': [
		{'first_name':  'Michael', 'last_name' : 'Jordan'},
		{'first_name' : 'John', 'last_name' : 'Rosales'},
		{'first_name' : 'Mark', 'last_name' : 'Guillen'},
		{'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
	'Instructors': [
		{'first_name' : 'Michael', 'last_name' : 'Choi'},
		{'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}

def names(names):
	for key, data in names.items():
		print key
		count = 1
		for value in data:
			length = len(value['first_name'] + value['last_name'])
			print '{2!s} - {0} {1} - {3!s}'.format(value['first_name'], value['last_name'], count, length)
			count += 1

# names(users)