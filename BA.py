class BankAccount:
    def __init__(self, name, initial_balance=0, currency="UAH"):
        self.name = name
        self.balance = initial_balance
        self.currency = currency
        self.transactions = []

    def deposit(self, amount, comment=None):
        if isinstance(amount, list):
            self.balance += sum(amount)
            self.transactions.append(("Deposit", sum(amount)))
        else:
            self.balance += amount
            self.transactions.append(("Deposit", amount, comment))

    def withdraw(self, amount, currency=None):
        if isinstance(amount, list):
            for amt in amount:
                self._withdraw_amount(amt)
        else:
            self._withdraw_amount(amount, currency)

    def _withdraw_amount(self, amount, currency=None):
        exchange_rate = 40 if currency == "USD" else 1
        converted_amount = amount * exchange_rate
        if self.balance >= converted_amount:
            self.balance -= converted_amount
            self.transactions.append(("Withdraw", converted_amount, currency))
        else:
            print("Insufficient funds")

    def transfer(self, amount, account=None, comment=None):
        if account:
            self.withdraw(amount)
            account.deposit(amount)
            self.transactions.append(("Transfer", amount, comment))
        else:
            print("No account specified")

    def get_account_info(self, detailed=False, as_dict=False):
        info = {
            "name": self.name,
            "balance": self.balance
        }
        if detailed:
            info.update({
                "currency": self.currency,
                "transactions": self.transactions,
                "transaction_count": len(self.transactions)
            })
        if as_dict:
            return info
        return str(info)

class PremiumAccount(BankAccount):
    def deposit(self, amount, comment=None):
        bonus = amount * 0.01 if isinstance(amount, (int, float)) else sum(amount) * 0.01
        super().deposit(amount + bonus, comment)

    def withdraw(self, amount, currency=None):
        exchange_rate = 40 if currency == "USD" else 1
        converted_amount = amount * exchange_rate
        if self.balance - converted_amount >= -1000:
            self.balance -= converted_amount
            self.transactions.append(("Withdraw", converted_amount, currency))
        else:
            print("Overdraft limit exceeded")

    def transfer(self, amount, account=None, comment=None):
        fee = amount * 0.005
        total_amount = amount + fee
        super().transfer(total_amount, account, comment)

def main():
    accounts = {}
    while True:
        print("\nМеню:")
        print("1. Создать аккаунт")
        print("2. Пополнить счёт")
        print("3. Снять деньги")
        print("4. Перевести деньги")
        print("5. Показать информацию о счёте")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите имя владельца: ")
            initial_balance = float(input("Введите начальный баланс (по умолчанию 0): ") or 0)
            currency = input("Введите валюту (по умолчанию UAH): ") or "UAH"
            account_type = input("Тип аккаунта (обычный/premium): ")
            accounts[name] = PremiumAccount(name, initial_balance, currency) if account_type.lower() == "premium" else BankAccount(name, initial_balance, currency)
            print("Аккаунт создан!")

        elif choice == "2":
            name = input("Введите имя владельца: ")
            if name in accounts:
                amount = float(input("Введите сумму: "))
                accounts[name].deposit(amount)
                print("Счёт пополнен!")
            else:
                print("Аккаунт не найден.")

        elif choice == "3":
            name = input("Введите имя владельца: ")
            if name in accounts:
                amount = float(input("Введите сумму: "))
                accounts[name].withdraw(amount)
                print("Снятие выполнено!")
            else:
                print("Аккаунт не найден.")

        elif choice == "4":
            sender = input("Введите имя отправителя: ")
            receiver = input("Введите имя получателя: ")
            if sender in accounts and receiver in accounts:
                amount = float(input("Введите сумму перевода: "))
                accounts[sender].transfer(amount, accounts[receiver])
                print("Перевод выполнен!")
            else:
                print("Один из аккаунтов не найден.")

        elif choice == "5":
            name = input("Введите имя владельца: ")
            if name in accounts:
                print(accounts[name].get_account_info(detailed=True))
            else:
                print("Аккаунт не найден.")

        elif choice == "6":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
