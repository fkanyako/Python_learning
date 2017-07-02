#Creating bank account example

class Bank_account(object):
	"""docstring for Bank_account"""
	def __init__(self, account_type, amount):
		self.account_type = account_type
		self.amount = amount


	def deposit(self, deposit_amount):
		self.amount += deposit_amount


	def withdraw(self, withdraw_amout):
		self.amount -= withdraw_amout


	def __str__(self):
		return "Account type: {}, current balance: {}".format(self.account_type, self.amount)



Frank = Bank_account("Checkings", 100)
print(Frank.account_type)
print(Frank.amount)


Frank.deposit(30)
print(Frank.amount)

Frank.withdraw(45)
print(Frank.amount)
print(Frank)



