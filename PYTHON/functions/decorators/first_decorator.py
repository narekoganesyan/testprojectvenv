def decorator(func):
    def inner(name, surname):
        print('Стартуем декоратор')
        func()
        print('Заканчиваем декоратор')
    return inner


@decorator
def say_hello_to(name, surname):
    print('hello', name, surname)

say_hello_to('Vasya', 'Ivanov')