'''
shipping_cost.py
Control Flow Exercise 2: Shipping Cost
Write calculate_shipping(order_total, is_member) that returns:
"Invalid total" if order_total is negative.
0 if the order is at least $100.
5 if the customer is a member and the order is at least $50.
10 for every other valid order.
Rules are evaluated in that priority order. Use if, elif, and else.
'''
def calculate_shipping(order_total, is_member):

    if order_total < 0:
        return "Invalid total"
    elif order_total >= 100:
        return 0
    elif is_member and order_total >= 50:
        return 5
    else:
        return 10



    # 5 if the customer is a member and the order is at least $50.
    if is_member and order_total >= 50:
        if order_total > 100:
            return 0
        else:
            return 5
    elif order_total >= 100:
        return 0
    elif order_total < 0:
        return "Invalid total"
    else:
        return 10  

print(calculate_shipping(-5, True))    # Invalid total
print(calculate_shipping(100, False))  # 0
print(calculate_shipping(120, True))   # 0
print(calculate_shipping(50, True))    # 5
print(calculate_shipping(75, True))    # 5
print(calculate_shipping(75, False))   # 10
print(calculate_shipping(25, True))    # 10
print(calculate_shipping(0, False))    # 10