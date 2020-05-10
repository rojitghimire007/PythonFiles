#Tuple can not be changed 
#safer code,easy syntax use if you know the code is not going to be changed


'''assignment = (1,2,3,4,5,3,7)
print(type(assignment))
print(assignment[0])
print(assignment.count(3))
'''




'''
locations = {
	(12,14): "MAN UNITED",
	(13,13): "CHELSEA",
	(16,13): "JUVENTUS"
}

print(locations[(12,14)])
print(locations.items())
'''

#Set - unique, every time, no order (index)

'''s = {1,6,3,7}
print(6 in s)
'''

'''lis1 = [1,2,3,5,8,2,3,2,3,6,9]
s = set(lis1)
s.add(3)
a = {25,3,2,6}
a.add(101)
a.add(525)
print(a | s)
print(a & s)
print(len(s))

#Throws an error if we try to remove something thats not in set
#if dont wanna get errors, use discard instead of remove
'''

word = "rojit"
print(len({ch for ch in word if ch in "aeiou"}) != 5)


