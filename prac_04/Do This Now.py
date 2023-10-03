# a.
names = ['James', 'Neive', 'Charlie']
user_choice = int(input(f"Enter Number, Up To {len(names)}: "))
try:
    print(names[user_choice - 1])
except IndexError:
    print("Invalid Number")

# b.
text = "This is a sentence".split()
long_words = [word for word in text if len(word) > 3]
print(long_words)
