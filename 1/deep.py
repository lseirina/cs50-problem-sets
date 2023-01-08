"""
q = input("What is the answer to the great question of life? ")

if q.strip() == "42":
    print("yes")
elif q.lower().strip() == "forty two":
    print("yes")
elif q.lower().strip() == "forty-two":
    print("yes")
else:
    print("No")



"""

question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
if question in ["42", "forty two", "forty-two"] :
    print("Yes")
else:
    print("No")