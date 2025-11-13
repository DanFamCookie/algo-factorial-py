# factorial is a number times its decending number so factorial(10) is 10*9*8*7*6*5*4*3*2*1







def factorial(num):
	result = 1
	for i in range(1, num + 1):
		result *= i
	return result
	

	
		
	pass


print(factorial(100))