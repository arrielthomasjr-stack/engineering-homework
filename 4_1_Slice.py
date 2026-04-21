def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                start = ord("A")
                result += chr((ord(ch) - start + shift) % 26 + start)
            else:
                start = ord("a")
                result += chr((ord(ch) - start + shift) % 26 + start)
        else:
            result += ch

    return result

def main():
    full_name = input("Enter your full name: ")

    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1]

    print("First initial and last name:", first_name[0] + last_name)
    print("Reversed name:", full_name[::-1])

    shift = int(input("Enter a shift number: "))

    encrypted = caesar_cipher(full_name, shift, "encrypt")
    print("Encrypted name:", encrypted)

    decrypted = caesar_cipher(encrypted, shift, "decrypt")
    print("Decrypted name:", decrypted)

    if decrypted == full_name:
        print("Decryption matches the original name.")
    else:
        print("Decryption does not match the original name.")

if __name__ == "__main__":
    main()