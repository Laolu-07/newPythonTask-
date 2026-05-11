total_bill = int(input('Enter total bill: '))
is_member = input('are you a memeber: ')
if (total_bill) >= 1000 and (is_member) == 'yes':
	print('you get a 10% discount your final amount is',total_bill -(total_bill * 10/100))
elif (total_bill) >= 1000 and (is_member) != 'yes':
	print('you get a 5% discount your final amount is',total_bill -(total_bill * 5/100))
else :
	print('No discount, your total amount is', total_bill)