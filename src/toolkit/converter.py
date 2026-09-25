from .constant import length_units, mass_units, temp_units, length_to_m, mass_to_g
import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
from .errors import *

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 12

def normalization(unit: str) -> str:
    return unit.strip().lower()

UNITS = length_units+mass_units+temp_units

def validation(value: Decimal, unit1: str, unit2: str) -> None:
    if unit1 not in UNITS:
        unknown_unit()
        # raise ToolkitError(f'Неизвестная единица измерения: {unit1}')
    if unit2 not in UNITS:
        unknown_unit()
        # raise ToolkitError(f'Неизвестная единица измерения: {unit2}')

    def group(unit: str) -> str:
        if unit in length_units:
            return 'length'
        if unit in mass_units:
            return 'mass'
        return 'temp'

    if group(unit1) != group(unit2):
        incompatible_units()
        # raise ToolkitError(f'Конвертация между разными группами запрещена: 'f"'{unit1-> '{unit2}'")

    # проверка абсолютного нуля для температур
    if unit1 in temp_units:
        if unit1 == 'c':
            k = value + Decimal(273)
        elif unit1 == 'f':
            k = (value - 32) * Decimal(5) / Decimal(9) + Decimal(273)
        else:
            k = value
        if k < 0:
            absolute_temperature()
            # raise ToolkitError('Температура ниже абсолютного нуля запрещена')


def estimation(value: Decimal, unit1: str, unit2: str) -> Decimal:
    if unit1 in length_units:
        meters = value * Decimal(str(length_to_m[unit1]))
        return meters / Decimal(str(length_to_m[unit2]))

    elif unit1 in mass_units:
        grams = value * Decimal(str(mass_to_g[unit1]))
        return grams / Decimal(str(mass_to_g[unit2]))

    else:  # температуры
        if unit1 == 'c':
            k = value + Decimal(273)
        elif unit1 == 'f':
            k = (value - 32) * Decimal(5) / Decimal(9) + Decimal(273)
        else:
            k = value

        if unit2 == 'c':
            return k - Decimal(273)
        elif unit2 == 'f':
            return (k - Decimal(273)) * Decimal(9) / Decimal(5) + Decimal(32)
        else:
            return k

def convert(value: float, unit1: str, unit2: str) -> Decimal:
    unit1, unit2 = normalization(unit1), normalization(unit2)
    value = Decimal(str(value))
    validation(value, unit1, unit2)
    return estimation(value, unit1, unit2)


