# Write a Program to check whether User's Given Password is Weak or Strong

password = input("Enter your password: ")
print(password)

if len(password) >= 8:
    print("Password length is OK")
else:
    print("Password is too short")

has_upper = False

for ch in password:
    if ch.isupper():
        has_upper = True
        break

if has_upper:
    print("Contains Uppercase letters")
else:
    print("No Uppercase letter found")

has_lower = False

for ch in password:
    if ch.islower():
        has_lower = True
        break

if has_lower:
    print("Contains Lowercase letters")
else:
    print("No Lowercase letter found")    


has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True
        break

if has_digit:
    print("Contains Digit")
else:
    print("No Digit found")


has_alnum = False

for ch in password:
    if not ch.isalnum():
        has_alnum = True
        break

if has_alnum:
    print("Contains Special Character")
else:
    print("No Special Charcter found")

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_alnum:
    score += 1

print("Score: ",score)

if score == 5:
    print("Password Strength : STRONG")
elif score >= 3:
    print("Password Strength : MEDIUM")
else:
    print("Password Strength : WEAK")

