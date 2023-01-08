"""
import requests
import sys
import json
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()

    rate = o["bpi"]['USD']["rate_float"]

except requests.RequestException:
    print("ExceptionError")
    sys.exit[1]

try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    else: 
        amount = float(sys.argv[1]) * float(rate)
        print(f"$ {amount:,.4f}")
except:
    print("Command-line argument is not a number")

"""



import json
import requests
import sys

try:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    
    else:
        try: 
                response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                o = response.json()
                rate = o["bpi"]["USD"]["rate_float"]
                amount = float(sys.argv[1]) * rate
                print(f"${amount:,.4f}")
        except requests.RequestException:
                sys.exit("Command-line argument is not a number")
except:
    sys.exit("Command-line argument is not a number")






















