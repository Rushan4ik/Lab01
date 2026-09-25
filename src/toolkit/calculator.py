import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
from .errors import * 
from .constant import OPERATORS, check_type
from .tokenization import tokenization
from .validation import validation, check_unary
from .estimation import estimation



def calculate(expression: list[str]) -> float:
    tokens = tokenization(expression)
    validation(tokens)
    return estimation(tokens)

