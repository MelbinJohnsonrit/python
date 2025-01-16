import csv

def read_csv_file(file_name):
    with open(file_name, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Read and print each row as a list of strings
        for row in csv_reader:
            print(row)

# Usage example
read_csv_file('example.csv')
