import itertools
counter = itertools.count()

class Account(object):
	newid = itertools.count(100)
	def __init__(self, owner, balance, accType):
		self.owner = owner
		self.accId = next(self.newid)
		self.balance = balance
		self.accType = accType

	def getOwner(self):
		return self.owner

	def getAccId(self):
		return self.accId

	def getBalance(self):
		return self.balance
	
	def getAccType(self):
		return self.accType

	def deposit(self, amount):
		self.balance += amount

	def withdraw(self, amount):
		self.balance -= amount

class CheckingAccount(Account):
	def __init__(self, owner, balance):
		Account.__init__(self, owner, balance, "Checking")

class SavingsAccount(Account):
	def __init__(self, owner, balance):
		Account.__init__(self, owner, balance, "Savings")

class BusinessAccount(Account):
	def __init__(self, owner, balance):
		Account.__init__(self, owner, balance, "Business")