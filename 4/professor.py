
"""
import random


def main():
    
    level = get_level()
    score = simulate_game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(1,9)
        y = random.randint(1,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)

    return x,y

def simulate_round(x,y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x,y = generate_integer(level)
        response = simulate_round(x,y)
        if response == True:
            
            score += 1
        count_round += 1
    return score

if __name__ == "__main__":
    main()


"""
import random


def main():
    level = get_level()
    score = simulate_game(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:    
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level



def generate_integer(level):
   
    if level == 1:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
    elif level == 2:
        num_1 = random.randint(11, 99)
        num_2 = random.randint(11, 99)
    elif level == 3:
        num_1 = random.randint(11, 99)
        num_2 = random.randint(11, 99)
    return num_1, num_2

def simulate_round(num_1, num_2):
    i = 0
    while i < 3:
        try:
            answer = int(input(f"{num_1} + {num_2} = "))
            if answer == (num_1 + num_2):
                return True
            else:
                i += 1
                print("EEE")
        except:
            i += 1
            print("EEE")
    
    print(f"{num_1} + {num_2} = {num_1 + num_2}")
    return False

def simulate_game(level):
    i = 0
    score = 0
    while i < 10:
        num_1,num_2 = generate_integer(level)
        response = simulate_round(num_1,num_2)
        if response == True:
            score += 1
        i += 1
    return score

if __name__ in "__main__":
    main()


   
    




        


    

