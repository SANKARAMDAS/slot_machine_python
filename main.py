#Python Slot Machine

def spin_row():
    pass


def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 50


    print("******************************")
    print(" Welcome to the Slot Machine! ")
    print("Symbols: 🍒🍉🔔⭐🍍🥭")
    print("******************************")


    while balance > 0:
        print(f"\nYour current balance is: £{balance}")

        bet = input("Please enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue

if __name__ == '__name__':
    main()