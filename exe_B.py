# Given a text file (e.g., a short paragraph), read it, split it into words (strip punctuation), and print the 5 most common words with their counts. Hint: use a dictionary.

word_counts = {}

with open("get.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        words = line.strip().split()
        for word in words:
            word = word.strip(".,!?;:")
            word_counts[word] = word_counts.get(word, 0) + 1

# Print the 5 most common words with their counts
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{word}: {count}")
