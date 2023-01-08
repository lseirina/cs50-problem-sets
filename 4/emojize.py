"""


from cgi import print_environ_usage
import emoji
import requests
import json





item = input("Input: ")
print("Output:", emoji.emojize(item, language="alias"))

"""

import emoji


item = input("Input: ")
print(emoji.emojize(f"Output: :{item}:", language='alias'))