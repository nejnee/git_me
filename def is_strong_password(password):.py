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