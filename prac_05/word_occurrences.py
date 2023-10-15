"""
Estimate: 10 minutes
Actual: 22 minutes
"""
word_to_frequency = {}
# text = input("Enter Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
for word in text.split():
    word_to_frequency[word] = word_to_frequency.get(word, 0) + 1
words = list(word_to_frequency.keys())
words.sort()
maximum_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{maximum_length}} : {word_to_frequency[word]}")
