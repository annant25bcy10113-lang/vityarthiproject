# Currency Converter (15×15)

A simple and efficient Python-based offline currency converter that converts between 15 currencies using INR as an internal base.

## Features

- Converts any currency to any other (15 × 15)
- Uses INR as the intermediate base for conversions
- Fully offline (no external API required)
- Simple, menu-driven command-line interface
- Beginner-friendly Python code with basic input validation
- Fast and lightweight

## Supported currencies (15)

USD, EUR, GBP, AUD, CAD, JPY, CNY, RUB, CHF, NZD, SGD, ZAR, AED, SAR, KRW

## How it works

1. Choose the currency to convert FROM (1–15).  
2. Choose the currency to convert TO (1–15).  
3. Enter the amount.  
4. The script converts the amount to INR using the FROM currency rate, then converts INR to the TO currency using the TO rate and displays the result.

## Project structure

Currency-Converter-15x15/  
- currency_converter.py  
- README.md  
- docs/  
  - usecase.png  
  - workflow.png  
  - sequence.png  
  - class.png  
  - er.png

## Usage

Run with Python 3:

```bash
python3 currency_converter.py
```

The script will list available currencies and prompt for:
- Currency to convert FROM (enter the number 1–15)  
- Currency to convert TO (enter the number 1–15)  
- Amount to convert

Example interaction:

```
=== Currency Converter (15x15) ===

1) USD
2) EUR
3) GBP
4) AUD
5) CAD
6) JPY
7) CNY
8) RUB
9) CHF
10) NZD
11) SGD
12) ZAR
13) AED
14) SAR
15) KRW

Currency to convert FROM (1-15): 1
Currency to convert TO (1-15): 2
Enter the amount you'd like to convert: 100

100 USD is approximately 91.15 EUR
```

## Main script (currency_converter.py)

```python
# Fixed exchange rates (values are approximate and expressed in INR)
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

def main():
    print("\n=== Currency Converter (15x15) ===\n")

    curr_list = list(currency_rates.keys())

    print("Available Currencies:\n")
    for index, curr in enumerate(curr_list, 1):
        print(f"{index}) {curr}")

    try:
        from_idx = int(input("\nCurrency to convert FROM (1-15): "))
        to_idx   = int(input("Currency to convert TO (1-15): "))
        amt = float(input("Enter the amount you'd like to convert: "))
    except Exception:
        print("Something went wrong with your input.")
        return

    if 1 <= from_idx <= len(curr_list) and 1 <= to_idx <= len(curr_list):
        from_curr = curr_list[from_idx - 1]
        to_curr = curr_list[to_idx - 1]

        inr_value = amt * currency_rates[from_curr]
        final_amount = inr_value / currency_rates[to_curr]

        print(f"\n{amt} {from_curr} is approximately {final_amount:.2f} {to_curr}\n")
    else:
        print("\nInvalid choice! Please enter numbers between 1 and 15.")

if __name__ == "__main__":
    main()
```

## Sample output

```
=== Currency Converter (15x15) ===
...
Currency to convert FROM (1-15): 1
Currency to convert TO (1-15): 2
Enter the amount you'd like to convert: 100

100 USD is approximately 91.15 EUR
```

## Testing

- Verified conversion correctness using INR as the intermediate base.  
- Tested valid currency combinations.  
- Tested invalid input handling (non-numeric values, out-of-range selections).

## Future enhancements

- GUI version (Tkinter)
- Live exchange rates using a public API
- Support for many more currencies (50+)
- Conversion history and export (CSV)
- Better input validation and localized formatting

## Author

Annant Pundir  
Reg No: 25BCY10113  
VIT Bhopal
