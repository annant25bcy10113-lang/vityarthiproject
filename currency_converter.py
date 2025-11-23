# Just putting the rates here. Might update later if forex changes.
# These values are roughly in INR... at least last time I checked.
currency_rates = {
    "USD": 84.5,
    "EUR": 92.3,
    "GBP": 108.7,
    "AUD": 56.2,
    "CAD": 62.1,
    "JPY": 0.56,
    "CNY": 11.9,
    "RUB": 0.95,
    "CHF": 93.4,
    "NZD": 50.3,
    "SGD": 63.2,
    "ZAR": 4.6,
    "AED": 23.0,
    "SAR": 22.5,
    "KRW": 0.065
}

print("\n=== Currency Converter (15x15) ===\n")  # I like shorter headers

# Converting dict keys to a list (probably unnecessary but feels easier to work with)
curr_list = list(currency_rates.keys())

print("Available Currencies:\n")
for index, curr in enumerate(curr_list, 1):
    # printing like this feels cleaner to me personally
    print(f"{index}) {curr}")

# Asking user for input — no validation yet; maybe add later if needed
try:
    from_idx = int(input("\nCurrency to convert FROM (1-15): "))
    to_idx   = int(input("Currency to convert TO (1-15): "))
    amt = float(input("Enter the amount you'd like to convert: "))
except:
    # quick fallback, not elegant but works
    print("Something went wrong with your input.")
    from_idx, to_idx = -1, -1  # force invalid
    amt = 0

# Quick bounds check
if 1 <= from_idx <= 15 and 1 <= to_idx <= 15:
    # grabbing the currency codes
    # maybe should’ve done better naming but whatever, works for now
    from_curr = curr_list[from_idx - 1]
    to_curr = curr_list[to_idx - 1]

    # Converting FROM -> INR -> target currency
    # Doing this in two steps so it's easier to read (though a single line would work)
    inr_value = amt * currency_rates[from_curr]

    # Slightly unnecessary variable but makes the next line clearer in my head
    final_amount = inr_value / currency_rates[to_curr]

    print(f"\n{amt} {from_curr} is approximately {final_amount:.2f} {to_curr}\n")

else:
    print("\nInvalid choice! (I'll probably add better error messages later.)")

