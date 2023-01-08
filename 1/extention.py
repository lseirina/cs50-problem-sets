# file = input("File name: ")
# file_new = file.strip().lower()
# if "gif" in file_new:
#     print("image/gif")
# elif "jpg" in file_new:
#     print("image/jpg")
# else:
#     print("application/octet-stream")

"""
from distutils import extension


file = input("File name: ")
name, extension = file.split(".")
if extension in ["gif", "jpg", "jpeg", "png"]:
    print(f"image/{extension}")
elif extension in ["pdf", "zip"]:
    print(f"application/{extension}")
elif "zip" in extension:
    print(f"text/{extension}")
else:
    print("application/octet-stream")


"""

"""
import sys

file = input("File name: ")
try:
    a,b = file.split(".")
    if b in ["gif", "jpg", "jpeg", "png"]:
        print(f"image/{b}")
    elif b in ["zip", "pdf"]:
        print(f"application/{b}")
    elif b == "txt":
        print(f"text/{b}")
    else:
        print("application/octet-stream")
except:
    sys.exit("application/octet-stream")

"""
file = input("File name: ")
new_file = file.lower()
if ".gif" in new_file:
    print("image/gif")
elif ".jpg" in new_file:
    print("image/jpeg")
elif ".jpeg" in new_file:
    print("image/jpeg")
elif ".png" in new_file:
    print("image/png")
elif ".zip" in new_file:
    print("application/zip")
elif ".pdf" in new_file:
    print("application/pdf")
elif ".txt" in new_file:
    print("text/plain")
else:
    print("application/octet-stream")



