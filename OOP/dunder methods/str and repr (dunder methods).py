class Lion:
    def __init__(self, name, surname, age, balance):
        self.name = name
        self.surname = surname
        self.age = age
        self.balance = balance

    def __repr__(self):
        return f"The object is Lion - {self.name}"

    def __str__(self):
        print(f"Эта функция подсказывает что делает этот класс. Это главный класс.")

    def __len__(self):
        return len(self.name + self.surname)

    def __abs__(self):
        self.age = abs(self.age)
        return self.age

    def __add__(self, other):
        print('__add__')
        if isinstance(other, Lion):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__')
        return self + other

    def __eq__(self, other):
        print('__eq__')
        if isinstance(other, Lion):
            return self.balance == other.balance

    def __lt__(self, other):
        print('__lt__')
        if isinstance(other, Lion):
            return self.balance < other.balance
        elif isinstance(other, (int, float)):
            return self.balance < other

    def __le__(self, other):
        print('__le__')
        return self < other or self == other

    # def __gt__(self, other):
    #     print('__gt__')
    #     if isinstance(other, Lion):
    #         return self.balance > other.balance
    #
    # def __le__(self, other):
    #     print('__le__')
    #     if isinstance(other, Lion):
    #         return self.balance <= other.balance