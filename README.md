# password-strength-checker
This is a command-line Python program that evaluates the strength of a user-provided password based on commonly used security rules.
The program analyzes the password, calculates a score, classifies its strength, and provides clear feedback on missing requirements.

Password input is masked using Python’s built-in getpass module so that the password is not displayed on the screen.

Features:
1) Password input masking (hidden input)
2) Rule-based password validation
3) Uniform scoring system
4) Clear strength classification (Weak / Medium / Strong)
5) Detailed feedback for improving weak passwords

Password Rules:
Each rule satisfied gives 2 points, for a maximum score of 10.
| Rule              | Description                             |
| ----------------- | --------------------------------------- |
| Length            | At least 8 characters                   |
| Uppercase         | At least one uppercase letter           |
| Lowercase         | At least one lowercase letter           |
| Number            | At least one digit                      |
| Special character | At least one non-alphanumeric character |

Strength Classification
1) Weak: Mandatory rules not satisfied or low score
2) Medium: Most rules satisfied
3) Strong: All rules satisfied
4) Uppercase and lowercase letters are mandatory for a password to be considered strong.

Technologies Used
1) Python 3
2) Standard Library (getpass)

How to run
password strength checker.py

Notes
1) This project focuses on password validation, not encryption or storage.
2) Password masking works in standard terminals and command prompts.
3) Some IDE consoles may not support masked input.
