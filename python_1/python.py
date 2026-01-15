print("Password Cracking Simulator (Educational)")
password = input("Enter a password for testing: ")
print("Password received.")
password = "user typed value"
import hashlib

hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("Hashed password:", hashed_password)
print("\nStarting dictionary attack...")

for guess in common_passwords:
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
    
    if guess_hash == hashed_password:
        print("Password cracked!")
        print("Password was:", guess)
        break
else:
    print("Password not found in dictionary.")


