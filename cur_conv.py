import requests


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    if response.status_code == 200:
        rates = response.json().get("rates", {})
        if to_currency.upper() in rates:
            converted = amount * rates[to_currency.upper()]
            print(f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            print(f"Error: {to_currency.upper()} not found in exchange rates.")
    else:
        print("Error fetching conversion rate")


# Taking user input
amount = float(input("Enter the amount: "))

