def is_valid(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack


# Примеры использования:
# print(is_valid(""))  # Ожидаемый результат: True
# print(is_valid("()"))  # Ожидаемый результат: True
# print(is_valid("()[]{}"))  # Ожидаемый результат: True
# print(is_valid("(]"))  # Ожидаемый результат: False
# print(is_valid("([)]"))  # Ожидаемый результат: False
# print(is_valid("{[]}"))  # Ожидаемый результат: True
# print(is_valid("("))  # Ожидаемый результат: False
# print(is_valid(")"))  # Ожидаемый результат: False
# print(is_valid("([{}])"))  # Ожидаемый результат: True