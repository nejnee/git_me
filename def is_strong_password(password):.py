def is_strong_password(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit


def collect_strings(items):
    new_list = []  
    for item in items:
        if isinstance(item, str):
            new_list.append(item)  
    return new_list

print(collect_strings([10, 'sfsdf', 20, [30, 40], 'abc']))
print(collect_strings([10, 'sfsdf', 'abc']))



def merge_schedules(schedule1, schedule2):
    merged = {}

    for day, tasks in schedule1.items():
        merged[day] = tasks.copy()

    for day, tasks in schedule2.items():
        if day in merged:
            merged[day].extend(tasks) 
        else:
            merged[day] = tasks.copy()
    
    return merged

main_schedule = {
    'Понедельник': ['почитать', 'сходить на йогу'],
    'Вторник': ['занятие по грузинскому']
}

extra_tasks = {
    'Понедельник': ['купить продукты'],
    'Среда': ['посмотреть лекцию']
}

print(merge_schedules(main_schedule, extra_tasks))

<<<<<<< HEAD
def remove_odds(numbers):
    new_list = []
    for num in numbers:
        if num == 0:
            continue
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(remove_odds([1, 2, 3, 4, 5, 6]))
=======
>>>>>>> d0adbee (added smth new)

# Участники соревнований в разные дни
day1 = ["Alice", "Bob", "Charlie", "Diana", "Eva"]
day2 = ["Charlie", "Fiona", "George", "Bob", "Helen"]

# Преобразуем списки в множества
set_day1 = set(day1)
set_day2 = set(day2)

# 1. Все участники за два дня (объединение)
all_participants = set_day1 | set_day2
print("Все участники за два дня:", all_participants)

# 2. Участники, которые были в оба дня (пересечение)
both_days = set_day1 & set_day2
print("Участники, которые были оба дня:", both_days)

# 3. Участники, которые были только в один из дней (симметрическая разность)
only_one_day = set_day1 ^ set_day2
print("Участники, которые были только в один из дней:", only_one_day)

# 4. Проверка: все ли из первого дня были во второй
is_subset = set_day1.issubset(set_day2)
print("Все ли участники первого дня были во второй день?", is_subset)

# 5. Общее количество уникальных участников
print("Общее количество уникальных участников:", len(all_participants))


robototechnics = ["Anna", "Boris", "Dina", "Egor", "Fedor"]
programming = ["Dina", "Egor", "Gleb", "Hana", "Ivan"]
mathematics = ["Anna", "Gleb", "Ivan", "Julia"]


set_rbt = set(robototechnics)
set_prg = set(programming)
set_mth = set(mathematics)

only_one = (
    (set_rbt - set_prg - set_mth) |
    (set_prg - set_rbt - set_mth) |
    (set_mth - set_rbt - set_prg)
)
print("Ходят только в один кружок:", only_one)


from datetime import datetime

birthdays = ["14.03.1990", "01.01.2000", "25.12.1985"]
today = datetime.today()

def calculate_age(birth_str):
    birth = datetime.strptime(birth_str, "%d.%m.%Y")
    years = today.year - birth.year
    if (today.month, today.day) < (birth.month, birth.day):
        years -= 1
    return years

sorted_birthdays = sorted(birthdays, key=lambda d: calculate_age(d))

for b in sorted_birthdays:
    print(f"{b} — {calculate_age(b)} лет")


def calculator():
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Введите операцию (+, -, *, /): ")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        else:
            raise ValueError("Неверная операция!")

    except ValueError as e:
        print("Ошибка:", e)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль запрещено!")
    else:
        print("Результат:", result)

import random

participants = list(range(1, 101))
winners = random.sample(participants, 6)
super_winner = winners[0]
other_winners = sorted(winners[1:])

print("Суперпобедитель:", super_winner)
print("Остальные победители:", other_winners)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"«{self.title}», автор: {self.author}, год: {self.year}"


book1 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967)
book2 = Book("1984", "Джордж Оруэлл", 1949)

print(book1.info())
print(book2.info())


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Снятие: -{amount}")
        else:
            self.history.append("Снятие: недостаточно средств")

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history


acc = BankAccount("Анна", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)
print("Баланс:", acc.get_balance())
print("История операций:")
for h in acc.get_history():
    print(h)