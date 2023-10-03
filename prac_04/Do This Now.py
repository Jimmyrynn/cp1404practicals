# a.
# names = ['James', 'Neive', 'Charlie']
# user_choice = int(input(f"Enter Number, Up To {len(names)}: "))
# try:
#     print(names[user_choice - 1])
# except IndexError:
#     print("Invalid Number")

# b.
# text = "This is a sentence".split()
# long_words = [word for word in text if len(word) > 3]
# print(long_words)

# c.
def main():
    """Program that takes query string and returns list of tuples."""
    string = "?name=Bob&age=99&day=Wed"
    pairs = extract_pairs(string)
    print(pairs)


def extract_pairs(string):
    """Extract name-value pairs as tuples in a list from a query string."""
    pairs = []
    parts = string[1:].split('&')
    for part in parts:
        pair = part.split('=')
        try:
            pair[1] = int(pair[1])
        except ValueError:
            pass
        pairs.append(tuple(pair))

        # try:
        #     pairs.append(tuple((pair[0], int(pair[1]))))
        # except ValueError:
    return pairs


main()
