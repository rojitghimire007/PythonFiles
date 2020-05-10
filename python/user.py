class User:

	@classmethod
	def from_string(cls,data_str):
		first,last,age = data_str.split(",")
		return cls(first,last,age)
	def __init__(self,first,last,age):
		self.first = first
		self.last = last
		self.age = age

	def full_name(self):
		return f"{self.first} {self.last}"

	def initials(self):
		a = self.first[0] + self.last[0]
		return a

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age > 65

	def birthday(self):
		self.age = self.age + 1
		return f"You grew {self.age} years old"


#user1 = User("Rojit","Ghimire",27)
#user2 = User("Sdfds","SDfsd",78)
#user3 = User("SDfs","Asfasf",17)

#print(user1.initials())
#print(user1.likes("LADIES"))

'''
print(user1.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)
'''

tom = User.from_string("Tom,Jones,89")
print(tom.first)
