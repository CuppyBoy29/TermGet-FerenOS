import os
import time
import sys

if len(sys.argv) == 2:
	if sys.argv[1] == "apt-get":
		package = "apt-get"
	elif sys.argv[1] == "pip":
		package = "pip"
else:
	package = "apt-get"
	
def clear():
	os.system("clear")
	#Runs 'clear' over shell to clear the screen.
	
print("Welcome to TermGet for Feren OS")
time.sleep(1)
clear()
#Sets the variable 'setup' to False
	
while True: #Starts a loop
	clear()
	print("Please choose an action\n\n1. Search for packages\n2. Install an application\n3. Remove an application\n4. Update all packages\n5. Update Repo\n6. Clean\n7. Credits\n8. Exit")
	user = input() #Asks for user input
	
	if user == "1": #Search
		clear()
		user = input("Please enter search query: ")
		print(" ")
		if package == "apt-get":
			os.system("sudo apt-cache search " + user)
		input("\nPress enter to continue")
		
	if user == "2": #Install
		clear()
		user = input("Please enter which package(s) to install: ")
		print("")
		
		if package == "apt-get":
			os.system("sudo apt-get install " + user)
			
		input("\nPress enter to continue")
		
	if user == "3": #Remove
		clear()
		user = input("Please enter which package(s) to remove: ")
		print("")
		if package == "apt-get":
			user1 = input("How will you like to remove the package?\n\n1. remove, removes just the package (faster)\n2. purge, removes the package, and all it's configuration files (saves space)")
			clear()
			if user1 == "1":
				os.system("sudo apt-get remove " + user)
			if user1 == "2":
				os.system("sudo apt-get purge " + user)
				
		input("\nPress enter to continue")
		
	if user == "4": #Updates Packages
		clear()
		print("\n")
		if package == "apt-get":
			os.system("sudo apt-get upgrade")
			os.system("sudo apt-get dist-upgrade")
			
		input("\nPress enter to continue")
		
	if user == "5": #Updates Repo
		clear()
		print("\n")
		if package == "apt-get":
			os.system("sudo apt-get update")
			
		input("\nPress enter to continue")
		
	if user == "6": #Cleans
	
		clear()
		
		if package == "apt-get":
			os.system("sudo apt-get autoremove")
			os.system("sudo apt-get clean")
			
		input("\nPress enter to continue")
		
	if user == "7": #Credits
		print("TermGet was created by:\n- PizzaLovingNerd (main developer)\n- SudoLinux\n- The Feren OS Developer")
		time.sleep(3)
		#If you contribute, please add your name.
		
	if user == "8": #Quit
		quit()

