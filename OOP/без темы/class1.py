class Purse:
    '''Онлайн кошелек'''

    def __init__(self, currency, name='Unknown'):
        self.money = 0.00
        self.name = name
        self.currency = currency

    def top_up_balance(self, hmm):
        self.money += hmm

    def top_down_balance(self, hmm):
        if self.money >= hmm:
            self.money -= hmm
        else:
            raise ValueError('Транзакция недоступна. Вы хотите снять больше, чем есть в кошельке.')

    def name_of_the_cart(self):
        print(f"{self.name.capitalize()} - {f'{self.money} {self.currency}'}")


x = Purse('RUB', 'Narek')
x.top_up_balance(92000)
print(x.__class__.__doc__)
x.name_of_the_cart()
x.top_down_balance(89000)
x.name_of_the_cart()

y = Purse('USDT', 'David')

y.name_of_the_cart()
y.top_up_balance(110)
y.top_down_balance(110)
y.name_of_the_cart()
