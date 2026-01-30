import getpass 

def password_check(password):
    if not password:
        return None

    rules = {
        "length": False,
        "uppercase alphabet": False,
        "lowercase alphabet": False,
        "number": False,
        "special character": False
    }

    if len(password) >= 8:
        rules["length"] = True

    for char in password:
        if char.isupper():
            rules["uppercase alphabet"] = True
        elif char.islower():
            rules["lowercase alphabet"] = True
        elif char.isdigit():
            rules["number"] = True
        elif not char.isalnum():
            rules["special character"] = True

    return rules


def cal_score(rules):
    score = 0
    for rule in rules.values():
        if rule:
            score += 2

    if not (rules["uppercase alphabet"] and rules["lowercase alphabet"]):
        print("Weak password")
    elif score <= 4:
        print("Weak password")
    elif score <= 8:
        print("Medium password")
    else:
        print("Strong password")

    print(f"Your password score is {score}/10")
    return score


def generate_feedback(rules):
    for rule, passed in rules.items():
        if not passed:
            if rule == "length":
                print("Password must contain at least 8 characters.")
            else:
                print(f"Password must contain at least one {rule}.")


password = getpass.getpass("Enter the password: ")

rules = password_check(password)
if rules is None:
    print("Password cannot be empty.")
else:
    score = cal_score(rules)
    generate_feedback(rules)
