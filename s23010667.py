class Bank_Account:
    # Initialize bank account
    def __init__(self, account_No, initial_balance):
        # Initialize account number and balance
        self.account_No = account_No
        self.balance = initial_balance

    # Method to deposit money
    def deposit(self, Deposit_amount):
        # Check if deposit amount is valid
        if Deposit_amount <= 0:
            print("Deposit_amount can't zero or negative.")
        else:
            self.balance += Deposit_amount     # Add deposit amount to balance
            print(f"Your Deposit is successful.Deposit amount is {Deposit_amount} and Your balance is {self.balance}")

    # Method to withdraw money
    def withdraw(self, Withdraw_amount):
        # Check if withdrawal amount is valid
        if Withdraw_amount <= 0:
            print("Withdraw_amount can't zero or negative.")
        elif Withdraw_amount <= self.balance:
            self.balance -= Withdraw_amount      # Subtract withdrawal amount from balance
            print(f"Your Withdraw_amount is successful.Withdraw amount is {Withdraw_amount} and Your balance is {self.balance}")
        else:
            # if account balance is insufficient print error message
            print("You account balance is insufficient!")

    # method to get account balance
    def check_balance(self):
        # Print account balance
        print(f"Account {self.account_No} balance: {self.balance}")

    # Method to transfer money
    def transfer(self,transfer_amount,recipient):
        # Check if transfer amount is valid
        if transfer_amount <= 0:
            print("transfer_amount can't zero or negative.")
        # if account balance is insufficient print error message
        elif transfer_amount > self.balance:
            print("Balance is Insufficient!")
        else:
            self.balance -= transfer_amount
            recipient.balance += transfer_amount
            print(f"Transferred {transfer_amount} to account no {recipient.account_No}.")
            print(f"your account no:{self.account_No} balance:Rs.{self.balance}")


# Function to create a new account
def create_account(accounts):
    account_No = input("Enter account No: ")
    if account_No in accounts:
        print("Account already exists!")
        return
    elif int(account_No) > 0:
        initial_deposit_amount = int(input("Enter deposit amount: "))
        if initial_deposit_amount > 0:
            accounts[account_No] = Bank_Account(account_No,initial_deposit_amount)
            print("Account Created!")
        else:
            print("initial_deposit_amount can't zero or negative.")
    else:
        print("Invalid account no!")


# Function to deposit money
def deposit(accounts):
    account_No = input("Enter account No: ")
    if account_No not in accounts:
        print("Account not found!")
        return
    Deposit_amount = int(input("Enter deposit amount: "))
    accounts[account_No].deposit(Deposit_amount)


# Function to withdraw money
def withdraw(accounts):
    account_No = input("Enter account No: ")
    if account_No not in accounts:
        print("Account not found!")
        return
    Withdraw_amount = int(input("Enter Withdrawals amount: "))
    accounts[account_No].withdraw(Withdraw_amount)


# Function to check the balance
def check_balance(accounts):
    account_No = input("Enter account No: ")
    if account_No not in accounts:
        print("Account not found!")
        return
    accounts[account_No].check_balance()


# Function to transfer money
def transfer(accounts):
    sender_account_No = input("Enter sender's account No: ")
    if sender_account_No not in accounts:
        print("Account not found!")
        return
    recipient_account_No = input("Enter recipient's account No: ")
    if recipient_account_No not in accounts:
        print("Account not found!")
        return
    transfer_amount = int(input("Enter the transfer amount: "))
    accounts[sender_account_No].transfer(transfer_amount,accounts[recipient_account_No])


# Main function
def main():
    accounts = {}
    while True:
        print("\nwelcome to Bank Account Management System!\n")
        print("Enter 1 - Create a new account")
        print("Enter 2 - Deposit money")
        print("Enter 3 - Withdraw money")
        print("Enter 4 - Check the account balance")
        print("Enter 5 - Transfer money between two accounts")
        print("Enter 6 - Exit\n")

        user_Input = input("Enter your choice: ")

        if user_Input == '1':
            create_account(accounts)

        elif user_Input == '2':
            deposit(accounts)

        elif user_Input == '3':
            withdraw(accounts)

        elif user_Input == '4':
            check_balance(accounts)

        elif user_Input == '5':
            transfer(accounts)

        elif user_Input == '6':
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
