class Account:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class ATM:
    def __init__(self):
        self.accounts = {}
        self.current_account = None

    def create_account(self, account_number, pin, initial_balance=0.0):
        if account_number in self.accounts:
            return False
        else:
            self.accounts[account_number] = Account(account_number, pin, initial_balance)
            return True

    def login(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            self.current_account = account
            return True
        else:
            return False

    def logout(self):
        self.current_account = None

    def check_balance(self):
        if self.current_account:
            return self.current_account.check_balance()
        else:
            return None

    def deposit(self, amount):
        if self.current_account:
            return self.current_account.deposit(amount)
        else:
            return False

    def withdraw(self, amount):
        if self.current_account:
            return self.current_account.withdraw(amount)
        else:
            return False

def main():
    atm = ATM()

    while True:
        print("\nATM Interface")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            initial_balance = float(input("Enter initial balance: "))
            if atm.create_account(account_number, pin, initial_balance):
                print("Account created successfully.")
            else:
                print("Account creation failed. Account number may already exist.")
        elif choice == '2':
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            if atm.login(account_number, pin):
                print("Login successful.")
                while True:
                    print("\n1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")
                    sub_choice = input("Choose an option: ")

                    if sub_choice == '1':
                        balance = atm.check_balance()
                        if balance is not None:
                            print(f"Current balance: {balance}")
                        else:
                            print("Unable to retrieve balance.")
                    elif sub_choice == '2':
                        amount = float(input("Enter amount to deposit: "))
                        if atm.deposit(amount):
                            print("Deposit successful.")
                        else:
                            print("Deposit failed.")
                    elif sub_choice == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        if atm.withdraw(amount):
                            print("Withdrawal successful.")
                        else:
                            print("Withdrawal failed.")
                    elif sub_choice == '4':
                        atm.logout()
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Login failed. Invalid account number or PIN.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
