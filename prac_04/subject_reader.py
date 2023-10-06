"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data from a file and print results."""
    total_list = get_data()
    print_variables_from_list(total_list)


def print_variables_from_list(total_list):
    """Print variables from a list."""
    for line in total_list:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students ")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    total_list = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        total_list.append(parts)
    input_file.close()
    return total_list


main()
