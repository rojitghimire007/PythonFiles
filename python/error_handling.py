#raise ValueError ("it is my mistake")

'''
def colorize(text,color):
	colors = ("Red","blue","green")
	if type(text) is not str:
		raise ValueError("it must be a string")
	if color not in colors:
		raise Exception
	print(f"Printed {text} in {color}")

colorize("Hello", "cyan")
#colorize(34,"AWE")
'''

'''
try:
	color
except:
	print("DEFCON 20, Houston, we have a problem")

print("conference room 5 minutes")
'''

'''
try:
	num = int(input("Enter a number"))
except:
	print("Can you please not enter string")
'''


'''
def divide(a,b):
	try:
		return (a / b) 
	except (ZeroDivisionError) as err:
		print("CAN NOT DO THAT ie divide by zero")
	except:
		print("Enter integer or floats")
	finally:
		print("im here too")

print(divide(4,"kl"))
'''



'''
import pdb
first = "First"
second = "Second"
pdb.set_trace()
result = first + second 
third = "third"
result += third
print(result)
'''