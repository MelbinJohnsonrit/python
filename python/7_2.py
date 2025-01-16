def copy_odd_lines(source_file, destination_file):
    # Open the source file in read mode
    with open(source_file, 'r') as src:
        # Read all lines from the source file
        lines = src.readlines()

    # Open the destination file in write mode
    with open(destination_file, 'w') as dest:
        # Iterate through the lines and write the odd lines to the destination file
        for i in range(0, len(lines), 2):  # Start at 0, skip every other line
            dest.write(lines[i])

# Usage example
copy_odd_lines('source.txt', 'destination.txt')
