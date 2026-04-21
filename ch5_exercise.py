# Write a program that asks for a list of numbers, reverses the list, and prints all numbers greater than 50.
# def reverse_and_filter(numbers):
#     """Reverses the list and filters numbers greater than 50."""
#     reversed_numbers = numbers[::-1]  # Reverse the list
#     filtered_numbers = [num for num in reversed_numbers if num > 50]  # Filter numbers greater than 50
#     return filtered_numbers 

# def main():
#     """Main program — runs when script is executed."""
#     input_numbers = input("Enter a list of numbers separated by spaces: ")
#     numbers = list(map(int, input_numbers.split()))  # Convert input string to a list of integers

#     result = reverse_and_filter(numbers)
#     print("Numbers greater than 50 in reversed order:", result)

# if __name__ == "__main__":
#     main()

def person_info():
	name = "John"
	age = 45
	city = "Tampa"
	return (name, age, city)

n, a, c = person_info()
print(n, "is", a, "and lives in", c,".")

