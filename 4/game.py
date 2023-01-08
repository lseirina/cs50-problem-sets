



import random

while True:
    try:
        level = int(input("Level: "))
        if level < 0:
            pass
        else:
            break
    except:
        pass
    
        
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            pass
        else:
            answer = random.randint(1, level)
            if answer < guess:
                print("Too large!")
            elif answer > guess:
                print("Too small!")
            else:
                break
    except:
        pass
print("Just right!")