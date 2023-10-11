# a.
def main():
    names = ['brett', 'kate', 'james', 'neive', 'charlie']
    ages = [50, 46, 20, 17, 15]
    oldest_age = find_oldest(names, ages)
    print(oldest_age)


def find_oldest(names, ages):
    # return names[ages.index(max(ages))] // Option 1
    oldest_age = -1
    oldest_index = -1
    for i, age in enumerate(ages):
        if age > oldest_age:
            oldest_age = age
            oldest_index = i
    return names[oldest_index]


main()

# b.
name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
# for name in name_to_age: // Option 1
#     print(f"{name} is {name_to_age[name]:2}")

for name, age in name_to_age.items():
    print(f"{name} is {age}")

# c.
name_to_age = {"Bill": 21, "Jane": 34, "Sven": 56}
new_name = input("Enter Name: ")
new_age = int(input("Enter Age: "))
name_to_age[new_name] = new_age
max_length = max(len(name) for name in list(name_to_age.keys()))
for name, age in name_to_age.items():
    print(f"{name:{max_length}} - {age:5}")
