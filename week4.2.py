from forex_python.converter  
import CurrencyRates

def currency_converter():
    c = CurrencyRates()

    print("Available currencies:")
    print(", ".join(c.get_rates('').keys()))

    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    
    if from_currency == to_currency:
        print("Conversion between the same currencies is not allowed.")
        return

    amount = float(input("Enter the amount to convert: "))

    try:
        rate = c.get_rate(from_currency, to_currency)
        result = amount * rate
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}")
    except:
        print("Invalid currency code or conversion not available.")

if __name__ == "__main__":
    currency_converter()
