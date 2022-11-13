class Category:
    def __init__(self, ledger):
        ledger = []

    def deposit(self, amount, description=''):
        amount = amount
        description = description
        entry = {"amount": amount, "description": description}
        self.ledger.append(entry)

    def withdraw(self, amount, description=''):
        amount = -1*amount

        # how to determine what balance is?

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]

        return balance

    








def create_spend_chart(categories):