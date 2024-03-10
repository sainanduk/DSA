words = ['apple', 'banana', 'cherry', 'dragonfruit', 'berry']
long_words = list(filter(lambda word: len(word) <= 5, words))
print(long_words)