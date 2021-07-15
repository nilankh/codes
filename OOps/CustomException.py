class ZeroDenominatorError(ZeroDivisionError):
	pass
while True:
	try:
		n = input('Enter the numerator :')
		num = int(n)
		n = input('Enter the denominator :')
		denom = int(n)
		if denom == 0:
			raise ZeroDenominatorError('Denominator should not be zero')
		value = num/denom
		print(value)
		break
	except ValueError:
		print("Numerator and Denominator should be integers")
	except ZeroDenominatorError:
		print("ZeroDenominatorError is raised")
	except ZeroDivisionError:
		print("Division by zero is not allowed")
	

	
