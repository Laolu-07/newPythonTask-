fs = int(input('Enter first score: '))
ss = int(input('Enter second score: '))
ts = int(input('Enter third score: '))
average = (fs + ss + ts)//3
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