import csv

def read_specific_columns(file_name, columns):
    with open(file_name, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Extract and print the content of the specified columns
            for column in columns:
                if column in row:
                    print(f"{column}: {row[column]}")
            print('-' * 20)

# Usage example
read_specific_columns('example.csv', ['Name', 'Occupation'])
