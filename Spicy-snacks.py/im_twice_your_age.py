# collect input for fathers age
# collect input for sons age
# if son age * 2 < or = to fathers age
# print fathers age - sons age
# if son age*2 = fathers age, print son age * 2
# if son age * 2 > fathers age, print son age * 2 - fathers age



father_age = int(input('Enter fathers current age(1 -> 80): '))
son_age = int(input("Enter son's cureent age: "))
if (son_age * 2)< father_age:
	print('father was twice his age', father_age-(son_age*2), 'years ago')
elif(son_age * 2)== father_age:
	print('father was twice his son age', son_age*2, 'years ago')
elif(son_age * 2)> father_age:
	print('father will be twice his son age in', son_age*2-(father_age), 'more years')
