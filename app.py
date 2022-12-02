import requests

initial_currency = input("Enter the initial currency the amount is in (as 3 letters e.g. CAD): ")
converted_currency = input("Enter the currency you would like the amount converted to (as 3 letters e.g. USD): ")

while True:
    try:
        amount = float(input("Enter the amount: "))
    except:
        print("The amount must be a number!")
        continue

    if not amount > 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = "https://api.apilayer.com/fixer/convert?to=" + converted_currency + "&from=" + initial_currency + "&amount=" + str(
    amount)

payload = {}
headers = {"apikey": "vXX7bXdJQdFhCqBipL24leQqd7l6Y6Vr"}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code

if status_code != 200:
    print("Invalid API key")
    quit()

result = response.json()

converted_currency = converted_currency.upper()
print("Conversion result in " + converted_currency + " is: " + str(result["result"]))
