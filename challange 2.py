    def _init_(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount > self._account_balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"

# Creating an instance of the BankAccount class
my_account = BankAccount("123456789", "John Doe", 1000)

# Testing deposit and withdrawal functionality
print(my_account.display_balance())  # Display initial balance
print(my_account.deposit(500))        # Deposit $500
print(my_account.withdraw(200))       # Withdraw $200
print(my_account.display_balance())  # Display updated balance
