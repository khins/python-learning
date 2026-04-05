"""
Mini project: inventory manager using Python data structures.

This project demonstrates how lists, tuples, sets, dicts, and collections
work together in a small real-world task.
"""

from collections import Counter, defaultdict, deque, namedtuple
from typing import Dict, List, Deque, Tuple

Product = namedtuple('Product', ['sku', 'name', 'category', 'price'])


class InventoryManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.stock: Dict[str, int] = {}
        self.categories: set[str] = set()
        self.recent_transactions: Deque[Tuple[str, str, int]] = deque(maxlen=10)
        self.sales_counter: Counter[str] = Counter()

    def add_product(self, sku: str, name: str, category: str, price: float, quantity: int) -> None:
        if sku in self.products:
            raise ValueError(f'Product {sku} already exists')
        product = Product(sku, name, category, price)
        self.products[sku] = product
        self.stock[sku] = quantity
        self.categories.add(category)
        self.recent_transactions.append(('add', sku, quantity))

    def restock(self, sku: str, quantity: int) -> None:
        if sku not in self.products:
            raise KeyError(f'Unknown product {sku}')
        self.stock[sku] += quantity
        self.recent_transactions.append(('restock', sku, quantity))

    def sell(self, sku: str, quantity: int) -> None:
        if sku not in self.products:
            raise KeyError(f'Unknown product {sku}')
        if self.stock[sku] < quantity:
            raise ValueError(f'Not enough stock for {sku}')
        self.stock[sku] -= quantity
        self.sales_counter[sku] += quantity
        self.recent_transactions.append(('sell', sku, quantity))

    def inventory_report(self) -> List[Dict[str, object]]:
        report = []
        for sku, product in self.products.items():
            report.append({
                'sku': sku,
                'name': product.name,
                'category': product.category,
                'stock': self.stock.get(sku, 0),
                'price': product.price,
            })
        return report

    def top_selling(self, n: int = 3) -> List[Tuple[str, int]]:
        return self.sales_counter.most_common(n)

    def categories_summary(self) -> Dict[str, List[str]]:
        groups: defaultdict[str, List[str]] = defaultdict(list)
        for sku, product in self.products.items():
            groups[product.category].append(product.name)
        return dict(groups)

    def available_categories(self) -> List[str]:
        return sorted(self.categories)

    def recent_activity(self) -> List[Tuple[str, str, int]]:
        return list(self.recent_transactions)


def run_demo() -> None:
    manager = InventoryManager()
    manager.add_product('p001', 'Notebook', 'Stationery', 2.50, 50)
    manager.add_product('p002', 'Water Bottle', 'Drinkware', 10.00, 30)
    manager.add_product('p003', 'Pen', 'Stationery', 1.25, 100)

    manager.sell('p001', 3)
    manager.sell('p003', 12)
    manager.restock('p002', 15)
    manager.sell('p002', 5)

    print('Inventory report:')
    for row in manager.inventory_report():
        print(row)

    print('\nTop selling products:')
    for sku, count in manager.top_selling(2):
        product = manager.products[sku]
        print(f'{product.name} ({sku}): {count}')

    print('\nCategories summary:')
    for category, items in manager.categories_summary().items():
        print(f'{category}:', items)

    print('\nAvailable categories:', manager.available_categories())
    print('Recent activity:', manager.recent_activity())


if __name__ == '__main__':
    run_demo()
