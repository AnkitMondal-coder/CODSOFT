import random
import string

print("Password Generator")

# Get the desired password length from the user
try:
    length = int(input("Enter the desired password length: "))
    if length <= 0:
        print("Please enter a positive integer.")
    else:
        # Define possible characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        print("Generated Password:", password)
except ValueError:
    print("Invalid input. Please enter a numeric value for length.")


