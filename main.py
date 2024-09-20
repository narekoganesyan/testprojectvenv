# Определение класса
class Car:
    # Конструктор класса (__init__) для инициализации объектов
    def __init__(self, brand, model, year):
        self.brand = brand  # Атрибут марки автомобиля
        self.model = model  # Атрибут модели автомобиля
        self.year = year    # Атрибут года выпуска


    # Метод для вывода информации о машине
    def car_info(self):
        return f'{self.year} {self.brand} {self.model}'


    # Метод для обновления года выпуска
    def update_year(self, new_year):
        self.year = new_year
        return f'Год обновлен: {self.year}'


    # Метод для проверки возраста автомобиля
    def car_age(self, current_year):
        age = current_year - self.year
        return f'Возраст машины: {age} лет'


# Создание объекта класса Car
my_car = Car("Toyota", "Corolla", 2015)


# Вызов метода для получения информации о машине
print(my_car.car_info())  # Вывод: 2015 Toyota Corolla


# Обновление года выпуска
print(my_car.update_year(2018))  # Вывод: Год обновлен: 2018


# Проверка возраста автомобиля
print(my_car.car_age(2024))  # Вывод: Возраст машины: 6 лет
