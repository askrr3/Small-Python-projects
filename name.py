# students = [ 
#      {'first_name' :  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# for x in range(0,len(students)):
# 	print students[x]['first_name'] +' '+ students[x]['last_name']

users = {
 'Students': [ 
     {'first_name' :  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]

 }
for key in users:
	print key
	number = 1
	for value in users[key]:
		name = value['first_name'] + ' ' + value['last_name']
		print str(number) + " - " + name  + " - " + str(len(name)-1)


# for value in users:
# 	print users[value]


	# for x in range(0,len('Students')):
	# 	print Students[x]['first_name'] + Students[x]['last_name']
	# 	print int.len('first_name') + int.len('last_name')










