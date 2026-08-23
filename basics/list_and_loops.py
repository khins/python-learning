'''
transactions = [125.50, -40.00, 75.25, -15.50, 200.00, -80.25]
Write code that determines:
The total of all transactions
The total income, using only positive values
The total expenses, reported as a positive number
The number of income transactions
The number of expense transactions
'''

transactions = [125.50, -40.00, 75.25, -15.50, 200.00, -80.25]
total = 0
total_income = 0
total_expenses = 0
income_count = 0
expense_count = 0

for number in transactions:
    total = total + number
    
    if number > 0:
        income_count += 1
        total_income += number
    elif number < 0:
        expense_count += 1
        total_expenses += number
        
print(f'The total of all transactions: {total}')
print(f'Total Income: {total_income}')
print(f'The total expenses: {total_expenses}')
print(f'The number of income transactions: {income_count}')
print(f'The number of expense transactions: {expense_count}')
        