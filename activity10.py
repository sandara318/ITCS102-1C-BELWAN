from getpass import getpass

username = 'darabels'
pword = 'ikawlang'

u = input("USERNAME --> ")
p = input("PASSWORD --> ")

if (u == username) and (p == pword) :
	print("Access Granted")
else:
	print("Access Denied")