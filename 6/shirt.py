"""
import sys
from PIL import Image
from PIL import ImageOps
import os
# def check_comand_line():
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 4:
    sys.exit("Too many command-line arguments")
# if not sys.argv[1] and  sys.argv[2] in [".jpg", ".png", ".jpeg"]:
#     sys.exit("Invalid Input")
# if sys.argv[1][-3:] != sys.argv[2][-3:]:
#     sys.exit("input and output have different extensions")
file1 = os.path.splitext(sys.argv[1])
file2 = os.path.splitext(sys.argv[2])
if file1[1] != file2[1]:
    sys.exit("input and output have different extensions")
if not file1[1] in [".jpg", ".png", ".jpeg"]:
    sys.exit("Invalid Input")
if not file1[2] in [".jpg", ".png", ".jpeg"]:
    sys.exit("Invalid Output")



try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
shirt = Image.open("shirt.png")
size = shirt.size

photo = ImageOps.fit(image,size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
"""


import sys
import os
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
file1 = os.path.splitext(sys.argv[1])
file2 = os.path.splitext(sys.argv[2])
if file1[1] != file2[1]:
    sys.exit("Input and output have different extensions")
if file1[1] not in [".jpg", ".jpeg", ".png"] and file2[1] not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")

try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
shirt = Image.open("shirt.png")
size = shirt.size

photo = ImageOps.fit(image,size)
photo.paste(shirt, shirt)
photo.save(sys.argv[2])
