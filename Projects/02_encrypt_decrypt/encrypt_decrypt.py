message = input("Enter message: ")
key = int(input("Enter Key (number): "))

print("message:",message)
print("key:",key)

ch = message[0]

# if ch.isupper():
#     position = ord(ch) - ord('A')
#     new_position = (position + key) % 26
#     encrypted_char = chr(new_position + ord('A'))

#     print("Origional:",ch)
#     print("Encrypted:",encrypted_char)


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

decrypted_message = ""

for ch in encrypted_message:
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

print("Encrypted message:",encrypted_message)
print("Decrypted message:",decrypted_message)





