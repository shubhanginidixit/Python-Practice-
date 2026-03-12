# Custom Exception
class InvalidTransactionError(Exception):
    pass


# Bank Account Class
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidTransactionError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InvalidTransactionError("Insufficient balance.")
        
        self.balance -= amount
        print("Withdrawal successful. Remaining balance:", self.balance)


# Program Flow
try:
    account = BankAccount(5000)
    
    amt = int(input("Enter withdrawal amount: "))
    account.withdraw(amt)

except InvalidTransactionError as e:
    print("Transaction Error:", e)

except Exception as e:
    print("Unexpected Error:", e)