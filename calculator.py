from fastapi import HTTPException
from typing import List

def rpn_calculate(expression: List[str]) -> float:
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(float(token))
        else:
            try:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
                else:
                    raise HTTPException(status_code=400, detail="Invalid operator")
            except IndexError:
                raise HTTPException(status_code=400, detail="Invalid expression")
    if len(stack) != 1:
        raise HTTPException(status_code=400, detail="Invalid expression")
    return stack[0]