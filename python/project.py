# # Correct password
# correct_password = "ishika@12"

# # User input
# password = input("Enter your password: ")

# # Check password
# if password == correct_password:
#     print("Access Granted ")
# else:
#     print("Wrong Password ")
 

import re

password = input("Enter your password: ")

if (len(password) >= 8 and
    re.search(r"[a-z]", password) and
    re.search(r"[A-Z]", password) and
    re.search(r"\d", password) and
    re.search(r"[^A-Za-z0-9]", password)):

    print("Valid Password")
else:
    print("Invalid Password")
           



