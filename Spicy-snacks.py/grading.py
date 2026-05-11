first = int(input('Enter first score: '))
second = int(input('Enter second score: '))
third = int(input('Enter third score: '))
average = (first + second + third)//3
if (average)>= 90:
	print(average,'A')
elif(average)>= 80:
	print(average,'B')
elif(average)>= 70:
	print(average,'C')
elif(average)>= 60:
	print(average,'D')
elif(average)< 59:
	print(average,'F')
