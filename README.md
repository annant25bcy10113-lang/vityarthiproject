📘 Currency Converter

A simple and efficient Python-based currency converter that can convert any of 15 currencies to any other using INR as an internal base.The program is fully offline, beginner-friendly, and demonstrates clean menu-driven programming.

🧾 Features

✔ Converts any currency to any other (15 × 15)
✔ Uses INR as the internal base for accurate conversion
✔ Full offline functionality
✔ Simple menu-driven interface
✔ Beginner-friendly Python code
✔ Includes basic input validation
✔ Fast and lightweight

🧾 Features

✔ Converts any currency to any other (15 × 15)
✔ Uses INR as the internal base for accurate conversion
✔ Full offline functionality
✔ Simple menu-driven interface
✔ Beginner-friendly Python code
✔ Includes basic input validation
✔ Fast and lightweight


⚙️ How It Works

1.User selects FROM currency (1–15)

2.User selects TO currency (1–15)

3.User enters an amount

4.Final converted value is displayed.


📂 Project Structure


📁 Currency-Converter-15x15
│── currency_converter.py
│── README.md
│── docs/
│     ├── usecase.png
│     ├── workflow.png
│     ├── sequence.png
│     ├── class.png
│     ├── er.png







🧠 Code (Main Script)

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

print("\n=== Currency Converter (15x15) ===\n")

curr_list = list(currency_rates.keys())

print("Available Currencies:\n")
for index, curr in enumerate(curr_list, 1):
    print(f"{index}) {curr}")

try:
    from_idx = int(input("\nCurrency to convert FROM (1-15): "))
    to_idx   = int(input("Currency to convert TO (1-15): "))
    amt = float(input("Enter the amount you'd like to convert: "))
except:
    print("Something went wrong with your input.")
    from_idx, to_idx = -1, -1
    amt = 0

if 1 <= from_idx <= 15 and 1 <= to_idx <= 15:
    from_curr = curr_list[from_idx - 1]
    to_curr = curr_list[to_idx - 1]

    inr_value = amt * currency_rates[from_curr]
    final_amount = inr_value / currency_rates[to_curr]

    print(f"\n{amt} {from_curr} is approximately {final_amount:.2f} {to_curr}\n")

else:
    print("\nInvalid choice! (I'll probably add better error messages later.)")


   

    


📝 Sample Output

    === Currency Converter (15x15) ===

1) USD
2) EUR
...
15) KRW

Currency to convert FROM (1-15): 1

Currency to convert TO (1-15): 2


Enter amount: 100


100 USD is approximately 91.15 EUR




🧪 Testing

Tested all valid currency combinations

Tested invalid input (letters, out-of-range values)

Verified accuracy using INR as a base



🚀 Future Enhancements

GUI version (Tkinter)

Live exchange rates using API

More currencies (50+)

Conversion history

Export results as CSV






👤 Author

Annant Pundir
Reg No: 25BCY10113
VIT Bhopal







