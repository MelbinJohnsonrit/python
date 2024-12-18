def add(a, b):
	return a + b
def subtract(a, b):
	return a - b
def multiply(a, b):
	return a * b
def divide(a, b):
	if b != 0:
		return a / b
	else:
		return "Division by zero is not allowed"
while True:
	print("\nMenu: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide \n5. Exit")
	choice = input("\nEnter your choice: ")
	if choice == '5':
                print("Exiting the calculator.")
                break
	num1 = float(input("\nEnter first number: "))
	num2 = float(input("Enter second number: "))
	if choice == '1':
		print(f"The result is: {add(num1, num2)}")
		continue
	elif choice == '2':
		print(f"The result is: {subtract(num1, num2)}")
		continue
	elif choice == '3':
		print(f"The result is: {multiply(num1, num2)}")
		continue
	elif choice == '4':
		print(f"The result is: {divide(num1, num2)}")
		continue
	else:
		print("Invalid choice. Please select a valid option.")
		continue
