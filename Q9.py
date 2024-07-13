# Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.


import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_random_password())
