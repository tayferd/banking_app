

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"deposited {amount} dollars, New balance: {self.balance} dollars")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds.")
        else:
            self.balance -= amount
            print(f"withdraw {amount} dollars, New balance: {self.balance} dollars.")

    def check_balance(self):
        print(f"withdraw {amount} dollars. New balance: {self.balance} dollars.")

    def main():
        accounts = ()
        while True:
            print("\nWelcome to the Bank")
            print("1. Create Account")
            print("2. Log in")
            print("3. Quit")

            choice = input("Enter your choice: ")


            if choice == "1":
                name = input("Enter your name: ")
                if name in accounts:
                    print("Account already exits ")
                else:
                    accounts[name] = BankAccount(name)
                    print("Account created sauccessfully.")
            elif choice == "2":
                name = input("Enter your name")
                if name in accounts[name]:
                    account = accounts[name]
                    print(f"Welcome back, {name}")
                    while True:
                        print("\n1. Check Balance")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Logout")

                        option = input("Enter your option: ")

                        if option == "1":
                            account.check_balance()
                        elif option == "2":
                            amount = float(input("Enter amount to deposit:"))
