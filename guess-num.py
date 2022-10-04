import random
r = random.randint (1, 10)
print(r)
#value = input('please type your number :')
#value = int(value)
while True:
	value = input('please type your number :')
	value = int(value)
	if value == r:
		print('matched')
		break
	else:
		if value > r:
			print('r is smaller')
		else:
			print('r is larger')
		print('please try again : ')




