text = input("Text: ")

word_count = {}

words = text.split()


for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

max_length = max(len(word) for word in word_count.keys())

for word in sorted(word_count.keys()):
    print(f"{word:{max_length}} : {word_count[word]}")
