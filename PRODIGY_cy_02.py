import re

def check_password_strength(pswd):
    min_len = 8
    score = 0
    fdbck = []
    if len(pswd) < min_len:
        fdbck.append(f"Password is too short. It should be at least {min_len} characters long.")
    else:
        score += 1 
    
    if re.search(r"[A-Z]", pswd):
        score += 1
    else:
        fdbck.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", pswd):
        score += 1
    else:
        fdbck.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", pswd):
        score += 1
    else:
        fdbck.append("Include at least one number.")

    if re.search(r"[!@#$%^&*()_+-=,.<>/?]", pswd): 
        score += 1
    else:
        fdbck.append("Include at least one special character (e.g., !@#$%^&*).")

    if score == 5:
        strength = "Very Strong"
        final_feedback = "Excellent password! Highly secure."
    elif score >= 3:
        strength = "Moderate"
        final_feedback = "Your password is decent, but consider making it stronger with a longer length or more character diversity."
    else:
        strength = "Weak"
        final_feedback = "Your password is weak. Please consider the suggestions below to improve it."

    return strength, final_feedback, fdbck

pswd = input("Enter your password to check its strength: ")
strength, final_feedback, improvements = check_password_strength(pswd)

print(f"\nPassword Strength: {strength}")
print(f"Feedback: {final_feedback}")

if improvements:
    print("\nSuggestions for improvement:")
    for suggestion in improvements:
        print(f"- {suggestion}")
