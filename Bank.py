import sys

if len(sys.argv) != 3:
    print("Usage: <INITIAL_BALANCE> <DEPOSIT_AMOUNT>")
    print("Example: python3 bank_balance.py 5000 1500")
    sys.exit(1)

try:
    initial_balance = float(sys.argv[1])
    deposit_amount = float(sys.argv[2])
except ValueError:
    print("ERROR: Please enter valid numbers for balance and deposit.")
    sys.exit(1)

updated_balance = initial_balance + deposit_amount

print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
print("Updated Balance:", updated_balance)
