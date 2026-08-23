"""
1. Warm-up: variables and arithmetic — 5 minutes
Given:
hours_worked = 38
hourly_rate = 24.50
tax_rate = 0.18
Write code that calculates and prints:
Gross pay
Estimated taxes
Net pay
Format each amount to two decimal places.
"""
hours_worked = 38
hourly_rate = 24.50
tax_rate = 0.18
gross_pay = hours_worked * hourly_rate
estimated_tax = gross_pay * tax_rate
net_pay = gross_pay - estimated_tax

print(f"Gross pay = ${gross_pay:.2f}")
print(f'Estimated Tax = ${estimated_tax:.2f}')
print(f'Net pay = ${net_pay:.2f}')
