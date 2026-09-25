import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
from .errors import * 
from .constant import OPERATORS, check_type
from .tokenization import tokenization
from .validation import validation, check_unary

getcontext().rounding = ROUND_HALF_UP
getcontext().prec = 12

def estimation(tokens) -> float:
    tokens = list(tokens)
    tokens = check_unary(tokens)

    i = 1
    while i + 1 < len(tokens):
        if tokens[i] in ('*', '/', '%', '//'):
            a, b = tokens[i-1], tokens[i+1]
            if tokens[i] == '*':
                res = a*b
            elif tokens[i] == '/':
                if b == 0:
                    division_by_zero()
                    
                res = a/b
            elif tokens[i] == '//':
                if b == 0:
                    division_by_zero()
                    
                res = Decimal(int(a)//int(b))
            else:
                if b == 0:
                    division_by_zero()
                    
                res = Decimal(int(a)%int(b))
            tokens[i-1:i+2] = [res]
        else: i += 2
    
    result = tokens[0]  
    i = 1
    while i < len(tokens):
        if tokens[i] == '+':
            result += tokens[i+1]
        else:
            result -= tokens[i+1]
        i += 2
    return float(result)