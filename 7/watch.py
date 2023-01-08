"""
import re
import sys
# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     matches = re.search(r"https?:\/\/(?:www\.)?youtube\.com\/embed(\/[a-z0-9]+)",s,re.IGNORECASE)
#     if matches:
#         return(f"https://youtu.be{matches.group(1)}")


# if __name__=="__main__":
#     main()

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"^<iframe(.)+<\/iframe>$",s):
        matches = re.search(r"https?:\/\/(?:www\.)?youtube.com\/embed(\/[a-z0-9]+)",s, re.IGNORECASE)
        if matches:
            return(f"https://youtu.be{matches.group(1)}")

if __name__ in "__main__":
    main()

    """





import re
import sys

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

# https://youtu.be/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        match = re.search(r'"https?:\/\/(?:www\.)?youtube\.com\/embed\/([0-9a-zA-Z]*?)"', s)
        if match:
            return f"https://youtu.be/{match.group(1)}"
        else:
            return None
    except:
        sys.exit(1)


if __name__ == "__main__":
    main()