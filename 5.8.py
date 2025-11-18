###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

def check_pin(correct_pin):
    entered = input("Enter your PIN: ")
    if entered == correct_pin:
        print("PIN correct.")
        return True
    else:
        print("Incorrect PIN.")
        return False

def change_pin(current_pin):
    old_pin = input("Enter your current PIN: ")

    if old_pin != current_pin:
        print("Incorrect PIN. PIN not changed.")
        return current_pin

    new_pin = input("Enter a new 4-digit PIN: ")

    if len(new_pin) == 4 and new_pin.isdigit():
        print("PIN changed successfully.")
        return new_pin
    else:
        print("Invalid PIN format. PIN not changed.")
        return current_pin

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        check_pin(pin)
    elif choice == '5':
        pin = change_pin(pin)
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")