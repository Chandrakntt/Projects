def check_password_strength(character):
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in character:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True
            break

    score = 0
    if len(character) >= 8:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score == 5:
        return "STRONG"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "WEAK"

password1 = input("Enter Your Password: ")
strength = check_password_strength(password1)
print("Password Stregth: ", strength)


    


