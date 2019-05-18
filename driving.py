country = input('Which country u from')
age = input('what is your age?')
age = int(age)
if country == "Taiwan":
	if age >= 18:
		print('U can drive')
	else:
		print('U cannot drive stupid')