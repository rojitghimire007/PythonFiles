'''
square = lambda x: x ** 2
print(square(8))
'''

#the final list or ds produced with the use of map is only for once


'''
people = ["Rojit","dsfsdf","SDfsdfs","DSfsfs"]
peeps = list(map(lambda name:name.upper(), people))
print(peeps)
#map objects are iterable
'''



'''
lis1 = [20,39,11]
decrement_list = list(map(lambda x:x-1,lis1))
print(decrement_list)
'''


'''
lis1 = ["Rojit", "Rordan", "Rarona", "Mscott"]
a = filter(lambda n:n[0] == 'R', lis1)
print(list(a))
'''
'''
def remove_negatives(lis1):
    a = filter(lambda n: n >= 0, lis1)
    return list(a)

print(remove_negatives([-1,-3,9,-7,3,0]))
'''

'''
nums = [2,26,7,19]
a = all(i % 2 ==0 for i in nums)
print(a)
'''


'''
def is_all_strings(lis1):
    b = [a for a in lis1 if type(a)==str ]
    return b
    	

print(is_all_strings([10,15,'a','e']))

'''


''' 
num1 = [12,36,9,87,5,1,2,4,78]
print(sorted(num1))

'''


# ANOTHER EXAMPLE DATA SET==================================
'''
songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31},
	{"title": "Tu hi das de", "playcount": 197989}
]

newSong = sorted(songs, key= lambda s: len(s["title"]))
print(newSong)
'''


'''
nums = [1,2,89,74,56,156]
print(max(nums))
'''


'''
names = ["Rojit", "A","pop","MscottGary"]
a= max(names, key=lambda n:len(n))
b = min(names, key=lambda n:len(n))
print(b)
'''

'''
def extremes(lis1):
	a = min(lis1)
	b = max(lis1)
	lis2 = []
	lis2.append(a)
	lis2.append(b)
	return tuple(lis2)

print(extremes([1,2,3])
'''

#.REVERSED works with any iterable object.

#print(abs(-77))

#fabs method gives absolute floating value, but we have to import it

'''
def max_magnitude(lis1):
    num = [i* (-1) for i in lis1 if i < 0]
    num = max(num)
    return num


print(max_magnitude([-5,-1,-88]))
'''

'''
def sum_even_values(*lis1):
    a = [i for i in lis1 if i%2==0]
    return sum(a)

print(sum_even_values([1,2,3,4,6]))
'''

'''
def sum_floats(*lis1):
    a = [i for i in lis1 if type(i) == float]
    return sum(a)

print(sum_floats(1,2,8,9.2,1.5,7,"rpjit"))
'''


'''
num1 = [1,2,3,4,5]
num2 = [2,4,5,6,7]
students = ["a","b","y","j"]

final = {t[0]:max(t[1], t[2]) for t in zip(students,num1,num2)}
print(final)
'''


#print(list(zip(num1,num2)))

'''
def interleave(word1,word2):
    new_word = zip(word1,word2)
    new_list = list(new_word)
    x = ["".join(c) for c in new_list]
    y = ""
    return (y.join(x))

print(interleave('aaa','zzz'))
'''

'''

def triple_and_filter(lis1):
    a = [num*3 for num in lis1 if num % 4 == 0]
    return a
print(triple_and_filter([6,8,10,12]))
'''


'''
def extract_full_name(names):
	a = [i["first"]+ "" + i["last"] for i in names]
	return a


print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}])

'''

'''
names = [{"first" : "Rojit", "last":"Ghimire"}]
capName = list(map(lambda x: x["first"].upper(),names))

print(capName)
'''

