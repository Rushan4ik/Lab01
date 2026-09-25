from datetime import datetime

OPERATORS = {'*', '/', '//', '%', '+', '-'}
def check_type(a, b):
    return type(a) == type(b)

length_units = ['mm', 'cm', 'm', 'km']
mass_units = ['g', 'kg']
temp_units = ['c', 'k', 'f']
length_to_m = {
    'mm': 0.001,
    'cm': 0.01,
    'm': 1.0,
    'km': 1000
}
mass_to_g = {
    'g': 0.001,
    'kg': 1.0,
}

YEAR, MONTH, DAY, HOUR, MINUTE = datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute
