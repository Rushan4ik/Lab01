import decimal
from decimal import Decimal, getcontext, ROUND_HALF_UP
from .errors import * 


def tokenization(expression: str) -> list[str]:
    tokens = []
    number = ''
    expression = expression.replace(' ', '')

    if not expression:
        empty_expression()
        
    i = 0
    while i < len(expression):
        element = expression[i]

        if element.isdigit() or element == '.':
            number += element
            i += 1
        elif element in '%+-':
            if number:
                try:
                    tokens.append(Decimal(number))
                except decimal.InvalidOperation:
                    wrong_value()
                    
                number = ''
            tokens.append(element)
            i += 1
        elif element == '/':
            if number:
                try:
                    tokens.append(Decimal(number))
                except decimal.InvalidOperation:
                    wrong_value()
                    
                number = ''
            if i + 1 < len(expression) and expression[i+1] == '/':
                tokens.append('//')
                i += 2
            else:
                tokens.append('/')
                i += 1
        elif element == '*':
            if number:
                try:
                    tokens.append(Decimal(number))
                except decimal.InvalidOperation:
                    wrong_value()
                    
                number = ''
            tokens.append('*')
            i += 1
        else:
            unexpected_symbol()
            
    if number:
        try:
            tokens.append(Decimal(number))
        except decimal.InvalidOperation:
            wrong_value()
    return tokens