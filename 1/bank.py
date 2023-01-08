


"""
def main():
    greeting = input("Greetings: ")
    print(value(greeting))
def value(greeting):
    greeting = greeting.strip().lower()
    if "hello" in greeting:
        return "$0"
    elif greeting[0] == "h":
        return "$20"
    else:
        return "$100"

if __name__=="__main__":
    main()


"""
# my solution:

def main():
    greeting = input("Greeting: ")
    output = value(greeting)
    print(f"${output}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ in "__main__":
    main()


