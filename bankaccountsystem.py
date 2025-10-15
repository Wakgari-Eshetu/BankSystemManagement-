print("Jesus is Lord!! Welcome to the Waks Bank System\n")

class BankSystem:
   
    total_accounts = 0
    accounts = {}  

    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        self.transactions = [] 
        BankSystem.total_accounts += 1
        BankSystem.accounts[account_number] = self 
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"{amount} deposited. Total balance: {self.balance}")

    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            self.transactions.append(f"Failed withdrawal attempt: {amount}")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")

   
    def check_balance(self):
        print(f"Current balance for {self.name}: {self.balance}")

    
    def transfer(self, target_account_number, amount):
        target_account = BankSystem.accounts.get(target_account_number)
        if not target_account:
            print("Target account not found.")
            return
        if amount > self.balance:
            print("Insufficient balance to transfer.")
            self.transactions.append(f"Failed transfer attempt: {amount} to {target_account.name}")
        else:
            self.balance -= amount
            target_account.balance += amount
            self.transactions.append(f"Transferred {amount} to {target_account.name}")
            target_account.transactions.append(f"Received {amount} from {self.name}")
            print(f"{amount} transferred to {target_account.name}. Your new balance: {self.balance}")

    
    def show_transactions(self):
        print(f"Transaction history for {self.name}:")
        for t in self.transactions:
            print(f"- {t}")


BankSystem("Kena", 1000000, 1001)
BankSystem("Zara", 500000, 1002)
BankSystem("lel",120202,1004)
while True:
    print("\nWelcome to Python Bank System")
    print("1. Login to your account")
    print("2. Create new account")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            acc_no = int(input("Enter your account number: "))
            current_user = BankSystem.accounts.get(acc_no)
            if not current_user:
                print("Account not found!")
                continue

            
            while True:
                print(f"\nHello, {current_user.name}! What would you like to do?")
                print("1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Transfer Money")
                print("5. Transaction History")
                print("6. Logout")

                action = input("Enter your choice: ")

                match action:
                    case "1":
                        current_user.check_balance()
                    case "2":
                        amount = float(input("Enter amount to deposit: "))
                        current_user.deposit(amount)
                    case "3":
                        amount = float(input("Enter amount to withdraw: "))
                        current_user.withdraw(amount)
                    case "4":
                        target_acc_no = int(input("Enter target account number: "))
                        amount = float(input("Enter amount to transfer: "))
                        current_user.transfer(target_acc_no, amount)
                    case "5":
                        current_user.show_transactions()
                    case "6":
                        print(f"Logging out {current_user.name}...")
                        break
                    case _:
                        print("Invalid choice. Try again.")

        case "2":
            name = input("Enter your name: ")
            balance = float(input("Enter initial deposit: "))
            # Generate account number automatically
            new_acc_no = max(BankSystem.accounts.keys(), default=1000) + 1
            BankSystem(name, balance, new_acc_no)
            print(f"Account created successfully! Your account number is {new_acc_no}")

        case "3":
            print("Thank you for using Python Bank System. Goodbye!")
            break

        case _:
            print("Invalid choice. Try again.")
