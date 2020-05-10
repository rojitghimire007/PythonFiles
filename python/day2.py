#HOW TO OPERATE THE CLI IN POWERSHELL 101

#cd One and then press tab

#cd desktop

#cd python
#python and then filenanme

#print("What is you favorite number?")
#answer = input()
#answer = int(answer)
#if answer%2 == 0:
	#print(f"THANK you for choosing integer value. I like {answer} too!!")
#else:
#	print("you dumbfuck")


#print("How old are you madame?")
#age = input()
#if age:

#	age = int(age)
#	if (age >= 18) and (age < 21):
#		print("Here is your wristband")
#	elif age >= 21:
#		print("Welcome to the party!!")
#	else:
#		print("Go to your home, kiddo")
#else:
#	print("Enter a number, will u?")

#print("Enter first number: ")
#x = input()
#x = int(x)
#print("Enter second number: ")
#y = input()
#y=int(y)
#if (x > 0) and (y > 0):
 #   print("both positive")
#elif (x <0) and (y<0):
 #   print("both negative")
#elif (x <0) and (y>0):
 #   print("x is n and y is pegative")
#else:
 #   print("y is n and x is p")


print("Are you actually sick")
actuallySick = input()
actuallySick = bool(actuallySick)
print("KINDA sick?")
kindaSick = input()
kindaSick = bool(kindaSick)
print("Hate your job")
hatejob = input()
hatejob = bool(hatejob)
print("Enter your sick days remaining")
sickday=input()
sickday = int(sickday)
if actuallySick == 'True' and kindaSick== 'False'and hatejob== 'False' and sickday < 10:
	print("Have your day off")
elif actuallySick == 'False' and (kindaSick == "True" and hatejob == "True") and sickday < 10:
	print("You can have your day off")
else:
	print("Get your ass here")