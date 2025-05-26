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