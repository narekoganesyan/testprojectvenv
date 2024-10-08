class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return (f'{self.__class__.__name__} {self.name}, оклад={self.salary}, максимальный процент'
                f' бонуса={self.bonus}%, '
                f'бонусы={self.calculate_salary()}руб, '
                f'полная зарплата и бонусы={self.calculate_salary() + self.salary}рублей.')


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)


class Director(Employee):
    def __init__(self, name):
        super().__init__(name, 105000, 100)


if __name__ == '__main__':
    a = []
    cleaner = Cleaner('Nina')
    print(cleaner)
    manager = Manager('Alex')
    print(manager)
    director = Director('Malik')
    print(director)
