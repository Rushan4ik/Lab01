import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
from .errors import * 
from .constant import OPERATORS, check_type


def validation(tokens: list[str]) -> None:
    if not tokens:
        missed_number()
        
    if check_type(tokens[0], ''):
        if tokens[0] not in '+-':
            wrong_start_expression(tokens[0])
            
        tokens = tokens[1:]
    if not tokens:
        missed_number()
        
    if check_type(tokens[-1], ''):
        missed_number()
    
    for i in range(len(tokens)-1):
        if check_type(tokens[i], '') and check_type(tokens[i+1], ''):
            if tokens[i] not in '+-':
                if tokens[i+1] not in '+-':
                    double_operands()
                    
                if i+2 >= len(tokens) or check_type(tokens[i+2], ''):
                    missed_number()
            else:
                if i+2 >= len(tokens) or check_type(tokens[i+2], ''):
                    missed_number()
def check_unary(tokens: list) -> list:
    result = []
    i = 0
    while i < len(tokens):
        is_sign = check_type(tokens[i], '') and tokens[i] in '+-'
        at_start = (i == 0)
        after_operator = (
            i > 0
            and check_type(tokens[i-1], '')
            and tokens[i-1] in OPERATORS  # *, /, //, %
        )
        after_sign = (
            i > 0
            and check_type(tokens[i-1], '')
            and tokens[i-1] in '+-'     
        )
        next_is_number = (
            i + 1 < len(tokens)
            and check_type(tokens[i+1], Decimal('0.1'))
        )

        if is_sign and (at_start or after_operator or after_sign) and next_is_number:
            sign = Decimal('1') if tokens[i] == '+' else Decimal('-1')
            result.append(sign * tokens[i+1])
            i += 2
        else:
            result.append(tokens[i])
            i += 1
    return result