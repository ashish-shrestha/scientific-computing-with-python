class Category:
    def __init__(self, ledger):
        ledger = []

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def deposit(self, amount, description=''):
        amount = amount
        description = description
        entry = {"amount": amount, "description": description}
        self.ledger.append(entry)

    def withdraw(self, amount, description=''):
        amount = amount
        current_balance = self.get_balance()
        if self.check_funds():
            entry = {"amount": -1 * amount, "description": description}
            return True
        else:
            return False

    def transfer(self, amount, category):
        amount = amount
        category = category
        if self.check_funds():
            self.withdraw(amount, 'Transfer to ' + category)
            category.deposit(amount, 'Transfer from ' + self)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    categories = categories
    