'''
#Adds in the tuple
def sum_all_nums(*lik):
	total = 0
	for i in lik:
		total += i
	return total

print(sum_all_nums(7,5))
'''

'''def favColor(**ourFamily):
	print(ourFamily)

favColor(Rojit = "purple", Jordan = "green",Myboo ="blue")


purple in ourFamily

'''

'''
def combine_words(word, **givenWord):
    if prefix in givenWord:
        return givenWord[v]+ word
    elif suffix in givenWord:
        return givenWord[v] + word
    return givenWord
print(combine_words("child", prefix ="man"))
'''

'''
def display_info(a,b,*args,student = "Rojit", **kwargs):
	return[a,b,args,student,kwargs]\

print(display_info(1,2,3,last_name ="Ghimire",job ="king"))
'''
# * For tuple unpacking
# makes the entire list or tuple as individual arguments of the function

# ** FOR disctionary unpacking


'''
def aam(a,b,c):
	return a + b *c

num = {"a":1,"b":3,"c":7}
print(aam(**num))
'''


