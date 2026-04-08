"""
Week 3 practice: regular classes and object responsibilities.
"""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


def run_demo() -> None:
    account = BankAccount("Kevin", 100.0)
    account.deposit(25.0)
    account.withdraw(40.0)
    print("Owner:", account.owner)
    print("Balance:", account.balance)


if __name__ == "__main__":
    run_demo()
