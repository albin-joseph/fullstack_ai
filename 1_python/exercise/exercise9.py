# word frequnecy

def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text = "hello world hello"
result = word_frequency(text)
print(result)