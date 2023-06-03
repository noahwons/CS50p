import sys
import json
import requests

def trynum():
    try:
        btcnum = sys.argv[1]
        try:
            float(btcnum)
            return btcnum
        except ValueError:
            sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

try:
    btcnum = trynum()
    request = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = request.json()
    btcprice = r['bpi']['USD']['rate_float']
    amount = float(btcnum) * btcprice
    print(f"${amount:,.4f}")

except requests.RequestException:
    sys.exit()
