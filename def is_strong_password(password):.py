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