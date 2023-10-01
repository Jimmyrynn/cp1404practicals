# a.
out_file = open("names.txt", "w")
user_name = input("Enter Name: ")
print(user_name, file=out_file)
out_file.close()

# b.
in_file = open("names.txt", "r")
name = in_file.read()
in_file.close()
print("Your name is", name)

# c.
in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(f"Total of first two lines: {number_1 + number_2} ")

# d.
running_total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    running_total += number
in_file.close()
print(f"Total: {running_total} ")
