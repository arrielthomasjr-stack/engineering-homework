vowels = "aeiou"
def count_vowels(s):
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def main():
    user_input = input("Enter a sentence: ")
    vowel_count = count_vowels(user_input)
    print(f"The number of vowels in the sentence is: {vowel_count}")

if __name__ == "__main__":
    main()


    