import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter the desired length of the password: "))
password = generate_password(length)
print("Generated Secure Password:", password)