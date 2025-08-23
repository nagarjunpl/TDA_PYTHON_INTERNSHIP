# Word Frequency Counter
sentence = "python is easy and python is powerful"
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)

print(freq.keys()) # prints the keys of the dictionary
print(freq.values()) # prints the values of the dictionary
print(freq.items()) # prints the key-value pairs of the dictionary
print(freq.get("python")) # prints the value of the key "python"
print(freq.get("python", 0)) # prints the value of the key "python" if it exists, otherwise prints 0


