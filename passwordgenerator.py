
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


print("==========================")
print("    PASSWORD GENERATOR")
print("==========================")

length = int(input("Enter password length: "))

if length < 4:
    print("Password must be at least 4 characters!")
else:
    password = generate_password(length)

    print("\nYour generated password is:")
    print(password)
    print("\nKeep it safe!")
