import random
r = random.randint (1, 10)
print(r)
count = 0
while True:
	count = count + 1
	value = input('please type your number :')
	value = int(value)
	if value == r:
		print('matched')
		print('you have tried', count, 'time')
		break
	else:
		if value > r:
			print('r is smaller')
		else:
			print('r is larger')
	print('you have tried', count, 'time')


