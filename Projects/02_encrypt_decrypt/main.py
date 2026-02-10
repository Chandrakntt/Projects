def encrypt(message,key):
    encrypted_message = ""

    for ch in message:
        if ch.isupper():
            position = ord(ch) - ord('A')
            new_position = (position + key) % 26
            encrypted_message += chr(new_position + ord('A'))

        elif ch.islower():
            position = ord(ch) - ord('a')
            new_position = (position + key) % 26
            encrypted_message += chr(new_position + ord('a'))

        else:
            encrypted_message += ch

    return encrypted_message


def decrypt(message,key):
    decrypted_message = ""

    for ch in message:
        if ch.isupper():
            position = ord(ch) - ord('A')
            new_position = (position - key) % 26
            decrypted_message += chr(new_position + ord('A'))

        elif ch.islower():
            position = ord(ch) - ord('a')
            new_position = (position - key) % 26
            decrypted_message += chr(new_position + ord('a')) 

        else:
            decrypted_message += ch

    return decrypted_message

# print("Encryption Decryption Tool")

# message = input("Enter Your Message: ")
# key = int(input("Enter Key (number) : "))

# encrypted = encrypt(message,key)
# print("Encrypted:",encrypted)

# decrypted = decrypt(encrypted,key)
# print("Decrypted:",decrypted)

print("=== Caesar Cipher Tool ===")
print("1. Encrypt")
print("2. Decrypt")

choise = input("Choose an option (1 or 2): ")

if choise == "1":
    message = input("Enter Your Message: ")
    key = int(input("Enter Key (number): "))
    encrypted = encrypt(message, key)
    print("Encrypted:",encrypted)

elif choise == "2":
    message = input("Enter Your Message: ")
    key = int(input("Enter Key (number): "))
    decrypted = decrypt(message,key)
    print("Decrypted:",decrypted)

else:
    print("Invalid Choise")




