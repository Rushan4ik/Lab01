import sys

def throw_error(error: str):
    sys.stderr.write("Ошибка:" + error + "\n")
    sys.exit(2)

def empty_expression():
    sys.stderr.write("Пустое выражение\n")
    sys.exit(2)

def double_operands():
    sys.stderr.write("Два оператора стоят рядом\n")
    sys.exit(2)

def unexpected_symbol():
    sys.stderr.write("Выражение содержит неизвестные операторы\n")
    sys.exit(2)

def absolute_temperature():
    sys.stderr.write("Температура ниже абсолютного нуля")
    sys.exit(2)


def missing_operand():
    sys.stderr.write("Отсуствует оператор в выражении\n")
    sys.exit(2)


def division_by_zero():
    sys.stderr.write("Деление на ноль запрещено\n")
    sys.exit(2)

def wrong_value():
    sys.stderr.write("Неправильное значение\n")
    sys.exit(2)

def unknown_unit():
    sys.stderr.write("Выражение содержит неизвестные единицы измерения\n")
    sys.exit(2)


def incompatible_units():
    sys.stderr.write("Нельзя преобразовать эти единицы измерения\n")
    sys.exit(2)

def missed_number():
    sys.stderr.write("Пропущено число\n")
    sys.exit(2)

def wrong_start_expression(operation):
    sys.stderr.write(f'Выражение не может начинаться с {operation}')
    sys.exit(2)

