names_input = input ("Enter the names (seperated by commas)")
names = names_input.split(',')
count = sum (name.count ('a') for name in names)
print("Occurances of a : ",count)
