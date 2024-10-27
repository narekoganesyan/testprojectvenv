from accessify import private

class BankAccount:
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)

    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)

    @private
    def print_private_data(self):
        print(self.name, self.balance, self.passport)

    def run_print_private_method(self):
        self.print_private_data()

account1 = BankAccount('Bank A', 2000000, 12345421)

account1.print_private_data()

