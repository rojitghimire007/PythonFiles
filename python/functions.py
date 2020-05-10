'''def say_hi():
	print("Hi")
	print("hello")

say_hi()


def sing_happy_birthday():
	print("HBD TO YOU")
	print("HBD TO YOU")
	print("HBD TO YOU")
	print("HBD TO YOU")

sing_happy_birthday()
'''

'''
def square_of_seven():
	return 7*7

print(square_of_seven())
'''


'''from random import random

def coin_flip():
	r = random()
	if r > 0.5:
		return "Heads"
	else:
		return "Tails"
print(coin_flip())
'''

'''num = []
def make_noise():
	i = 1
	while i < 50:
		num.append(i)
		i+=1
	return [num for num in num if num%2==0]

print(make_noise()) 
'''


'''def make_noise():
	return [num for num in range(1,50) if num%2==0]

print(make_noise())
'''

'''def user_square(num):
	return num * num

print(user_square(5))
print(user_square(6))

'''

'''def area(l,b):
	print(l)
	print(b)
	return l * b

print(area(7,5))
'''

'''def speak(animal = "dog"):
    if animal == "pig":
    	return "oink"
    elif animal == "duck":
    	return "quack"
    elif animal == "cat":
    	return "meow"
    elif animal == "dog":
    	return "woof"
    return "?"

print(speak("banana"))
'''


'''def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')

print(speak("gsdg"))
'''

'''noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
print(set(noises))
'''

'''def exp(num=3,power=3):
	return num * power

print(exp(power = 5, num = 5))
'''
'''name = "ROJIT"
def student():
	global name
	name +=  " JORDAN"
	return name

print(student())
'''
'''dayName = {1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",
            5:"Thursday",6:"Friday",7:"Saturday"}

def return_day(num):
    if num in dayName:
        return dayName.get(num)
    return "None"
print(return_day(43))
'''

'''def single_letter_count(a, b):
	a = a.lower()
	if b in a:
		count = a.count(b)
		return count

	return 0

print(single_letter_count("Hello World", "H"))
'''
'''
word = "Rojit"
c = word.count("R")
print(c)
'''

''' def multiple_letter_count(supply):
    a = {supply[i]: supply.count(supply[i]) for i in range(0,len(supply))}
    return a 

print(multiple_letter_count("awesome"))
'''

'''word = "Rojit"
print(word[0])
print(word.count(word[2]))
'''

'''def list_manipulation(lis1,cmd,location,value):
	if cmd == "remove" and location == "end":
		a = lis1.pop(-1)
		return a
	elif cmd == "remove" and location == "beginning":
		a = lis1.pop(0)
		return a
	elif cmd == "add" and location == "beginning":
		a = lis1.insert(0,value)
		return lis1
	else:
		a = lis1.append(value)
		return lis1

print(list_manipulation([1,2,3],"add","end",101))
'''
'''a = "Rojit" [::-1]
print(a)
'''

'''
def frequency(lis1,num):
    a = lis1.count(num) 
    return a

print(frequency([1,2,3,4,4,4], 4)) # 3
print(frequency([True, False, True, True], False))
'''


'''def multiply_even_numbers(lis1):
	product = 1
	for i in range(0,len(lis1)):
		if lis1[i] % 2 == 0:
			product *= lis1[i]
	return product

'''
'''def multiply_even_numbers(lis1):
	product = 1
	lis2 = [x for x in lis1 if x %2==0 ]
	product = [product * lis2[i] for i in len(lis2)]
	return prodcut
'''

#print(multiply_even_numbers([2,3,4,5,6,2]))


'''
def capitalize(word):
    word = word[0].upper()+ word[1:len(word)]
    return word 

print(capitalize("rojit"))
'''

def compact(lis1):
	lis2 = [i for i in lis1 if i]
	return lis2


print(compact([0,1,2,"",[], False, {}, None, "All done"]) 


