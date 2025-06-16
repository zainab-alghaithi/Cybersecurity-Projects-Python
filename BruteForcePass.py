import itertools
import string

def brute_force_password(secret):
    letters = string.ascii_lowercase
    digits = string.digits
    # Iterate through all combinations: 5 letters + 2 digits
    for letter_tuple in itertools.product(letters, repeat=5):
        for digit_tuple in itertools.product(digits, repeat=2):
            guess = ''.join(letter_tuple) + ''.join(digit_tuple)
            print(f"Trying: {guess}")
            if guess == secret:
                print(f"\nPassword found: {secret!r}")
                return
    print("Password not found.")

def main():
    # Prompt the user for a password that consists of 5 letters followed by 2 digits
    secret = input("Enter a password (5 lowercase letters followed by 2 digits): ").strip()
    if len(secret) != 7:
        print("Password must be exactly 7 characters (5 letters + 2 digits).")
        return
    if not (secret[:5].isalpha() and secret[:5].islower()):
        print("The first 5 characters must be lowercase letters.")
        return
    if not secret[5:].isdigit():
        print("The last 2 characters must be digits.")
        return

    print("\nStarting brute-force...\n")
    brute_force_password(secret)

if __name__ == "__main__":
    main()