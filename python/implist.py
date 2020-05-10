'''wow = ["Just"]
demo_list = ["ROJIT", 7 , "True", "is", "a", "king",wow,"srkhgsg" ]
print(demo_list[-1])
print(len(demo_list))

r = range(1,8)
print(list(r))'''

'''colors = ["r","g","b","p","g",7.77,True]
for i in colors:
	print(i)
'''

#If we want availability of index along with the whole list, we might want to use the while loop
#Function if attached to a list, becomes a list method in this case LIST

'''numbers = [1,2,3,4,5,6,7]
numbers.extend([9,11]) #append takes only 1 argument
i = 0

while i < len(numbers):
	print(numbers[i])
	i+=1
print(len("Rojit")) 
'''


'''friend_list = ["M","j","S","k"]
friend_list.insert(1,"Rojit")
friend_list.insert(-1,"sdgsdg")
print(friend_list)
'''

'''items = [1,2,3,4,5,"Rojit", "Ghimire"]
print(items.pop(3))
print(items.remove("Rojit"))
print(items)
print(items.count(9))
print(items.index(5))'''

'''list = [1,13,45,89,17,53,21,46,25]
list.sort()
print(list)'''

'''instructors = []
instructors.extend(["Colt","Blue","Lisa"])
print(instructors.pop(0))
print(instructors)
'''

#----SLICING-----
#IT DOESN'T hamper the original list, just a new list that is a copy of an original list
colors = ["r","b","h","p","l","k"]
'''print(colors[:])
colors2 = colors[3:]
print(colors2)
'''

'''myString = "DOOD"
newString = (myString[: :-1])
if myString == newString:
	print("PALINDROME")
else:
	print("NOT PALINDROME")
'''

'''numbers = [1,2,3,4]
numbers[0],numbers[2 = numbers[2], numbers[0]
print(numbers)
'''

'''name = "rojit"
for c in name:
	print(c.upper())
'''

'''name = "rojit"
capital_name = [c.upper() for c in name]
print(capital_name)
'''

#any number is truthy except 0

'''nums = [1,2,3,4,5,6,7]
newD = [str(num)+"Hello" for num in nums]
print(newD)

'''

'''nums = [1,2,3,4,5,6,7,8,9,10]
evens = [num for num in nums if num%2==0]
num_if = [num*2 if num%2!=0 else num for num in nums]
print(evens)
print(num_if)
'''

'''lis = ["Ellie","Tim","Mona","Rojit", "Cristiano", "Ronaldo"]

answer =  lis[2: :-1] #[a[0] for a in lis]
print(answer)
print(lis)'''

'''myS = "ROJIT"
print(myS[3::-1])
'''

'''lis1 = [1,2,3,4,7]
lis2 = [2,5,0,9]

#answer =  lis1 + lis2
#answer = [a for a in lis2 if a in (lis1 or lis2)]
print(answer)
'''

'''words = ["ellie", "tim", "matt"]
answer = [word[::-1].lower() for word in words ]
print(answer)
'''

'''numbers = [a for a in range(1,101) if a%12==0]
print(numbers)
'''

''' words = "amazing"
newWord = [a for a in words if a in "aeiou"]
print(newWord)
'''

''' nested_list = [[1,2,30], [2,3,5],[5,2,6,89]]
print(nested_list[1][0])
'''

'''nested_list = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
for loc in nested_list:
	for c in loc:
		print(c)
'''

'''board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)

'''

practice = [[num for num in range(10)] for val in range(10)]
print(practice)


''' all list at 0,
can be any type even other list
list methods / append, extend,pop,reverse
SLICES copying section of lists (From anywhere to anywhere)


