import random
import string

print("===================================")
print("     RANDOM PASSWORD GENERATOR")
print("===================================")

# Ask the user for password length
length = int(input("Enter password length: "))

# Check whether the length is valid
if length < 4:
    print("Password length must be at least 4 characters.")
else:
    # Character sets
    letters = string.ascii_letters
    numbers = string.digits
    special_characters = "@#$"

    # Make sure the password contains at least
    # one letter, one number, and one special character
    password = [
        random.choice(letters),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    # Remaining characters
    all_characters = letters + numbers + special_characters

    for i in range(length - 3):
        password.append(random.choice(all_characters))

    # Shuffle the password characters
    random.shuffle(password)

    # Convert list into a string
    password = "".join(password)

    print("\nGenerated Password:", password)