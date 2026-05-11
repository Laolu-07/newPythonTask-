# collect input for fathers age
# collect input for sons age
# if son age * 2 < or = to fathers age
# print fathers age - sons age
# if son age*2 = fathers age, print son age * 2
# if son age * 2 > fathers age, print son age * 2 - fathers age



age_one = int(input('Enter fathers current age(1 -> 80): '))
age_two = int(input("Enter son's cureent age: "))
if (age_two * 2)< age_one:
	print('father was twice his age', age_one-(age_two*2), 'years ago')
elif(age_two * 2)== age_one:
	print('father was twice his son age', age_two*2, 'years ago')
elif(age_two * 2)> age_one:
	print('father will be twice his son age in', age_two*2-(age_one), 'more years')
