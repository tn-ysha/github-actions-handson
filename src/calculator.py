"""電卓モジュール。基本的な四則演算を提供する。"""



def add(a: float, b: float) -> float:
    """2つの数値を加算する。"""
    return a + b


def subtract(a: float, b: float) -> float:
    """2つの数値を減算する。"""
    return a - b


def multiply(a: float, b: float) -> float:
    """2つの数値を乗算する。"""
    return a * b


def divide(a: float, b: float) -> float:
    """2つの数値を除算する。0除算時はValueErrorを送出する。"""
    if b == 0:
        raise ValueError("0で割ることはできません")
    return a / b
