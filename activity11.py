temp = eval(input("Enter Temperature outside --> "))

#input 40
if temp >=1 and temp <= 20:
	print("Temperature is Considered as Extremly Cold")
if temp >=21 and temp <= 31:
	print("Temperature is Considered as Moderately Cold")
if temp >=34 and temp <= 37:
	print("Temperature is Considered as Lukewarm")
if temp >=38 and temp <= 45:
	print("Temperature is Considered as Hot")
if temp >=46 and temp <= 54:
	print("Temperature is Considered as Boiling Hot")
if temp >=55 and temp <= 62:
	print("Temperature is Considered as Dangerous Temperature")

else:
	print("Invalid Temperature")


