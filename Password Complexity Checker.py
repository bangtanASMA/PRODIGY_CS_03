import re

def password_strength(password):
    length = len(password)
    score = 0

    # Criteria
    if length >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~`]", password):
        score += 1

    # Feedback
    if score == 0:
        return "Very Weak: Password should contain at least 8 characters including uppercase, lowercase letters, numbers, and special characters."
    elif score == 1:
        return "Weak: Password should contain at least 8 characters including uppercase, lowercase letters, numbers, and special characters."
    elif score == 2:
        return "Moderate: Password should contain at least 8 characters including uppercase, lowercase letters, numbers, and special characters."
    elif score == 3:
        return "Strong: Password should contain at least 8 characters including uppercase, lowercase letters, numbers, and special characters."
    elif score == 4:
        return "Very Strong: Password meets all criteria, but consider adding more complexity."
    else:
        return "Extremely Strong: Password meets all criteria and is highly secure."

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
