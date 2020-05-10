class BankAccount:

	allowed = ["Darcy","Rebecca"]
	def __init__(self, owner,balance=0):
		if owner not in BankAccount.allowed:
			raise ValueError(f"You can't have an account {owner}")

			self.owner = owner
			self.balance = balance

	def deposit(self,num):
		self.balance = num + self.balance
		return self.balance

	def withdraw(self, num):
		self.balance = self.balance - num
		return self.balance

acct = BankAccount("Darcy")
acct1 = BankAccount("Usher")
print(acct.owner)
acct.deposit(10)
print(acct.balance)
acct.withdraw(3)
print(acct.balance)