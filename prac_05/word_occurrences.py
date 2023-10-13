"""
Word Occurrences
Estimate: 10 minutes
Actual: 22 minutes
"""
word_to_frequency = {}
# text = input("Enter Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = word_to_frequency.get(word, 0)
    word_to_frequency[word] = frequency + 1
words = list(word_to_frequency.keys())
words.sort()
longest_word = max((len(word) for word in words))
for word in words:
    print(f"{word:{longest_word}} : {word_to_frequency[word]}")