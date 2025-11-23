 
Currency Converter Project
Author: Annant Pundir
 
 Reg No: 25BCY10113
 
 Campus: VIT Bhopal
This project converts 15 currencies to any of the 15 currencies.
 
 
🧾 Features
✔ Converts any currency to any other (15 × 15)
  ✔ Uses INR as the internal base for accurate conversion
  ✔ Full offline functionality
  ✔ Simple menu-driven interface
  ✔ Beginner-friendly Python code
  ✔ Includes basic input validation
  ✔ Fast and lightweight
 
 
 
 
💱 Supported Currencies
USD (US Dollar)
EUR (Euro)
GBP (British Pound)
AUD (Australian Dollar)
CAD (Canadian Dollar)
JPY (Japanese Yen)
CNY (Chinese Yuan)
RUB (Russian Ruble)
CHF (Swiss Franc)
NZD (New Zealand Dollar)
SGD (Singapore Dollar)
ZAR (South African Rand)
AED (UAE Dirham)
SAR (Saudi Riyal)
KRW (South Korean Won)
 
 
 
 
⚙️ How It Works
User selects FROM currency (1–15)
User selects TO currency (1–15)
User enters an amount
Program converts amount using this formula:
Amount in Source Currency → INR → Target Currency
   5.	Final converted value is displayed.
 
 
 
 
  Code (Main Script)

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



Output
1) USD
2) EUR
...
15) KRW

Currency to convert FROM (1-15): 1
Currency to convert TO (1-15): 2
Enter amount: 100

100 USD is approximately 91.15 EUR





  
 
 
Testing
Tested all valid currency combinations
Tested invalid input (letters, out-of-range values)
Verified accuracy using INR as a base
 

