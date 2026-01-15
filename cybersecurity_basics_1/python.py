import hashlib

print("Password Cracking Simulator (Educational)")

# 1. Take password input from user
password = input("Enter a password for testing: ")
print("Password received.")

# 2. Hash the password
hashed_password = hashlib.sha256(password.encode()).hexdigest()
print("Hashed password:", hashed_password)

# 3. Define a dictionary of common passwords (for testing)
common_passwords = [
    "123456",
    "password",
    "admin",
    "hello",
    "welcome",
    "hello123"
]

print("\nStarting dictionary attack...")

# 4. Simulate dictionary attack
for guess in common_passwords:
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()

    if guess_hash == hashed_password:
        print("Password cracked!")
        print("Password was:", guess)
        break
else:
    print("Password not found in dictionary.")
