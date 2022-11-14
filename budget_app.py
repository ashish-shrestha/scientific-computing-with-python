class Category:
    def __init__(self, name, ledger=[]):
        self.name = name
        self.ledger = []

    def __str__(self):
        length_of_name = len(self.name)
        title_line = ('*' * ((30 - length_of_name) // 2)) + self.name + ('*' * ((30 - length_of_name) // 2))
        result = title_line
        for i in self.ledger:
            desc = i['description']
            amount = str(round(i['amount'], 2))
            if len(desc) > 23:
                desc = desc[:23]
            if len(amount) > 7:
                amount = amount[:7]
            whitespace = 30 - len(desc) - len(amount)
            line = desc + (' ' * whitespace) + amount
            result += '\n' + line

        final = self.get_balance()
        result += '\n' + 'Total: ' + str(final)

        return result

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def deposit(self, amount, description=''):
        amount = amount
        description = description
        entry = {'amount': amount, 'description': description}
        self.ledger.append(entry)

    def withdraw(self, amount, description=''):
        amount = amount
        current_balance = self.get_balance()
        if self.check_funds(amount):
            entry = {'amount': -1 * amount, 'description': description}
            self.ledger.append(entry)
            return True
        else:
            return False

    def transfer(self, amount, category):
        amount = amount
        category = category
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.name)
            category.deposit(amount, 'Transfer from ' + self.name)
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
    bar_chart = 'Percentage spent by category'

    # finding total spend & total spend by category
    spend_by_category = {}
    total_spend = 0
    for category in categories:
        spend = 0
        for item in category.ledger:
            if item['amount'] < 0 and not item['description'].startswith('Transfer to'):
                spend += item['amount']
                total_spend += item['amount']
        spend_by_category[category] = spend

    # determining percentage spent by category
    for category in spend_by_category:
        spend_by_category[category] = round(((spend_by_category[category] / total_spend) * 100) / 10) * 10

    # drawing y-axis and plotting o's
    total_line_length = len((' ' * 3 * (len(categories) - 1)) + (' ' * 4)) + 4
    dict_keys = list(spend_by_category.keys())
    for i in range(100, -10, -10):
        line = str(i) + '|'
        if len(line) < 4:
            line = (' ' * (4 - len(line))) + line
        for category in spend_by_category:
            if spend_by_category[category] == i:
                if line[-1] == '|':
                    line += ' o '
                    spend_by_category[category] -= 10
                else:
                    line += ' o '
                    spend_by_category[category] -= 10
            else:
                if category == dict_keys[-1]:
                    line += ('+' * 4)
                else:
                    line += ('+' * 3)
        if len(line) < total_line_length:
            line += ('+' * (total_line_length - len(line)))
        bar_chart += '\n' + line

    # drawing x-axis
    line = ''
    for category in categories:
        if category.name == categories[0].name:
            line += '    ---'
        elif category.name == categories[-1].name:
            line += '----'
        else:
            line += '---'
    bar_chart += '\n' + line

    # determining how many times to loop/lines to add
    longest_category_name = 0
    for category in categories:
        if len(category.name) > longest_category_name:
            longest_category_name = len(category.name)

    # writing category names vertically
    lines_written = 0
    while lines_written < longest_category_name:
        line = ''
        for category in categories:
            if category.name == categories[0].name:
                try:
                    line += '     ' + category.name[lines_written]
                except:
                    line += '      '
            else:
                try:
                    line += '  ' + category.name[lines_written]
                except:
                    line += '   '
        bar_chart += '\n' + line
        lines_written += 1

    return bar_chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, auto, clothing]))
'''
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")



food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
'''