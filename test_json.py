import requests
import sys

url = "http://api.fixer.io/latest?base="

birinci_valyuta = input("Birinci Valyuta:")
ikinici_valyuta = input("Ikinci Valyuta:")
miqdar = float(input("Miqdar:"))

response = requests.get(url + birinci_valyuta)

json_melumat = response.json()
try:
    print(json_melumat["rates"][ikinici_valyuta] * miqdar)

except KeyError:
    sys.stderr.write("Duzgun valyuta daxil edin")
    sys.stderr.flush()