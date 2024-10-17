from calculator import rpn_calculate
import pytest
from fastapi import HTTPException

def test_rpn_calculate():
    assert rpn_calculate(["3", "4", "+", "2", "*"]) == 14.0
    assert rpn_calculate(["10", "5", "/"]) == 2.0
    assert rpn_calculate(["2", "3", "+", "4", "*"]) == 20.0
    with pytest.raises(HTTPException):
        rpn_calculate(["3", "+"])
