def add(a, b):
    """Helper function."""
    return a + b

def multiply(a, b):
    """Another helper function."""
    return a * b

def main():
    """Main program — runs when script is executed."""
    print("=== Calculator ===")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    sum_result = add(x, y)
    product = multiply(x, y)

    print(f"{x} + {y} = {sum_result}")
    print(f"{x} * {y} = {product}")

# This line ensures main() only runs when this file is executed directly
# It does NOT run if this file is imported as a module
if __name__ == "__main__":
    main()

# Example output when run:
# === Calculator ===
# Enter first number: 5
# Enter second number: 3
# 5 + 3 = 8
# 5 * 3 = 15