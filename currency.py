def get_exchange_rate(base_currency, target_currency):
    
    exchange_rates = {
        'USD': {'USD': 1.0, 'INR': 74.0, 'GBP': 0.76, 'JPY': 110.16, 'EUR': 0.85},
        'INR': {'USD': 0.0135, 'INR': 1.0, 'GBP': 0.0108, 'JPY': 1.57, 'EUR': 0.012},
        'GBP': {'USD': 1.31, 'INR': 92.7, 'GBP': 1.0, 'JPY': 145.78, 'EUR': 1.12},
        'JPY': {'USD': 0.0091, 'INR': 0.636, 'GBP': 0.0069, 'JPY': 1.0, 'EUR': 0.0077},
        'EUR': {'USD': 1.18, 'INR': 84.7, 'GBP': 0.89, 'JPY': 129.39, 'EUR': 1.0}
    }
    
    if base_currency in exchange_rates and target_currency in exchange_rates[base_currency]:
        return exchange_rates[base_currency][target_currency]
    else:
        return None
def currency_converter():
    
    print("Available currencies (ISO codes):")
    print("USD - United States Dollar")
    print("INR - Indian Rupee")
    print("GBP - British Pound")
    print("JPY - Japanese Yen")
    print("EUR - Euro")
    
    
    amount = float(input("\nEnter the amount to convert: "))
    from_currency = input("Convert from (currency code): ").upper()
    to_currency = input("Convert to (currency code): ").upper()
    
    # Get exchange rate
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    if exchange_rate is not None:
        result = amount * exchange_rate
        print(f"\n{amount} {from_currency} is equal to {result} {to_currency}")
    else:
        print(f"Unable to perform currency conversion. Please check the currency codes.")

if __name__ == "__main__":
    currency_converter()
