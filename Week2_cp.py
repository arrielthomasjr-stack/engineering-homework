
# Get user-specified file
filename = input("Enter the filename to analyze: ")

word_counts = {}
vowels_count = 0
consonants_count = 0
vowels = set("aeiou")
consonants = set("bcdfghjklmnpqrstvwxyz")
total_characters = 0
total_words = 0
total_lines = 0
max_word = ""
min_word = ""
total_word_length = 0

try:
    with open(filename, "r") as f:
        lines = f.readlines()
        total_lines = len(lines)
        total_characters = sum(len(line) for line in lines)

        for line in lines:
            words = line.strip().split()
            total_words += len(words)
            for word in words:
                # Normalize: lowercase and strip punctuation
                clean_word = word.strip((".,!?;:")).lower()
                if not clean_word:
                    continue

                word_counts[clean_word] = word_counts.get(clean_word, 0) + 1

                # Count vowels and consonants per character
                for char in clean_word:
                    if char in vowels:
                        vowels_count += 1
                    elif char in consonants:
                        consonants_count += 1

                # Track longest and shortest words
                if not max_word or len(clean_word) > len(max_word):
                    max_word = clean_word
                if not min_word or len(clean_word) < len(min_word):
                    min_word = clean_word

                total_word_length += len(clean_word)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    exit()
except IOError as e:
    print(f"Error reading file: {e}")
    exit()

# Calculate average word length
average_word_length = total_word_length / total_words if total_words > 0 else 0

# Find most common word
most_common_word = max(word_counts, key=word_counts.get) if word_counts else "N/A"
most_common_count = word_counts.get(most_common_word, 0)

# Save report
with open("report.txt", "w") as f:
    f.write("===== TEXT ANALYSIS REPORT =====\n\n")

    f.write(f"Total Characters : {total_characters}\n")
    f.write(f"Total Words      : {total_words}\n")
    f.write(f"Total Lines      : {total_lines}\n\n")

    f.write(f"Most Common Word : '{most_common_word}' ({most_common_count} times)\n\n")

    f.write(f"Total Vowels     : {vowels_count}\n")
    f.write(f"Total Consonants : {consonants_count}\n\n")

    f.write(f"Longest Word     : '{max_word}' ({len(max_word)} chars)\n")
    f.write(f"Shortest Word    : '{min_word}' ({len(min_word)} chars)\n")
    f.write(f"Avg Word Length  : {average_word_length:.2f}\n\n")

    
print("Analysis complete. Report saved to report.txt")