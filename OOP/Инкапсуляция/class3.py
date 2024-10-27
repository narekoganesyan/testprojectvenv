# from accessify import private, protected, accessify, implements


# class Car:
#
#     @protected
#     def start_engine(self):
#         return 'Engine sound.'
#
#
# class Tesla(Car):
#
#     def run(self):
#         return self.start_engine()
#
#
# if __name__ == '__main__':
#     tesla = Tesla()
#     print(tesla.run())
#
#
# class Car:
#
#     @private
#     def start_engine(self):
#         return 'Engine sound.'
#
#     def run(self):
#         return self.start_engine()
#
#
# if __name__ == '__main__':
#     car = Car()
#     car.start_engine()


# @accessify
# class Car:
#
#     @private
#     def start_engine(self):
#         return 'Engine sound.'
#
#
# if __name__ == '__main__':
#     car = Car()
#
#     assert 'start_engine' not in dir(car)


# class HumanInterface:
#
#     @staticmethod
#     def eat(food, *args, allergy=None, **kwargs):
#         pass
#
#
# if __name__ == '__main__':
#
#     @implements(HumanInterface)
#     class Human:
#
#         pass