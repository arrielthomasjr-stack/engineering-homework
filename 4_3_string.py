# Convert a decimal number to binary, octal, and hex
def convert_decimal():
    decnum_input = input("\nEnter decimal number: ")
    if decnum_input.isdigit():
        decnum_input = int(decnum_input)
        print(bin(decnum_input))
        print(oct(decnum_input))
        print(hex(decnum_input))
    else:
        print("Invalid input. Please enter a valid whole number.")
        convert_decimal()
    
    
# Clean up a messy string (strip, title case, remove extra spaces)

def messy_string():
	messy_input = input("\nEnter more than 3 characters in no particular order:  ")
	print(messy_input.strip())
	print(messy_input.title())
	print(" ".join(messy_input.strip().split()))
	



# Count how many times a word appears in a sentence

def word_count():
	sentence_input = input("\nEnter a sentence that has any word more than once:  ")
	search_input = input("\nEnter a word in that is in the sentence:  ")
	print(f"The word '{search_input}' appears {sentence_input.count(search_input)} times in the sentence.")
	


# Check if a word is a palindrome (hint: use slicing + .lower())

def word_palin():
	check_input = input("\nEnter a word:  ")
	check_input = check_input.lower()
	if check_input == check_input[::-1]:
		print("It's a palindrome!")
	else:
		print("Not a palindrome!")

def main():
    while True:
        
        print("\n  Number & String Toolkit ")
        print("=" * 40)
        print(" 1. Convert a decimal       ")
        print(" 2. Clean up messy string ")
        print(" 3. Count words  ")
        print(" 4. Check word palindrome ")
        print(" 5. Quit              ")
        print("=" * 40)


        # Input validation: while loop rejects choices outside 1–5
        choice = ""
        while choice not in ("1", "2", "3", "4", "5"):
            choice = input("  Enter choice (1-5): ").strip()
            if choice not in ("1", "2", "3", "4", "5"):
                print("  Invalid choice. Please enter 1, 2, 3, 4, or 5.")

        if   choice == "1": convert_decimal()
        elif choice == "2": messy_string()
        elif choice == "3": word_count()
        elif choice == "4": word_palin()
        elif choice == "5":
            print("\n  Goodbye!\n")
            break
main()