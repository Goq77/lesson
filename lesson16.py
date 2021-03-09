# thisdict = {'name':'Aram','year':'1994'}
# thisdict['year'] = 2014
# thisdict['age'] = 88
# print(thisdict)

# person = dict(name='Aram', age=12)

# if 'email' in person:
# 	person['email'] = 'g@gmail.com'
# else:
# 	person['email'] = 'g@gmail.com'
# print(person)

# students = {
# 	'anna': 5,
# 	'anjela': 4,
# 	'aram': 10
# }

# count = 0
# for i in students.values():
# 	count += i
# print(count/len(students))

# for i,j in students.items():
# 	print(i,j)

# c = input('pakagic: ').split(' ')
# if c.count('(') == c.count(')'):
# 	print('ok')
# else:
# 	print('no')



# char = input('char: ')
# count = 0

# for i in char:
# 	if i == '(':
# 		count += 1
# 	elif i == ')':
# 		count -= 1
# 	if count == -1:
# 		print('no')
# 		break
# else:
# 	if count == 0:
# 		print('ok')
# 	else:
# 		print('no')


# name = input('name: ').title()
# my_dict = {
# 	'name1': 'Aram',
# 	'name2': 'Vzgo',
# 	'name3': 'Ani'
# }

# if name in my_dict.values():
# 	print("ok")
# else:
# 	print('no')


# my_dict = {
# 	'name1': 'Aram',
# 	'name2': 'Vzgo',
# 	'name3': 'Ani'
# }
# if 'name2' in my_dict:
# 	del my_dict['name2']
# print(my_dict)


#EX1
students = {
	'anna': 5,
	'anjela': 4,
	'aram': 10
}

sortedList=sorted(students.values())
print(sortedList)

#EX2
students = {
	'anna': 5,
	'anjela': 4,
	'aram': 10
}
students['Vazgo'] = 55
print(students)

#EX3
mydict = {'a':1,'b':2,'c':12}
key = 'a'
if key in mydict:
	print('key exists')
else:
	print('NOt exists')

#EX4
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
dict1.update(dict2)
print(dict1) 

#EX5
mydict = {'a':1,'b':2,'c':12}
c = 1
for i in mydict:    
    c = c * mydict[i]
print(c)

#EX6

c = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}

a = sorted(c.values())[-3:][::-1]

n = {}

for j in a:
	for i in c:
		if j == c[i]:
			n[i] = j
print(n)

#git
print("status")