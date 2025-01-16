# Open the file in read mode
with open('filename.txt', 'r') as file:
    # Read lines into a list
    lines = file.readlines()

# Print the list
for line in lines:
	print(line)
