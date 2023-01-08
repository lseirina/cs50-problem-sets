
"""
camelCase = input("camelCase: ")
 
print("snake_case:", end ="")

for letter in camelCase:
    if letter.isupper():
        print("_" + letter.lower(), end = "")

    else:
        print(letter, end = "")


print()
 """

camelcase = input("camelCase: ")
print("snake_case: ", end="")
for i in camelcase:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

print()
    


