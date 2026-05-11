weight = int(input('Enter weight: '))
height = float(input('Enter height: '))
bmi_procedure = height*weight
bmi = weight/bmi_procedure
if (bmi) < 18.5:
	print('Underweight')
elif (bmi) <= 24.9:
	print('Nomal')
elif (bmi) <= 29.9:
	print('Overweight')
elif (bmi) >= 30:
	print('Obese')
print(bmi)