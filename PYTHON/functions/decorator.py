def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} started.")
        result = func(*args)
        print(f"{func.__name__} finished.")
        result /= int('2')
        return result

    return wrapper

@logger
def summ(a, b): # в этот момент summ = wrapper
    c = a + b
    return c


if __name__ == "__main__":
    # function = logger(summ)
    # print(function(1, 2))

    # print(logger(summ)(1, 2))

    # summ = logger(summ)
    # print(summ(2, 3))

    print(summ(2, 3))