country = input('Which country u from')
age = input('what is your age?')
age = int(age)
if country == "Taiwan":
	if age >= 18:
		print('U can drive')
	else:
		print('U cannot drive stupid')
elif country == 'USA':
	if age >= 16:
		print('U can have the license')
	else:
		print(' Fuck u not yet get license')
