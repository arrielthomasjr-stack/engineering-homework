secret_number = 26
guess = ["13", "24", "36", "26", "42", "28", "46"]
x = 0
count = 0

while x < len(guess):
    if int(guess[x]) == secret_number:
        print("Correct!")
        break
    elif int(guess[x]) < secret_number:
        print("Too low!")
    else: 
        print("Too high!")        
    count += 1
    x += 1

print(f"You guessed {count} times.")