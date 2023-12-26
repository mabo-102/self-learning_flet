# 関数

```python:
def add(a: int, b: int) -> int:
    """Add a + b.

    This function sums up two arguments and return the result.

    Parameters
    ----------
    a : int
        A value to be added and return. Must support addition with b.
    b : int
        A value to be added and return. Must support addition with a.

    Examples
    --------
    >>> add(1, 2)
    3
    """
    return a + b
```

# クラス

## クラス定義

```python:
class User:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
```

## デコレータ

```python:
@staticmethod
def f(arg):
    ...
```

## プロパティ

```python:
class Potato:
    def __init__(self):
        self._price = None
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
    
    @price.deleter
    def price(self):
        del self._price
```

## データクラス

```python:
from dataclasses import dataclass


@dataclass
class User:
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}" 
```

## 継承

```python:
class VipUser(User):
    def discount(self) -> float:
        percent = 10.0
        return percent
```