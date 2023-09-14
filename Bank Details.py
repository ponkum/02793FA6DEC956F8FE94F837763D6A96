class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for deposit.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount for withdrawal or insufficient balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: ${self.balance}"


def main():
    # Create a bank account
    account1 = BankAccount("12345", "John Doe")

    while True:
        print("\nBank Account Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            account1.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            account1.withdraw(amount)
        elif choice == "3":
            balance = account1.get_balance()
            print(f"Current balance: ${balance}")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
