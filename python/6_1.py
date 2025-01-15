class bankaccount:
	def __init__(self,name,account_number,account_type,balance):
		self.name=name
		self.account_number=account_number
		self.account_type=account_type
		self.balance=balance

	def deposit(self,amount):
		self.balance+=amount
		print("deposit amount is",amount,"new balance is ",self.balance)
	def withdraw(self,amount):
		if(amount>self.balance):
			print("insufficient balance")
		else:
			self.balance-=amount
			print("withdraw amount is ",amount,"new balance is ",self.balance)
	def display(self):
		print(self.name)
		print(self.account_number)
		print(self.account_type)
		print(self.balance)

print("enter account detail to enter")
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
account_type = input("Enter account type (Savings/Current): ")
balance = float(input("Enter initial balance: "))

account=bankaccount(name,account_number,account_type,balance)

account.display()
while True:
	print("\nChoose an operation:")
	print("1. Deposit")
	print("2. Withdraw")
	print("3. Display Account Details")
	print("4. Exit")
	choice = input("Enter your choice: ")
	if choice == "1":
		amount = float(input("Enter deposit amount: "))
		account.deposit(amount)
	elif choice == "2":
		amount = float(input("Enter withdrawal amount: "))
		account.withdraw(amount)
	elif choice == "3":
		account.display()
	elif choice == "4":
		print("Exiting the program.")
		break
	else:
		print("Invalid choice. Please try again.")
