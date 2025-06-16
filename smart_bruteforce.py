import itertools
import string
import time

def generate_smart_guesses(name, nickname, birth_year, grad_year, city, pet, favorite):
    base = [name, nickname, birth_year, grad_year, city, pet, favorite]
    base = [x.lower() for x in base if x]

    guesses = set()
    for a in base:
        guesses.add(a)
        guesses.add(a + "123")
        guesses.add(a + birth_year[-2:])
        guesses.add(a + grad_year)
        guesses.add(a + "@" + city)
        for b in base:
            if a != b:
                guesses.add(a + b)
                guesses.add(b + a)
                guesses.add(f"{a}_{b}")
                guesses.add(f"{a}{b}123")
                guesses.add(f"{a}@{b}")
    return list(guesses)

def brute_force_fallback(secret, max_len=5):
    print(f"\n[2] Starting full brute-force search (up to {max_len} characters)...")
    charset = string.ascii_lowercase + string.digits
    attempts = 0

    for length in range(1, max_len + 1):
        for combo in itertools.product(charset, repeat=length):
            guess = ''.join(combo)
            attempts += 1
            if attempts % 100000 == 0:
                print(f"Brute-force try #{attempts}: {guess}")
            if guess == secret:
                print(f"\n✅ Password cracked by brute force: {secret!r} (in {attempts} attempts)")
                return True
    print("\n❌ Password not found in brute-force search.")
    return False

def smart_then_bruteforce(secret, smart_guesses):
    print("\n[1] Trying smart guesses based on personal info...")
    for attempt, guess in enumerate(smart_guesses, start=1):
        print(f"Smart Try #{attempt}: {guess}")
        time.sleep(0.05)
        if guess == secret:
            print(f"\n✅ Password found with smart guess: {guess!r} (in {attempt} tries)")
            return True
    return brute_force_fallback(secret)

def main():
    secret = input("Set a password for testing (any length): ").strip()

    print("\nEnter personal info to improve guesses:")
    name = input("First name: ")
    nickname = input("Nickname: ")
    birth_year = input("Birth year (e.g., 1985): ")
    grad_year = input("Graduation year (e.g., 2014): ")
    city = input("City: ")
    pet = input("Pet's name: ")
    favorite = input("Favorite band/hobby: ")

    smart_guesses = generate_smart_guesses(name, nickname, birth_year, grad_year, city, pet, favorite)

    start_time = time.time()
    smart_then_bruteforce(secret, smart_guesses)
    print(f"\n⏱️ Time elapsed: {round(time.time() - start_time, 2)} seconds")

if __name__ == "__main__":
    main()
