import re
# email = input("What is your email adress? ")
# if re.search("^.+@.+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# email = input("What is your email adress? ")
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# email = input("What is your email adress? ")
# if re.search(r"^[a-zA-z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# email = input("What is your email adress? ")
# if re.search(r"^\w+@\w+\.edu$",email):
#     print("Valid")
# else:
#     print("Invalid")

# email = input("What is your email adress? ")
# if re.search(r"^(\w|\s)+@\w+\.(edu|com|net)$",email):
#     print("Valid")
# else:
#     print("Invalid")

email = input("What is your email adress? ")
if re.search(r"^(\w+\.)?\w+@\w+\.edu$",  email, re.IGNORECASE):
    print("valid")
else:
    print("Invalid")