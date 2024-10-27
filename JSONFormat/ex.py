import json
import random
import string


# Функция для генерации случайной строки
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


# Функция для генерации случайных данных
def generate_data(num_entries):
    data = []
    for _ in range(num_entries):
        entry = {
            "id": random.randint(1, 10000),
            "name": random_string(10),
            "age": random.randint(18, 90),
            "email": random_string(5) + "@example.com",
            "city": random_string(8),
            "salary": round(random.uniform(30000, 100000), 2)
        }
        data.append(entry)
    return data


# Генерация данных
large_data = {
    "employees": generate_data(10000)  # 10000 записей
}

# Запись в JSON файл
with open('large_data.json', 'w') as json_file:
    json.dump(large_data, json_file, indent=4)

print("Большой JSON файл создан")
