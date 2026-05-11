password = input('Enter password: ')
len(password)
if (len(password))== 1:
	print('Invalid password')
elif(len(password))<= 6:
	print('Password strength => Weak')
elif(len(password))<= 10:
	print('Password strength => Medium')
elif(len(password))> 10:
	print('Password strength => Strong')