import csv

def write_dict_to_csv(file_name, data_dict):
    # Write the dictionary to a CSV file
    with open(file_name, mode='w', newline='') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)
        
        # Write the header (keys of the dictionary)
        header = data_dict.keys()
        csv_writer.writerow(header)
        
        # Write the values (rows of the dictionary)
        rows = zip(*data_dict.values())
        for row in rows:
            csv_writer.writerow(row)

def read_csv_file(file_name):
    # Read and display the content of the CSV file
    with open(file_name, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

# Example dictionary
data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Occupation': ['Engineer', 'Designer', 'Teacher']
}

# Write the dictionary to the CSV file
write_dict_to_csv('example.csv', data_dict)

# Read and display the content of the CSV file
read_csv_file('example.csv')
